import app

separator = "="*41

def bottomInfo(): 
    displayBack = "[9] : tekan 9 dan enter untuk kembali.\n" if len(app.currentRoutes) > 1 else ""
    print(f"\n\n{displayBack}[0] : tekan 0 dan enter untuk keluar dari program\n")