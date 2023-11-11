from models.product import list_product, schema_product
from helpers import toRupiah, requiredInput, findItemInListObj, changeItemInListObj, changeItemByCond

def GetProducts():
    return list_product

def GetProductById(value):
    value = value.lower()
    try:
        return findItemInListObj(lambda product: (value in product["sku"].lower()), list_product)
    except:
        return []
    
def GetIndexByProductId(breakIfNotFound):
    isNotFound = True
    index = -1
    try:
        while isNotFound:
            value = input(f"\n\nMasukkan sku : ").lower()
            selectedProduct = findItemInListObj(lambda product: (value == product[1]["sku"].lower()), enumerate(list_product))
            isNotFound = len(selectedProduct) == 0
            if isNotFound: 
                print("The data that you are looking for doesn't exist, Try another sku.")
                if breakIfNotFound:
                    break
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
                    print("Data already exists, try another input.")
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
        productTab = "\t"*3 if len(product_name) < 14 else "\t"*2 if len(product_name) < 24 else "\t"*1
        brandTab = "\t"*2 if len(brand_name) >= 6 else "\t"*3
        strCat = ','.join(category)
        categoryTab = "\t"*3 if len(strCat) < 14 else "\t"*2 if len(strCat) < 24 else "\t"*1
        print(f"{index}{sku}\t| {product_name}{productTab}| {brand_name}{brandTab}| {strCat}{categoryTab}| {toRupiah(price)}\t| {stock} ".title())

def showProductDetail(item):
    print(f"\n\nsku\t\t| product name\t\t\t| brand name\t\t| category\t\t\t| price\t\t| stock ".title())
    sku, product_name, brand_name, category, price, stock = item.values()
    productTab = "\t"*3 if len(product_name) < 14 else "\t"*2 if len(product_name) < 24 else "\t"*1
    brandTab = "\t"*2 if len(brand_name) >= 6 else "\t"*3
    strCat = ','.join(category)
    categoryTab = "\t"*3 if len(strCat) < 14 else "\t"*2 if len(strCat) < 24 else "\t"*1
    print(f"{sku}\t| {product_name}{productTab}| {brand_name}{brandTab}| {strCat}{categoryTab}| {toRupiah(price)}\t| {stock} ".title())