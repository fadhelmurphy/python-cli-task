from models.product import list_product, schema_product
from helpers import toRupiah, requiredInput, findItemInListObj, changeItemInListObj, changeItemByCond

def GetProducts():
    return list_product

def GetProductById(value):
    value = value.lower()
    try:
        return findItemInListObj(lambda product: (value in product["sku"].lower() or value in product["product_name"].lower()), list_product)
    except:
        return []
    
def GetIndexByProductId():
    isNotFound = True
    index = 0
    try:
        while isNotFound:
            value = input(f"\n\nMasukkan sku yang ingin diubah : ").lower()
            selectedProduct = findItemInListObj(lambda product: (value in product[1]["sku"].lower()), enumerate(list_product))
            isNotFound = len(selectedProduct) == 0
            if isNotFound: print("Sku tidak ditemukan, silakan coba yang lain")
            else:
                index = selectedProduct[0][0]
        return index
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
    list_product.append(payload)

def printAllProduct(withIndex=False):
    products = GetProducts()
    showlist_product(products, withIndex)
    return products

# def changeProductQty(key, val, condKey, condVal):
#     return changeItemInListObj(lambda item: changeItemByCond(item, key, val, item[condKey].lower() == condVal.lower()), list_product)

def changeProductQty(val, condVal):
    return changeItemInListObj(lambda item: changeItemByCond(item, "stock", val, item["sku"].lower() == condVal.lower() and item["stock"] >= val), list_product)

def create_product():
    product = {}
    for item, options in schema_product.items():
        data_type, unique, nullable = options.values()
        if "list" in str(data_type):
            val = input(f"Masukkan {item} pisahkan dengan , jika lebih dari 1.\ncontoh: fragrance, sunscreen : ")
            product[item] = data_type(val.split(","))
        elif unique and nullable != True:
            isValid = True
            while isValid:
                val = requiredInput(f"Masukkan {item} : ", data_type)
                isValid = isProductExist(val)
                if isValid == True:
                    print("Data yang anda input sudah ada, silakan input yang lain.")
            product[item] = val
        elif nullable != True:
            val = requiredInput(f"Masukkan {item} : ", data_type)
            product[item] = val
        elif nullable:
            val = data_type(input(f"Masukkan {item} : "))
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
        categoryTab = "\t"*2 if len(category) >= 6 else "\t"*3
        print(f"{index}{sku}\t| {product_name}{productTab}| {brand_name}{brandTab}| {' '.join(category)}{categoryTab}| {toRupiah(price)}\t| {stock} ".title())

def showProductDetail(item):
    print(f"sku\t\t| product name\t\t\t| brand name\t| category\t\t\t| price\t\t| stock ")
    sku, product_name, brand_name, category, price, stock = item.values()
    print(f"{sku}\t| {product_name}\t\t\t| {brand_name}\t\t| {' '.join(category)}\t\t\t| {price}\t| {stock} ")