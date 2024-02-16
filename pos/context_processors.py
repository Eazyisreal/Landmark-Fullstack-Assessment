def cart_items_processor(request):
    cart_items = request.session.get('cart', {})
    total_items_in_cart = sum(cart_items.values())
    return {'total_items_in_cart': total_items_in_cart}
