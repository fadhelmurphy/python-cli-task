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
        "product_name": "Serum Lip Tint",
        "brand_name": "Dear Me",
        "category": ["Make up", "Lip Tint"],
        "price": 89000,
        "stock": 24
    },
    {
        "sku": "FDS-1103",
        "product_name": "Truffle Cleansing Essence",
        "brand_name": "Skintific",
        "category": ["Skin care", "Skintific"],
        "price": 128000,
        "stock": 24
    },
    {
        "sku": "FDS-1104",
        "product_name": "Sunscreen GEL SPF 50+",
        "brand_name": "WHITELAB",
        "category": ["Sun Care"],
        "price": 84300,
        "stock": 24
    },
    {
        "sku": "FDS-1105",
        "product_name": "Supreme Treatment Essence",
        "brand_name": "ESQA",
        "category": ["Skin care"],
        "price": 84300,
        "stock": 24
    },
    {
        "sku": "FDS-1106",
        "product_name": "Xpress Micelar Oil Water",
        "brand_name": "Azarine",
        "category": ["Skin care"],
        "price": 3900,
        "stock": 24
    },
    {
        "sku": "FDS-1107",
        "product_name": "MSH Niacinamide",
        "brand_name": "Skintific",
        "category": ["Skin care", "Moisturizer"],
        "price": 154200,
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