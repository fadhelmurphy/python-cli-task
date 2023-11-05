from services.productServices import GetProductById, GetSortedProductsByParams, DeleteProductByIdx, PutProductByIdx, PostProduct
from services.productServices import showlist_product, create_product, printAllProduct, changeProductQty, GetIndexByProductId
from services.cartServices import GetCarts, PostCart

def GetProductsController(): 
    products = printAllProduct()
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
    else: 
        print("Mohon maaf, data yang ada cari tidak ada, silakan cari yang lain.\n")
        SearchProductByIdController()

def DeleteProductByIdController():
    printAllProduct()
    index = GetIndexByProductId()
    DeleteProductByIdx(index)
    printAllProduct()

def PutProductByIdController():
    val = ""
    products = printAllProduct()
    index = GetIndexByProductId()
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
    product = create_product()
    PostProduct(product)
    printAllProduct()

def PostBuyProductController():
    printAllProduct()
    isNotFound = True
    while isNotFound:
        sku = input(f"Masukkan sku yang ingin dibeli : ")
        products = GetProductById(sku)
        isNotFound = len(products) == 0
        if isNotFound: print("Mohon maaf, data yang ada cari tidak ada.")

    stock = int(input(f"Masukkan jumlah stock yang ingin dibeli : "))
    # current_product = changeProductQty(key="stock", val=stock, condKey="sku", condVal=sku).copy()
    # showlist_product(current_product)
    products = GetProductById(sku).copy()[0].copy()
    products["stock"] = stock
    PostCart(products)
    current_cart = GetCarts()
    showlist_product(current_cart)
