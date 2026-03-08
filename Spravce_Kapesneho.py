# Program na hlidani penez - FINÁLNÍ VERZE
# Pridany komentare k logicky castem

pokracovat = "ano"

# Hlavni smycka - program bezi dokud uzivatel chce zadavat data
# Zaměřeno na logiku cyklu
while pokracovat == "ano":
    print("--- ZADAVANI NOVYCH UDAJU ---")
    nasetreno = float(input("Kolik mas nyni penez: "))
    limit = float(input("Tvuj tydenni limit na utratu: "))
    
    # Načítání hodnot do proměnných
    jidlo = float(input("Utrata za jidlo: "))
    zabava = float(input("Utrata za zabavu: "))
    ostatni = float(input("Ostatni utraty: "))
    
    celkova_utrata = jidlo + zabava + ostatni
    zbytek = nasetreno - celkova_utrata
    
    # Vetveni programu pro kontrolu penez
    if celkova_utrata > limit:
        print("!!! ALERT: Limit prekrocen o", celkova_utrata - limit, "Kc.")
    elif celkova_utrata == limit:
        print("Opatrne, ses presne na limitu.")
    else:
        print("Vsechno v poradku, mas rezervu.")
        
    print("Zbyva ti:", zbytek, "Kc.")
    
    # Dotaz na uzivatele jestli chce cely proces opakovat
    # Pokud napise cokoli jineho nez 'ano', smycka while skonci
    pokracovat = input("Chces zadat nove udaje? (ano/ne): ")

print("Program ukoncen. Mej se hezky!")
