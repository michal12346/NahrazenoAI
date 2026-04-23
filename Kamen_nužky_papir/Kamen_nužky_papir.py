#kamen nužky papír - DRUHÁ VERZE

import random # Importujeme knihovnu pro generování náhodných hodnot (volba počítače)

moznosti = ["kámen", "nůžky", "papír"]
hrac = input("Vyber si: kámen, nůžky, nebo papír: ").lower()
pocitac = random.choice(moznosti)

print(f"Hráč vybral: {hrac}")
print(f"Počítač vybral: {pocitac}")

# Logická část pro vyhodnocení vítěze pomocí série podmínek if-elif-else
if hrac == pocitac:
    # Pokud se volby shodují, je to remíza
    print("Je to remíza!")
elif hrac == "kámen" and pocitac == "nůžky":
    print("Vyhrál jsi!")
elif hrac == "nůžky" and pocitac == "papír":
    print("Vyhrál jsi!")
elif hrac == "papír" and pocitac == "kámen":
    print("Vyhrál jsi!")
else:
    # Pokud nenastala remíza a neplatí žádná z podmínek pro výhru hráče, 
    # logicky z toho vyplývá výhra počítače.
    print("Počítač vyhrál!")
