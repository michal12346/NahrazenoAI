# Kviz - DESÁTÁ VERZE

# Importujeme vestavěný modul 'random', který nám umožňuje míchat seznamy
import random
# Importujeme vestavěný modul 'time', abychom mohli měřit čas u rychlovek
import time

def spustit_kviz():
    # Definujeme seznam otázek. Možnosti jsou teď jako samostatný seznam textů.
    # U 'spravne' už nepíšeme písmeno 'a' nebo 'b', ale přímo text správné odpovědi.
    otazky = [
        {
            "text": "Jaké je hlavní město ČR?", 
            "moznosti": ["Praha", "Brno", "Ostrava"], 
            "spravne": "Praha", 
            "typ": "volba"
        },
        {
            "text": "RYCHLOVKA: Kolik je 7 * 8?", 
            "spravne": "56", 
            "typ": "casovka", 
            "limit": 10
        },
        {
            "text": "Jak se jmenuje naše galaxie?", 
            "spravne": "Mléčná dráha", 
            "typ": "otevrena"
        }
    ]

    # Spustíme nekonečnou smyčku 'while', která drží hru spuštěnou
    while True:
        # Náhodně promícháme celé pořadí otázek v seznamu
        random.shuffle(otazky)
        # Vytvoříme proměnnou pro počítání bodů v tomto kole a nastavíme ji na 0
        skore = 0
        
        # Cyklus 'for' začne postupně procházet jednu otázku za druhou
        for otazka in otazky:
            print("-" * 30) # Vytiskne oddělovací čáru pro přehlednost
            print(otazka["text"]) # Vytiskne text aktuální otázky
            
            # --- LOGIKA PRO ČASOVÉ OTÁZKY ---
            if otazka["typ"] == "casovka":
                print(f"!!! POZOR, máš jen {otazka['limit']} sekund !!!")
                start_cas = time.time() # Uložíme si čas předtím, než uživatel začne psát
                odpoved = input("Tvoje odpověď: ") # Čekáme na vstup uživatele
                konec_cas = time.time() # Uložíme si čas hned poté, co stiskne Enter
                
                uplynuly_cas = konec_cas - start_cas # Spočítáme rozdíl (jak dlouho to trvalo)
                
                # Pokud čas zadávání překročil stanovený limit
                if uplynuly_cas > otazka["limit"]:
                    print(f">>> Čas vypršel! Trvalo ti to {uplynuly_cas:.1f} s.")
                    print(f">>> Správně bylo: {otazka['spravne']}")
                    continue # Příkaz 'continue' přeskočí zbytek kódu a jde rovnou na další otázku
            
            # --- LOGIKA PRO VÝBĚROVÉ OTÁZKY ---
            elif otazka["typ"] == "volba":
                # Vytvoříme si kopii seznamu možností, abychom je mohli bezpečně zamíchat
                aktualni_moznosti = otazka["moznosti"].copy()
                # Náhodně přeházíme pořadí slov (např. ["Brno", "Ostrava", "Praha"])
                random.shuffle(aktualni_moznosti)
                
                # Definujeme si indexy písmen, která budeme k možnostem přiřazovat
                pismena = ["a", "b", "c"]
                # Proměnná, do které si uložíme, jaké písmeno nakonec dostala správná odpověď
                pismeno_spravne_odpovedi = ""
                
                # Pomocí cyklu projdeme všechny 3 možnosti
                # Funkce 'enumerate' nám dává jak pořadové číslo (index), tak samotný text možnosti
                for index, moznost in enumerate(aktualni_moznosti):
                    pismenko = pismena[index] # Získáme písmeno 'a', 'b' nebo 'c' podle indexu
                    print(f"{pismenko}) {moznost}") # Vytiskneme uživateli např. "a) Brno"
                    
                    # Pokud se text této možnosti shoduje se správnou odpovědí, zapamatujeme si její písmeno
                    if moznost == otazka["spravne"]:
                        pismeno_spravne_odpovedi = pismenko
                
                # Vyžádáme si od uživatele písmeno jeho volby
                odpoved_pismeno = input("Tvoje volba (a/b/c): ").lower().strip()
                # Do univerzální proměnné 'odpoved' dosadíme to písmeno, které uživatel zvolil
                odpoved = odpoved_pismeno
                # Do proměnné pro kontrolu dosadíme správné písmeno, které jsme zjistili v cyklu výše
                kontrola_spravnosti = pismeno_spravne_odpovedi

            # --- LOGIKA PRO OTEVŘENÉ OTÁZKY ---
            else:
                odpoved = input("Tvoje odpověď: ") # Uživatel píše přímo text
                kontrola_spravnosti = otazka["spravne"] # Kontrolovat budeme přímo text z databáze

            # --- UNIVERZÁLNÍ VYHODNOCENÍ ODPOVĚDI ---
            # Převedeme texty na malá písmena (.lower) a smažeme mezery (.strip), aby byla kontrola férová
            if odpoved.lower().strip() == kontrola_spravnosti.lower().strip():
                print(">>> Správně!")
                skore += 1 # Přičteme bod k aktuálnímu skóre
            else:
                # Pokud uživatel odpovídal na výběr, ukážeme mu správné písmeno i text
                if otazka["typ"] == "volba":
                    print(f">>> Špatně! Správná volba byla: {kontrola_spravnosti}) {otazka['spravne']}")
                else:
                    print(f">>> Špatně! Správně bylo: {otazka['spravne']}")
        
        # --- KONEC KOLA ---
        print("\n" + "=" * 25)
        print(f"KVÍZ DOKONČEN! Skóre: {skore} / {len(otazky)}")
        print("=" * 25)

        # Zeptáme se uživatele, zda chce hrát znovu
        if input("Chceš hrát znovu? (ano/ne): ").lower().strip() != "ano":
            print("Nashledanou!")
            break # Ukončíme hlavní while cyklus a program skončí

if __name__ == "__main__":
    spustit_kviz()
