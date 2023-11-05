import app

separator = "="*41


def toRupiah(angka=0):
    integer_part = '{:,.0f}'.format(angka)
    formatted_amount = 'Rp ' + integer_part
    return formatted_amount
    
def requiredInput(placeholder, data_type = str):
    isRequired = True
    val = ""
    while isRequired:
        val = input(placeholder)
        if val != "" : 
            isRequired = False
            if "list" in str(data_type):
                val = data_type(val.split(","))
            else:
                val = data_type(val)
        else: print("Data yang di input masih kosong, silakan coba lagi.")
    return val

def findItemInListObj(funcCondition, obj): return list(filter(funcCondition, obj))

def changeItemInListObj(funcCondition, obj): return list(map(funcCondition, obj))

def changeItemByCond(item, key, value, condition):
    if condition : 
        item[key] -= value
    return item

def bottomInfo(): 
    displayBack = "[9] : tekan 9 dan enter untuk kembali ke menu sebelumnya.\n" if len(app.currentRoutes) > 1 else ""
    print(f"\n\n{displayBack}[0] : tekan 0 dan enter untuk keluar dari program\n")