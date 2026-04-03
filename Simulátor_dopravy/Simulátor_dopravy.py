# Simulátor dopravy ve městě - FINÁLNÍ VERZE
celkem_aut = 0
celkem_autobusu = 0
pocet_mereni = 0 

print("Vítejte v Simulátoru městské dopravy!")

# SMYČKA: Nekonečný cyklus, přeruší se až příkazem 'break'
while True:
    pocet_aut = int(input("Kolik aut právě projelo? "))
    pocet_autobusu = int(input("Kolik autobusů právě projelo? "))
    
    celkem_aut = celkem_aut + pocet_aut
    celkem_autobusu = celkem_autobusu + pocet_autobusu
    pocet_mereni = pocet_mereni + 1  
    
    zatizeni = pocet_aut + (pocet_autobusu * 3)
    
    if zatizeni > 20:
        print("POZOR: Tvoří se dopravní zácpa!")
    else:
        print("Doprava je plynulá.")
        
    odpoved = input("Chceš pokračovat? (napiš 'konec' pro zastavení, nebo cokoliv pro pokračování): ")
    # LOGIKA: Ukončení smyčky, pokud uživatel zadá klíčové slovo
    if odpoved == "konec":
        break  

print("\n--- KONEČNÉ STATISTIKY ---")
print("Celkem aut:", celkem_aut)
print("Celkem autobusů:", celkem_autobusu)

# LOGIKA: Ochrana proti chybě dělení nulou, pokud by uživatel ukončil program hned
if pocet_mereni > 0:
    prumer = celkem_aut / pocet_mereni
    print("Průměrně projelo", prumer, "aut během jednoho měření.")
