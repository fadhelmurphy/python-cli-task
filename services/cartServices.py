from models.cart import list_cart

def GetCarts():
    return list_cart

def PostCart(payload):
    list_cart.append(payload)