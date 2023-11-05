import app

separator = "="*41


def toRupiah(angka):
    try:
        # Format the integer part with thousands separators
        integer_part = '{:,.0f}'.format(angka)

        # Combine the integer
        formatted_amount = 'Rp ' + integer_part

        return formatted_amount
    except (ValueError, TypeError):
        return "Invalid Input"
    
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
    return val

def findItemInListObj(funcCondition, obj): return list(filter(funcCondition, obj))

def bottomInfo(): 
    displayBack = "[9] : tekan 9 dan enter untuk kembali ke menu.\n" if len(app.currentRoutes) > 1 else ""
    print(f"\n\n{displayBack}[0] : tekan 0 dan enter untuk keluar dari program\n")