#kamen nužky papír - FINÁLNÍ VERZE

import random # Importujeme knihovnu pro generování náhodných hodnot (volba počítače)

moznosti = ["kámen", "nůžky", "papír"]

# Hlavní herní smyčka. 'while True' znamená, že poběží do nekonečna, 
# dokud ji ručně nezastavíme příkazem 'break'.
while True:
    hrac = input("Vyber si (kámen, nůžky, papír) nebo napiš 'konec': ").lower()

    # Podmínka pro ukončení programu.
    if hrac == "konec":
        print("Díky za hru!")
        break # Přeruší smyčku a ukončí program

    # Kontrola platnosti vstupu. Pokud hráč napsal nesmysl, smyčka se restartuje.
    if hrac not in moznosti:
        print("Neplatný tah. Zkus to znovu.")
        continue # Přeskočí zbytek kódu a vrátí se na začátek smyčky (k zadání vstupu)

    pocitac = random.choice(moznosti)

    print(f"Hráč vybral: {hrac} | Počítač vybral: {pocitac}")

    # Optimalizovaná logika vyhodnocení (sloučení podmínek výhry pomocí 'or')
    if hrac == pocitac:
        print("-> Je to remíza!\n")
    elif (hrac == "kámen" and pocitac == "nůžky") or \
         (hrac == "nůžky" and pocitac == "papír") or \
         (hrac == "papír" and pocitac == "kámen"):
        print("-> Vyhrál jsi!\n")
    else:
        print("-> Počítač vyhrál!\n")
