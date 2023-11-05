from services.productServices import GetProducts, GetProductById, GetSortedProductsByParams, DeleteProductByIdx, PutProductByIdx, PostProduct
from services.productServices import showlist_product, create_product, printAllProduct
from services.cartServices import GetCarts

def GetProductsController(): 
    printAllProduct()
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
            showlist_product(products)

def SearchProductByIdController():
    sku = input("Masukkan sku atau product name : ")
    products = GetProductById(sku)
    if len(products) > 0: showlist_product(products)
    else: print("Mohon maaf, data yang ada cari tidak ada.")

def DeleteProductByIdController():
    products = GetProducts()
    showlist_product(products, withIndex=True)
    index = int(input(f"\n\nMasukkan index yang ingin dihapus (0-{len(products)-1}) : "))
    DeleteProductByIdx(index)
    printAllProduct()

def PutProductByIdController():
    val = ""
    products = GetProducts()
    showlist_product(products, withIndex=True)
    index = int(input(f"\n\nMasukkan index yang ingin diubah (0-{len(products)-1}) : "))
    print("\n\nTekan enter jika data tidak ingin diubah")
    for key in products[index].keys():
        if key == "sku": continue
        elif isinstance(products[index][key], str):
            val = input(f"Masukkan {key} : ")
            if val != "" : products[index][key] = val
        elif isinstance(products[index][key], int):
            val = input(f"Masukkan {key} : ")
            if val != "" : products[index][key] = int(val)
        elif isinstance(products[index][key], list):
            val = input(f"Masukkan {key} pisahkan dengan , jika lebih dari 1.\ncontoh: fragrance, parfume : ")
            if val != "" : products[index][key] = val.split(",")

    PutProductByIdx(index, products[index])
    printAllProduct()

def PostProductController():
    product = create_product();
    isSuccessAdd = PostProduct(product)
    if isSuccessAdd:
        printAllProduct()
    else: 
        print("Product yang di input sudah ada, silakan input sku atau nama product yang lain\n")
        PostProductController()

def PostBuyProductController():
    printAllProduct(withIndex=True)
    current_cart = GetCarts()
    print(current_cart)
