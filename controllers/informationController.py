from helpers import separator

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
[2] : Menampilkan product berdasarkan nama produk atau sku
        """)