from services.cartServices import GetCarts
def GetCartsController():
    carts = GetCarts()
    print(carts)

    