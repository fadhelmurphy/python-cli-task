from helpers import separator
import app

def MainInformationController():
    print(f"""
Main Menu {separator}\n
[1] : Menuju Halaman Product
[6] : Menuju Halaman About
        """)

def ProductInformationController():
    print(f"""
Product Menu {separator}\n
Halo, Anda sedang berada di halaman Product

[1] : Menampilkan seluruh product
[2] : Mencari product berdasarkan nama produk atau sku
[3] : Menghapus satu product
[4] : Mengupdate satu product
[5] : Menambah satu product

[6] : Membeli product
[7] : Menampilkan keranjang
        """)
    
def AboutInformationController():
    print(f"""
{"=" * (len(separator)//2)} About {"=" * (len(separator)//2)}

This application build from scratch by Fadhel Ijlal Falah (Iron Man)
        """)
    app.backToMainMenu()