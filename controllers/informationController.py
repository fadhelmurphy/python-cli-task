from helpers import separator

def MainInformationController():
    print(f"""
Main Menu {separator}\n
[1] : Menampilkan product
[2] : Menambah satu product
[3] : Mengupdate satu product
[4] : Menghapus satu product

[5] : Membeli Product
[6] : Menampilkan Keranjang
[7] : Halaman Checkout
[99] : Menuju Halaman About
        """)

def GetProductsInformationController():
    print(f"""
GET Products Menu {separator}\n
Halo, Anda sedang berada di halaman GET Products

[1] : Menampilkan seluruh product
[2] : Mencari product berdasarkan sku
        """)
    
def AboutInformationController():
    print(f"""
{"=" * (len(separator)//2)} About {"=" * (len(separator)//2)}

This application build from scratch by Fadhel Ijlal Falah (Iron Man)
        """)