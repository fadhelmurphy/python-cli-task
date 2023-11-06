from services.cartServices import printAllCarts
from services.productServices import changeProductQty, printAllProduct
from models.product import list_product

def GetCartsController():
    carts = printAllCarts(withIndex=True)
    if len(carts) > 0:
        isDeleteItem = input("Ingin menghapus item di cart? (y / t) : ").lower()
        if isDeleteItem == "y":
            index = input(f"Masukan index yang ingin dihapus t? (0 - {len(carts)-1}) : ").lower()


def PostCartsCheckout():
    print("""
Checkout page""")
    global list_product
    carts = printAllCarts()
    isCheckout = input(f"Ingin melanjutkan transaksi? (y / t) : ").lower()
    if isCheckout == "y":
        for item in carts:
            sku, product_name, brand_name, category, price, stock = item.values()
            list_product = changeProductQty(val=stock, condVal=sku)
        printAllProduct()
    



    