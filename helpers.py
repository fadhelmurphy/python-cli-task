import app

separator = "="*41

def bottomInfo(): 
    displayBack = "[9] : tekan 9 dan enter untuk kembali.\n" if len(app.currentRoutes) > 1 else ""
    print(f"\n\n{displayBack}[0] : tekan 0 dan enter untuk keluar dari program\n")

def showProductList(products):
    print(f"sku\t\t| product name\t\t\t| brand name\t| category\t\t\t| price\t\t| stock ")
    for item in products:
        sku, product_name, brand_name, category, price, stock = item.values()
        print(f"{sku}\t| {product_name}\t\t\t| {brand_name}\t\t| {' '.join(category)}\t\t\t| {price}\t| {stock} ")

def showProductDetail(item):
    print(f"sku\t\t| product name\t\t\t| brand name\t| category\t\t\t| price\t\t| stock ")
    sku, product_name, brand_name, category, price, stock = item.values()
    print(f"{sku}\t| {product_name}\t\t\t| {brand_name}\t\t| {' '.join(category)}\t\t\t| {price}\t| {stock} ")