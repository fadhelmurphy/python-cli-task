import app

separator = "="*41

def bottomInfo(): 
    displayBack = "[9] : tekan 9 dan enter untuk kembali.\n" if len(app.currentRoutes) > 1 else ""
    print(f"\n\n{displayBack}[0] : tekan 0 dan enter untuk keluar dari program\n")

def showProductList(products, withIndex = False):
    index = f"Index\t\t| " if withIndex else ""
    print("\n")
    print(f"{index}sku\t\t| product name\t\t\t| brand name\t\t| category\t\t\t| price\t\t| stock ".title())
    for idx, item in enumerate(products):
        index = f"{idx}\t\t| " if withIndex else ""
        sku, product_name, brand_name, category, price, stock = item.values()
        productTab = "\t"*2 if len(product_name) >= 14 else "\t"*3
        brandTab = "\t"*2 if len(brand_name) >= 6 else "\t"*3
        print(f"{index}{sku}\t| {product_name}{productTab}| {brand_name}{brandTab}| {' '.join(category)}\t\t\t| {price}\t| {stock} ".title())

def showProductDetail(item):
    print(f"sku\t\t| product name\t\t\t| brand name\t| category\t\t\t| price\t\t| stock ")
    sku, product_name, brand_name, category, price, stock = item.values()
    print(f"{sku}\t| {product_name}\t\t\t| {brand_name}\t\t| {' '.join(category)}\t\t\t| {price}\t| {stock} ")