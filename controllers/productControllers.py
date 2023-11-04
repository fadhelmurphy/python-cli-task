from services.productServices import GetProducts, GetProductById, GetSortedProductsByParams
from helpers import showProductList, showProductDetail

def AllProductsController(): 
    products = GetProducts()
    showProductList(products)
    if len(products) > 0:
        isSorted = input("\nMau di sort? (y/t) : ").lower()
        if isSorted == "y":
            print("\nList kolom : ")
            list_products_kolom = [item for item in products[0].keys()]
            for idx, item in enumerate(list_products_kolom): print(f"[{idx}] : {item}")
            sortedBy = int(input(f"Pilih kolom yang ingin di sort (masukkan angka 0-{len(list_products_kolom)-1}) : "))
            isDescending = input("\nAscending / Descending? (a/d) : ").lower()
            isDescending = isDescending == "d"
            products = GetSortedProductsByParams(list_products_kolom[sortedBy], isDescending)
            showProductList(products)

def ProductByIdController():
    sku = input("Masukkan sku : ")
    products = GetProductById(sku)
    if len(products) > 0: showProductDetail(products)
    else: print("Mohon maaf, data yang ada cari tidak ada.")
