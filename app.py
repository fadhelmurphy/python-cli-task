from routes import menu
from helpers import bottomInfo, separator

currentRoutes = [1]
last_menu_removed = False

def backToMainMenu():
    global currentRoutes, last_menu_removed
    currentRoutes = [1]
    last_menu_removed = True

def backToPrevMenu(): 
    global last_menu_removed
    currentRoutes.pop()
    last_menu_removed = True

def start():

    global last_menu_removed
    user_input = 1
    while user_input != 0:

        get_menu = "_".join(map(str, currentRoutes))
        if menu.get(get_menu):
            last_menu_removed = False
            if isinstance(menu[get_menu], str): print(menu[get_menu])
            elif callable(menu[get_menu]):menu[get_menu]()
        else: 
            print("Menu tidak ada...")
            backToPrevMenu()

        if last_menu_removed == False:
            bottomInfo()
            user_input = int(input("Masukkan angka menu: "))
            if len(currentRoutes) == 1 and user_input == 9: continue
            if user_input == 9:
                backToPrevMenu()
            else:
                currentRoutes.append(user_input)
    print(f"{separator}\nGood Bye, Thank for using this app\n{separator}")