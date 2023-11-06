from services.cartServices import printAllCarts, PostCartsCheckout, DeleteCartByIdx, PutCartByIdx
from services.productServices import printAllProduct, GetProductById
import app

def GetCartsController():
    carts = printAllCarts(withIndex=True)
    if len(carts) > 0:

        print(f"""
[1] : Menghapus product pada keranjang
[2] : Mengganti stok product pada keranjang
[9] : Kembali ke menu sebelumnya
            """)
        cartMenu = int(input("Pilih menu : "))
        if cartMenu == 1:
            index = input(f"Masukan index yang ingin dihapus? (0 - {len(carts)-1}) : ").lower()
            DeleteCartByIdx(index)
        elif cartMenu == 2:
            index = int(input(f"Masukan index yang ingin diubah stoknya? (0 - {len(carts)-1}) : "))
            stok = int(input("Masukkan stok dalam bentuk angka : "))
            cart = carts[index].copy()
            product = GetProductById(cart["sku"]).copy()[0].copy()
            cart["stock"] = stok
            cart["price"] = stok * product["price"]
            PutCartByIdx(index, cart)

        printAllCarts()
    app.backToPrevMenu()


def PostCartsCheckoutController():
    print("""
Checkout page""")
    printAllCarts()
    isCheckout = input(f"Ingin melanjutkan transaksi? (y / t) : ").lower()
    if isCheckout == "y":
        PostCartsCheckout()
        printAllProduct()
    



    