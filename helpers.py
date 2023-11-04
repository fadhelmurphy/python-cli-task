import app

separator = "="*41


def rupiah_format(angka):
    try:
        # Format the integer part with thousands separators
        integer_part = '{:,.0f}'.format(angka)

        # Combine the integer
        formatted_amount = 'Rp ' + integer_part

        return formatted_amount
    except (ValueError, TypeError):
        return "Invalid Input"

def bottomInfo(): 
    displayBack = "[9] : tekan 9 dan enter untuk kembali.\n" if len(app.currentRoutes) > 1 else ""
    print(f"\n\n{displayBack}[0] : tekan 0 dan enter untuk keluar dari program\n")