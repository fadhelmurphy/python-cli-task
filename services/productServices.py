from models.product import list_product, schema_product
from helpers import toRupiah, requiredInput, findItemInListObj

def GetProducts():
    return list_product

def GetProductById(value):
    value = value.lower()
    try:
        return findItemInListObj(lambda product: (value in product["sku"].lower() or value in product["product_name"].lower()), list_product)
    except:
        return []

def GetSortedProductsByParams(params, reverse=False):
    global list_product
    list_product = sorted(list_product, key=lambda d: d[params], reverse=reverse) 
    return list_product

def DeleteProductByIdx(index):
    try:
        del list_product[index]
    except:
        print("\nMaaf index yang kamu masukkan tidak ada dalam table\n")

def PutProductByIdx(index, payload):
    list_product[index] = payload

isProductExist = lambda sku: len(GetProductById(sku)) > 0

def PostProduct(payload):
    isExist = isProductExist(payload["sku"])
    if isExist == False:
        list_product.append(payload)
        return True
    else: return False

def printAllProduct(withIndex=False):
    print(showlist_product(GetProducts(), withIndex))
        

def create_product():
    product = {}
    for item, data_type in schema_product.items():
        if "list" in str(data_type):
            val = input(f"Masukkan {item} pisahkan dengan , jika lebih dari 1.\ncontoh: fragrance, parfume : ")
            product[item] = data_type(val.split(","))
        else:
            val = requiredInput(f"Masukkan {item} : ", data_type)
            product[item] = val
    return product

def showlist_product(products, withIndex = False):
    index = f"Index\t\t| " if withIndex else ""
    print("\n")
    print(f"{index}sku\t\t| product name\t\t\t| brand name\t\t| category\t\t\t| price\t\t| stock ".title())
    for idx, item in enumerate(products):
        index = f"{idx}\t\t| " if withIndex else ""
        sku, product_name, brand_name, category, price, stock = item.values()
        productTab = "\t"*2 if len(product_name) >= 14 else "\t"*3
        brandTab = "\t"*2 if len(brand_name) >= 6 else "\t"*3
        print(f"{index}{sku}\t| {product_name}{productTab}| {brand_name}{brandTab}| {' '.join(category)}\t\t\t| {toRupiah(price)}\t| {stock} ".title())

def showProductDetail(item):
    print(f"sku\t\t| product name\t\t\t| brand name\t| category\t\t\t| price\t\t| stock ")
    sku, product_name, brand_name, category, price, stock = item.values()
    print(f"{sku}\t| {product_name}\t\t\t| {brand_name}\t\t| {' '.join(category)}\t\t\t| {price}\t| {stock} ")