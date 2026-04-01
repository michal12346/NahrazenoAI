# Simulátor dopravy ve městě - VERZE 1

celkem_aut = 0
pokracovat = "ano"

# SMYČKA: Hlavní cyklus programu, který se opakuje, dokud uživatel zadává "ano"
while pokracovat == "ano":
    pocet_aut = int(input("Kolik aut právě projelo křižovatkou? "))
    
    celkem_aut = celkem_aut + pocet_aut
    print("Celkem už projelo:", celkem_aut, "aut.")
    
    pokracovat = input("Chceš zadat další měření? (ano/ne): ")

print("Simulace byla ukončena.")