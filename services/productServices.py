list_product = [
    {
        "sku": "FDS-1101",
        "product_name": "MINES Parfume",
        "brand_name": "MINES",
        "category": ["fragrance"],
        "price": 250000,
        "stock": 24
    },
    {
        "sku": "FDS-1102",
        "product_name": "AAA Parfume",
        "brand_name": "MINES",
        "category": ["fragrance"],
        "price": 250000,
        "stock": 24
    }
]
def GetProducts():
    return list_product

def GetProductById(value):
    value = value.lower()
    try:
        return list(filter(lambda product: (value in product["sku"].lower() or value in product["product_name"].lower()), list_product))
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