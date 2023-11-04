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

def GetProductById(sku):
    try:
        return list(filter(lambda product: product["sku"].lower() == sku.lower(), list_product))[0]
    except:
        return []

def GetSortedProductsByParams(params):
    return sorted(list_product, key=lambda d: d[params]) 