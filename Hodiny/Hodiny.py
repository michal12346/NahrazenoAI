# Hodiny - FINÁLNÍ VERZE

# Importujeme 'time' pro čas a 'os' pro interakci s operačním systémem
import time
import os

# Funkce, která řeší problém s vypisováním času pod sebe
def vymaz_obrazovku():
    # Podmínka zjišťuje, jaký má uživatel operační systém
    # 'nt' znamená Windows, cokoliv jiného je většinou Mac nebo Linux
    if os.name == 'nt':
        os.system('cls')   # Příkaz pro smazání konzole ve Windows
    else:
        os.system('clear') # Příkaz pro smazání konzole na Mac/Linux

# Hlavní funkce programu, která sdružuje celou logiku hodin
def spust_hodiny():
    # Naše nekonečná smyčka pro běh hodin
    while True:
        # 1. Nejdřív zavoláme naši funkci a smažeme starý text na obrazovce
        vymaz_obrazovku()
        
        # 2. Získáme nový aktuální čas
        aktualni_cas = time.strftime("%H:%M:%S")
        
        # 3. Hezky ho vypíšeme s rámečkem
        print("====================")
        print(f" Aktuální čas: {aktualni_cas}")
        print("====================")
        
        # 4. Počkáme 1 vteřinu, než se smyčka zopakuje a znovu vše smaže
        time.sleep(1)

# Samotné spuštění hlavní funkce (bez tohoto řádku by program nic neudělal)
spust_hodiny()
