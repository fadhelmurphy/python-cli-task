from services.productServices import GetProductById, GetSortedProductsByParams, DeleteProductByIdx, PutProductByIdx, PostProduct
from services.productServices import showlist_product, create_product, printAllProduct, GetIndexByProductId, showProductDetail
from services.cartServices import PostCart, isCartExist, GetCartById, GetIndexByCartId, PutCartByIdx, printAllCarts, isCartExist
import app

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
            print("\nHasil sort product :\n\n")
            showlist_product(products)
    else: 
        print("Data doesn't exist")
        GetProductsController()
    app.backToPrevMenu()

def SearchProductByIdController():
    printAllProduct()
    sku = input("\nMasukkan sku : ")
    products = GetProductById(sku)
    print("\nHasil mencari product :")
    if len(products) > 0: 
        showlist_product(products)
        app.backToPrevMenu()
    else: 
        print("Data doesn't exist, try another sku.\n")
        SearchProductByIdController()

def DeleteProductByIdController():
    printAllProduct()
    index = GetIndexByProductId(breakIfNotFound=True)
    if index == -1:
        DeleteProductByIdController()
    else:
        DeleteProductByIdx(index)
        print("\nData successfully deleted\n")
        printAllProduct()
        app.backToPrevMenu()

def PutProductByIdController():
    val = ""
    products = printAllProduct()
    index = GetIndexByProductId(breakIfNotFound=True)
    if index == -1:
        PutProductByIdController()
    else:
        showProductDetail(products[index])

        print("Nama - nama kolom yang ada : \n")
        for key in products[index].keys():
            if key == "sku": continue
            else: print(f"{key}")
        
        print("\nTekan enter jika data tidak ingin diubah\n\n")
        key = input(f"Masukkan nama kolom : ")
        if key == "sku": pass
        elif isinstance(products[index][key], str):
            val = input(f"Masukkan {key} : ")
            if val != "" : products[index][key] = val
        elif isinstance(products[index][key], int):
            val = input(f"Masukkan {key} : ")
            if val != "" : products[index][key] = int(val)
        elif isinstance(products[index][key], list):
            val = input(f"Masukkan {key} pisahkan dengan , jika lebih dari 1.\ncontoh: fragrance, parfume : ")
            if val != "" : products[index][key] = val.split(",")

        if val != "":
            PutProductByIdx(index, products[index])
            printAllProduct()
            print("\nData successfully updated\n")
        app.backToPrevMenu()

def PostProductController():
    product = create_product()
    PostProduct(product)
    print("\nData successfully saved\n")
    printAllProduct()
    app.backToPrevMenu()

def PostBuyProductController():
    printAllProduct()
    isNotFound = True
    while isNotFound:
        sku = input(f"Masukkan sku yang ingin dibeli : ")
        products = GetProductById(sku)
        isNotFound = len(products) == 0
        if isNotFound: print("Mohon maaf, data yang ada cari tidak ada.")

    isntAddToCart = True
    product = GetProductById(sku).copy()[0].copy()
    cart = {}
    if isCartExist(sku):
        cart = GetCartById(product["sku"]).copy()[0].copy()
    else:
        cart = {"stock": 0}
    while isntAddToCart:
        stock = int(input(f"Masukkan jumlah stock yang ingin dibeli : "))
        isntAddToCart = (cart["stock"] + stock) > product["stock"]
        if isntAddToCart: print("Mohon maaf, jumlah stok yang di input melebihi jumlah stock yang ada di toko.")

    if isCartExist(product["sku"]):
        cart["stock"] += stock
        cart["price"] = cart["stock"] * product["price"]
        cartIndex = GetIndexByCartId(cart["sku"])
        PutCartByIdx(cartIndex, cart)
    else:
        product["stock"] = stock
        product["price"] = stock * product["price"]
        PostCart(product)
    print("\nKeranjang anda sekarang :")
    printAllCarts()
    isBeli = input(f"\n\nIngin beli lagi? (y / t) : ").lower()
    if isBeli == "y":
        PostBuyProductController()
