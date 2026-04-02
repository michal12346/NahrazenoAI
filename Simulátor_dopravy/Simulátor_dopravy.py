# Simulátor dopravy ve městě - VERZE 2
celkem_aut = 0
celkem_autobusu = 0
pokracovat = "ano"

# SMYČKA: Hlavní cyklus pro průběžné zadávání dat
while pokracovat == "ano":
    pocet_aut = int(input("Kolik aut právě projelo? "))
    pocet_autobusu = int(input("Kolik autobusů právě projelo? "))
    
    celkem_aut = celkem_aut + pocet_aut
    celkem_autobusu = celkem_autobusu + pocet_autobusu
    
    # LOGIKA: Výpočet vytížení křižovatky. 
    # Autobus zabírá více místa, proto se násobí třemi.
    zatizeni = pocet_aut + (pocet_autobusu * 3)
    
    # LOGIKA: Rozhodnutí, zda vzniká zácpa
    if zatizeni > 20:
        print("POZOR: Tvoří se dopravní zácpa!")
    else:
        print("Doprava je plynulá.")
        
    pokracovat = input("Chceš zadat další měření? (ano/ne): ")

print("Konec simulace. Celkem projelo", celkem_aut, "aut a", celkem_autobusu, "autobusů.")
