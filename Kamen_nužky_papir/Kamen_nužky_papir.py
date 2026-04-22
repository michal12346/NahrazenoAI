#kamen nužky papír - PRVNÍ VERZE

import random # Importujeme knihovnu pro generování náhodných hodnot (volba počítače)

# Datová struktura (seznam) obsahující povolené tahy
moznosti = ["kámen", "nůžky", "papír"]

# Získání vstupu od hráče. Funkce lower() převede text na malá písmena, aby se předešlo chybám.
hrac = input("Vyber si: kámen, nůžky, nebo papír: ").lower()

# Počítač náhodně vybere jednu položku ze seznamu možností
pocitac = random.choice(moznosti)

# Výpis toho, co kdo vybral
print(f"Hráč vybral: {hrac}")
print(f"Počítač vybral: {pocitac}")
