from services.productServices import GetProducts, GetProductById, GetSortedProductsByParams

def AllProductsController(): 
    print(GetProducts())
    isSorted = input("Mau di sort? (y/t) : ")
    if isSorted.lower() == "y":
        sortedBy = input("Sorted by:")
        print(GetSortedProductsByParams(sortedBy))

def ProductByIdController():
    sku = input("Masukkan sku:")
    print(GetProductById(sku))
