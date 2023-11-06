from models.cart import list_cart
from helpers import findItemInListObj
from services.productServices import showlist_product, changeProductQty, GetProductById, changeItemByCond, changeItemInListObj

def GetCarts():
    return list_cart

def PostCart(payload):
    list_cart.append(payload)

def GetCartById(value):
    value = value.lower()
    try:
        return findItemInListObj(lambda product: (value.lower() in product["sku"].lower()), list_cart)
    except:
        return []
    
isCartExist = lambda sku: len(GetCartById(sku)) > 0

def GetIndexByCartId(sku):
    index = -1
    selectedCart = findItemInListObj(lambda product: (sku.lower() == product[1]["sku"].lower()), enumerate(list_cart))
    isNotFound = len(selectedCart) == 0
    if isNotFound: print("Sku tidak ditemukan, silakan coba yang lain")
    else:
        index = selectedCart[0][0]
    return index

def PutCartByIdx(index, payload):
    list_cart[index] = payload

def DeleteCartByIdx(index):
    try:
        del list_cart[index]
    except:
        print("\nMaaf index yang kamu masukkan tidak ada dalam table\n")

def changeCartQty(val, condVal):
    return changeItemInListObj(lambda item: changeItemByCond(item, "stock", val, item["sku"].lower() == condVal.lower() and item["stock"] >= val), list_cart)

def PostCartsCheckout():
    global list_product
    carts = GetCarts()
    for item in carts:
        sku, product_name, _, _, _, stock = item.values()
        products = GetProductById(sku).copy()[0].copy()
        if products["stock"] >= stock:
            list_product = changeProductQty(val=stock, condVal=sku)
        else: print(f"Jumlah {product_name} melebihi stok yang ada di toko.")

def printAllCarts(withIndex=False):
    carts = GetCarts()
    if len(carts) > 0: showlist_product(carts, withIndex)
    else: print("Keranjang anda kosong")
    return carts
