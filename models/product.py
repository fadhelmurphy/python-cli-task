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

schema_product =     {
    "sku": str,
    "product_name": str,
    "brand_name": str,
    "category": list,
    "price": int,
    "stock": int
}