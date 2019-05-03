from .cart import Cart

def general_processors(request):
    return {
        'cart': Cart(request) 
    }
