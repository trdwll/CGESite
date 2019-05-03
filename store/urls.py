
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.StoreHomeView.as_view(), name='store_home'),
    # path('<slug:product_slug>/', views.StoreProductView.as_view(), name='store_item_page'),

    # Payment Gateways
    path('paypal/', include('paypal.standard.ipn.urls')),

    # Coupon
    path('coupon/apply/', views.CouponApplyView.as_view(), name='apply_coupon'),

    # Cart
    path('cart/', views.CartView.as_view(), name='cart_page'),
    path('cart/add/<int:product_id>/', views.CartAddView.as_view(), name='cart_add_page'),
    path('cart/remove/<int:product_id>/', views.CartRemoveView.as_view(), name='cart_remove_page'),
    
    # Payment
    path('payment/process/', views.StorePaymentProcessView.as_view(), name='process_payment'),
    path('payment/done/', views.StorePaymentDoneView.as_view(), name='done_payment'),
    path('payment/canceled/', views.StorePaymentCanceledView.as_view(), name='canceled_payment'),

    # Order
    path('order/create/', views.OrderCreateView.as_view(), name='order_create'),
    
    # Admin
    path('admin/order/<int:order_id>/', views.OrderAdminView.as_view(), name='admin_order_detail'),
    path('admin/order/<int:order_id>/pdf/', views.OrderAdminPDFView.as_view(), name='admin_order_pdf'),
]