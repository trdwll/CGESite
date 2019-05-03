from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.conf import settings
from django.utils import timezone
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse

from decimal import Decimal

from .tasks import order_created
from .cart import Cart
from .forms import (
    CartAddProductForm, 
    CouponApplyForm, 
    OrderCreateForm
)

from .models import (
    Product, 
    Coupon, 
    Order, 
    OrderItem
)


# import weasyprint


class StoreHomeView(ListView):
    model = Product
    template_name = 'store/index.html'
    paginate_by = 5
    context_object_name = 'products'



class StoreProductView(View):
    template_name = 'store/product.html'

    def get(self, request, product_id, product_slug):
        # cart = Cart(request)
        # cart.clear()
        
        if settings.DEBUG:
            for key, value in request.session.items():
                print('=== {} => {}'.format(key, value))

        product = get_object_or_404(Product, id=product_id, slug=product_slug)

        return render(request, self.template_name, {
            'product': product,
            'cart_product_form': CartAddProductForm()
        })


# Order

class OrderCreateView(View):
    template_name = ''

    def get(self, request):
        return render(request, self.template_name, {
            'form': OrderCreateForm()
        })

    def post(self, request):
        cart = Cart(request)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount

            order.save()

            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            
            # clear the cart
            cart.clear()

            # launch asynchronous task
            order_created.delay(order.id)

            # set the order in the session
            request.session['order_id'] = order.id

            # redirect to the payment
            return redirect('process_payment')
    
        return render(request, self.template_name, {
            'cart': cart, 
            'form': form
        })


# TODO: Require staff
class OrderAdminView(View):
    template_name = 'admin/orders/order/detail.html'

    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        return render(request, self.template_name, {'order': order})


# TODO: Require staff
class OrderAdminPDFView(View):
    template_name = 'orders/order/pdf.html'

    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        html = render_to_string(self.template_name, {'order': order})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="order_{}.pdf"'.format(order.id)
        #weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
        return response


# Coupon

class CouponApplyView(View):
    def post(self, request):
        now = timezone.now()
        form = CouponApplyForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                coupon = Coupon.objects.get(code__iexact=code,
                    valid_from__lte=now,
                    valid_to__gte=now,
                    is_active=True)
                request.session['coupon_id'] = coupon.id
            except Coupon.DoesNotExist:
                request.session['coupon_id'] = None

        return redirect('cart_page')


# Cart

class CartView(View):
    template_name = 'store/cart/index.html'
    
    def get(self, request):
        cart = Cart(request)

        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})

        return render(request, self.template_name, {
            'cart': cart,
            'coupon_apply_form': CouponApplyForm(),
        })


class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cart.add(
                product=product,
                quantity=form.cleaned_data['quantity'],
                update_quantity=form.cleaned_data['update']
            )

        return redirect('cart_page')


class CartRemoveView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)

        return redirect('cart_page')



# Payment

class StorePaymentProcessView(View):
    template_name = 'store/payment/process.html'

    def get(self, request):
        return render(request, self.template_name)

    # TODO: This may need to be a GET rather than a POST
    def post(self, request):
        order_id = request.session.get('order_id')
        order = get_object_or_404(Order, id=order_id)
        host = request.get_host()

        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': '%.2f' % order.get_total_cost().quantize(Decimal('.01')),
            'item_name': 'Order {}'.format(order.id),
            'invoice': str(order.id),
            'currency_code': 'USD',
            'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
            'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled')),
        }
        form = PayPalPaymentsForm(initial=paypal_dict)
        return render(request, 'payment/process.html', {
            'order': order, 
            'form':form
        })


class StorePaymentDoneView(View):
    template_name = 'store/payment/done.html'
    
    def get(self, request):
        return render(request, self.template_name)


class StorePaymentCanceledView(View):
    template_name = 'store/payment/canceled.html'
    
    def get(self, request):
        return render(request, self.template_name)