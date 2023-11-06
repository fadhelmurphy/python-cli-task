from models.cart import list_cart
from helpers import findItemInListObj
from services.productServices import showlist_product

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


def printAllCarts(withIndex=False):
    carts = GetCarts()
    showlist_product(carts, withIndex)
    return carts