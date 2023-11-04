from routes import menu
from helpers import bottomInfo, separator

currentRoutes = [1]

def start():

    user_input = 1
    last_menu_removed = False
    while user_input != 0:

        get_menu = "_".join(map(str, currentRoutes))
        if menu.get(get_menu):
            if isinstance(menu[get_menu], str): print(menu[get_menu])
            elif callable(menu[get_menu]):menu[get_menu]()
            last_menu_removed = False
        else: 
            print("Menu tidak ada...")
            currentRoutes.pop()
            last_menu_removed = True

        if last_menu_removed == False:
            bottomInfo()
            user_input = int(input("Masukkan angka menu: "))
            if len(currentRoutes) == 1 and user_input == 9: continue
            if user_input == 9:
                currentRoutes.pop()
            else:
                currentRoutes.append(user_input)
    print(f"{separator}\nGood Bye, Thank for using this app\n{separator}")