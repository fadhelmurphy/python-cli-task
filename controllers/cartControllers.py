from services.cartServices import GetCarts
from services.productServices import showlist_product

def GetCartsController():
    carts = GetCarts()
    showlist_product(carts)

    