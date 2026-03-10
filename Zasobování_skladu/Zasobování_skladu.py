# Simulátor skladu - 1 VERZE
# Základní pohyb zboží

sklad_nazev = "Elektronika"
aktualni_zasoby = 100
minimalni_limit = 20

print(f"--- VITEJTE V SYSTEMU SKLADU: {sklad_nazev} ---")

# Hlavní smyčka simulace
pokracovat = "ano"
while pokracovat == "ano":
    print(f"\nAktuální stav: {aktualni_zasoby} ks")
    
    # Zadávání pohybu zboží
    vydano = int(input("Kolik kusů se dnes prodalo: "))
    prijato = int(input("Kolik kusů přivezli z továrny: "))
    
    # Logika aktualizace stavu
    # Přičteme nové zboží a odečteme prodané
    aktualni_zasoby = aktualni_zasoby + prijato - vydano
    
    # Kontrola kritického stavu
    if aktualni_zasoby < 0:
        print("!!! CHYBA: Sklad nemůže jít do záporu. Resetuji na 0.")
        aktualni_zasoby = 0
    elif aktualni_zasoby <= minimalni_limit:
        print(f"!!! VAROVÁNÍ: Stav klesl pod limit {minimalni_limit} ks! Objednejte zboží.")
    else:
        print("Stav zásob je v normě.")

    pokracovat = input("Chceš pokračovat dalším dnem? (ano/ne): ")

print("Systém vypnut.")