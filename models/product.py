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
    "sku": {
        "type": str,
        "unique": True,
        "nullable": False
    },
    "product_name": {
        "type": str,
        "unique": False,
        "nullable": True
    },
    "brand_name": {
        "type": str,
        "unique": False,
        "nullable": True
    },
    "category": {
        "type": list,
        "unique": False,
        "nullable": True
    },
    "price": {
        "type": int,
        "unique": False,
        "nullable": True
    },
    "stock": {
        "type": int,
        "unique": False,
        "nullable": True
    }
}