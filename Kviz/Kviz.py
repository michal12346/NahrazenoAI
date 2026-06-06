# Kviz - DEVATENÁCTÁ VERZE

import random  # Importujeme modul 'random' pro náhodné míchání otázek a možností.
import time  # Importujeme modul 'time' pro měření času u časovek.

def spustit_kviz():  # Definujeme hlavní funkci, do které zabalíme celý kód naší hry.
    otazky = [  # Zakládáme proměnnou 'otazky' jako seznam (list) pomocí hranatých závorek.
        # --- KATEGORIE 1: Geografie (10 otázek) ---  # Popisek pro první kategorii.
        {"text": "Jaké je hlavní město ČR?", "moznosti": ["Praha", "Brno", "Ostrava"], "spravne": "Praha", "typ": "volba", "kategorie": "1"},  # Otázka 1: volba ze 3 možností.
        {"text": "Jaká je nejvyšší hora České republiky?", "moznosti": ["Praděd", "Sněžka", "Lysá hora"], "spravne": "Sněžka", "typ": "volba", "kategorie": "1"},  # Otázka 2: volba.
        {"text": "Napiš hlavní město Francie:", "spravne": "Paříž", "typ": "otevrena", "kategorie": "1"},  # Otázka 3: otevřená otázka, hráč píše text.
        {"text": "Jak se jmenuje nejdelší řeka světa?", "spravne": "Amazonka", "typ": "otevrena", "kategorie": "1"},  # Otázka 4: otevřená otázka.
        {"text": "Kolik kontinentů je tradičně na Zemi?", "moznosti": ["5", "6", "7"], "spravne": "7", "typ": "volba", "kategorie": "1"},  # Otázka 5: volba.
        {"text": "Který oceán je největší na světě?", "moznosti": ["Tichý", "Atlantský", "Indický"], "spravne": "Tichý", "typ": "volba", "kategorie": "1"},  # Otázka 6: volba.
        {"text": "Napiš hlavní město Itálie:", "spravne": "Řím", "typ": "otevrena", "kategorie": "1"},  # Otázka 7: otevřená otázka.
        {"text": "Jaký je nejmenší stát světa?", "moznosti": ["Monako", "Vatikán", "San Marino"], "spravne": "Vatikán", "typ": "volba", "kategorie": "1"},  # Otázka 8: volba.
        {"text": "Na kterém kontinentu leží Egypt?", "moznosti": ["Asie", "Afrika", "Evropa"], "spravne": "Afrika", "typ": "volba", "kategorie": "1"},  # Otázka 9: volba.
        {"text": "Napiš jméno státu, který je naším východním sousedem:", "spravne": "Slovensko", "typ": "otevrena", "kategorie": "1"},  # Otázka 10: otevřená otázka.

        # --- KATEGORIE 2: Věda a technika (10 otázek) ---  # Popisek pro druhou kategorii.
        {"text": "Kolik je 5 + 5?", "moznosti": ["10", "12", "8"], "spravne": "10", "typ": "volba", "kategorie": "2"},  # Otázka 11: matematika, volba.
        {"text": "Která planeta je nejblíže Slunci?", "moznosti": ["Venuše", "Merkur", "Země"], "spravne": "Merkur", "typ": "volba", "kategorie": "2"},  # Otázka 12: vesmír, volba.
        {"text": "Jaký chemický prvek má značku O?", "moznosti": ["Zlato", "Kyslík", "Olovo"], "spravne": "Kyslík", "typ": "volba", "kategorie": "2"},  # Otázka 13: chemie, volba.
        {"text": "Který savec umí jako jediný aktivně létat?", "spravne": "netopýr", "typ": "otevrena", "kategorie": "2"},  # Otázka 14: biologie, otevřená.
        {"text": "Který programovací jazyk používáme pro tento kvíz?", "moznosti": ["Java", "Python", "C++"], "spravne": "Python", "typ": "volba", "kategorie": "2"},  # Otázka 15: IT, volba.
        {"text": "Který orgán pumpuje krev v lidském těle?", "spravne": "srdce", "typ": "otevrena", "kategorie": "2"},  # Otázka 16: biologie, otevřená.
        {"text": "Kolik je 12 * 12?", "moznosti": ["144", "124", "142"], "spravne": "144", "typ": "volba", "kategorie": "2"},  # Otázka 17: matematika, volba.
        {"text": "Jak se jmenuje galaxie, ve které se nachází Země?", "moznosti": ["Andromeda", "Mléčná dráha", "Sombrero"], "spravne": "Mléčná dráha", "typ": "volba", "kategorie": "2"},  # Otázka 18: vesmír, volba.
        {"text": "Napiš chemickou značku pro zlato:", "spravne": "Au", "typ": "otevrena", "kategorie": "2"},  # Otázka 19: chemie, otevřená.
        {"text": "Kdo zformuloval teorii relativity?", "moznosti": ["Isaac Newton", "Albert Einstein", "Nikola Tesla"], "spravne": "Albert Einstein", "typ": "volba", "kategorie": "2"},  # Otázka 20: fyzika, volba.

        # --- KATEGORIE 3: Rychlovky (10 otázek) ---  # Popisek pro třetí kategorii.
        {"text": "RYCHLOVKA: Kolik je 7 * 8?", "spravne": "56", "typ": "casovka", "limit": 10, "kategorie": "3"},  # Otázka 21: časovka s limitem 10s.
        {"text": "RYCHLOVKA: Jaká je chemická značka vody?", "spravne": "H2O", "typ": "casovka", "limit": 10, "kategorie": "3"},  # Otázka 22: časovka.
        {"text": "RYCHLOVKA: Jaké je hlavní město Slovenska?", "spravne": "Bratislava", "typ": "casovka", "limit": 10, "kategorie": "3"},  # Otázka 23: časovka.
        {"text": "RYCHLOVKA: Kolik minut má jedna hodina?", "spravne": "60", "typ": "casovka", "limit": 10, "kategorie": "3"},  # Otázka 24: časovka.
        {"text": "RYCHLOVKA: Napiš zkratku České republiky:", "spravne": "ČR", "typ": "casovka", "limit": 10, "kategorie": "3"},  # Otázka 25: časovka.
        {"text": "RYCHLOVKA: Jaký je výsledek 100 / 4?", "spravne": "25", "typ": "casovka", "limit": 10, "kategorie": "3"},  # Otázka 26: časovka.
        {"text": "RYCHLOVKA: Kolik nohou má pavouk?", "spravne": "8", "typ": "casovka", "limit": 10, "kategorie": "3"},  # Otázka 27: časovka.
        {"text": "RYCHLOVKA: Jaký den v týdnu následuje po pátku?", "spravne": "sobota", "typ": "casovka", "limit": 10, "kategorie": "3"},  # Otázka 28: časovka.
        {"text": "RYCHLOVKA: Napiš oficiální zkratku pro Evropskou unii:", "spravne": "EU", "typ": "casovka", "limit": 10, "kategorie": "3"},  # Otázka 29: časovka.
        {"text": "RYCHLOVKA: Kolik měsíců má jeden kalendářní rok?", "spravne": "12", "typ": "casovka", "limit": 10, "kategorie": "3"}  # Otázka 30: časovka.
    ]  # Konec seznamu otázek.

    print("=== VÍTEJ V PARÁDNÍM MULTI-KVÍZU ===")  # Vypíše úvodní název hry do konzole.
    jmeno_hrace = input("Zadej své jméno: ").strip()  # Zeptá se hráče na jméno a odstraní mezery na začátku a konci.
    
    try:  # Začátek bloku pro odchytávání chyb - zkusíme otevřít soubor.
        with open("rekord.txt", "r", encoding="utf-8") as soubor:  # Otevře soubor rekord.txt v režimu čtení ('r').
            osobni_rekord = int(soubor.read())  # Přečte obsah souboru, převede ho na celé číslo (int) a uloží.
            print(f"> Načten tvůj historický rekord ze souboru: {osobni_rekord} bodů!")  # Vypíše zjištěný rekord hráči.
    except FileNotFoundError:  # Pokud soubor neexistuje, zachytí tuto specifickou chybu.
        osobni_rekord = 0  # Nastaví osobní rekord na 0, protože hráč hraje poprvé.
        print("> Zatím nemáš uložený žádný rekord. Čas ho vytvořit!")  # Informuje hráče, že nemá rekord.

    while True:  # Spustí nekonečnou smyčku, aby hra mohla běžet pořád dokola.
        print("\nVyber si téma kvízu:")  # Vypíše prázdný řádek a nadpis menu.
        print("1) Geografie")  # Vypíše možnost 1.
        print("2) Věda a technika")  # Vypíše možnost 2.
        print("3) Rychlovky")  # Vypíše možnost 3.
        
        volba_kategorie = input("Zadej číslo kategorie (1/2/3): ").strip()  # Načte od hráče jeho volbu a ořízne mezery.
        if volba_kategorie not in ["1", "2", "3"]:  # Zkontroluje, jestli uživatel nezadal nesmysl.
            print("Neplatná volba! Zkus to znovu.")  # Upozorní na špatný vstup.
            continue  # Přeskočí zbytek kódu ve smyčce a vrátí se úplně na začátek menu.
            
        aktivni_otazky = []  # Vytvoří prázdný seznam, do kterého budeme skládat jen otázky vybrané kategorie.
        for o in otazky:  # Začne procházet všechny otázky z velké databáze 'otazky' jednu po druhé.
            if o["kategorie"] == volba_kategorie:  # Pokud se kategorie otázky shoduje s volbou hráče:
                aktivni_otazky.append(o)  # Přidá tuto otázku do seznamu 'aktivni_otazky'.

        random.shuffle(aktivni_otazky)  # Náhodně zamíchá pořadí otázek, aby každá hra byla jiná.
        skore = 0  # Vynuluje skóre na začátku nového kola.
        zivoty = 3  # Nastaví hráči počáteční 3 životy pro toto kolo.
        
        for otazka in aktivni_otazky:  # Začne procházet zamíchané otázky z vybrané kategorie.
            print("-" * 30)  # Vypíše oddělovací čáru z 30 pomlček.
            print(f"Tvůj stav: {'❤️ ' * zivoty}")  # Vypíše aktuální počet srdíček (životů).
            print(otazka["text"])  # Vypíše samotné znění vybrané otázky.
            
            if otazka["typ"] == "casovka":  # Zkontroluje, zda je aktuální otázka typu 'casovka'.
                print(f"!!! POZOR, máš jen {otazka['limit']} sekund !!!")  # Varuje hráče a ukáže mu časový limit.
                start_cas = time.time()  # Uloží si přesný aktuální čas těsně před odpovědí (stopky - start).
                odpoved = input("Tvoje odpověď: ")  # Zobrazí výzvu a čeká, až hráč něco napíše.
                konec_cas = time.time()  # Uloží si přesný aktuální čas hned po odeslání odpovědi (stopky - cíl).
                uplynuly_cas = konec_cas - start_cas  # Odečte start od cíle, čímž získáme reálný čas v sekundách.
                
                if uplynuly_cas > otazka["limit"]:  # Zkontroluje, jestli byl hráč pomalejší než povolený limit.
                    print(f">>> Čas vypršel! Trvalo ti to {uplynuly_cas:.1f} s.")  # Oznámí nestihnutí limitu.
                    print(f">>> Správně bylo: {otazka['spravne']}")  # Ukáže správnou odpověď.
                    zivoty -= 1  # Odebere hráči jeden život jako trest za zdržování.
                else:  # Pokud hráč stihl odpovědět v časovém limitu:
                    kontrola_spravnosti = otazka["spravne"]  # Připraví si správnou odpověď pro pozdější porovnání.
            
            elif otazka["typ"] == "volba":  # Zkontroluje, jestli jde o otázku s možnostmi (a, b, c).
                aktualni_moznosti = otazka["moznosti"].copy()  # Vytvoří kopii možností, abychom nepoškodili originál.
                random.shuffle(aktualni_moznosti)  # Zamíchá pořadí možností (a, b, c budou pokaždé jinak).
                pismena = ["a", "b", "c"]  # Připraví si seznam písmen, která budeme k možnostem přiřazovat.
                pismeno_spravne_odpovedi = ""  # Připraví si prázdnou proměnnou, kam si uložíme správné písmeno.
                
                for index, moznost in enumerate(aktualni_moznosti):  # Prochází zamíchané možnosti i jejich pořadí.
                    pismenko = pismena[index]  # Získá správné písmeno podle indexu (0='a', 1='b', 2='c').
                    print(f"{pismenko}) {moznost}")  # Vypíše možnost na obrazovku i s jejím přiřazeným písmenem.
                    if moznost == otazka["spravne"]:  # Zkontroluje, jestli je zrovna vypisovaná možnost ta správná.
                        pismeno_spravne_odpovedi = pismenko  # Pokud ano, zapamatuje si, jaké písmeno dostala.
                
                odpoved = input("Tvoje volba (a/b/c): ").lower().strip()  # Nechá hráče napsat vstup a upraví ho.
                kontrola_spravnosti = pismeno_spravne_odpovedi  # Řekne programu, jaké písmeno je správné.
                
            else:  # Zbyly už jen 'otevrene' otázky, na které se musí text ručně vypsat.
                odpoved = input("Tvoje odpověď: ")  # Zeptá se hráče přímo na odpověď.
                kontrola_spravnosti = otazka["spravne"]  # Program si připraví text správné odpovědi k porovnání.

            # Tento blok if se spustí vždy kromě případu, kdy vypršel čas u časovky.
            if otazka["typ"] != "casovka" or (otazka["typ"] == "casovka" and uplynuly_cas <= otazka["limit"]):  # Bezpečnostní kontrola času.
                if odpoved.lower().strip() == kontrola_spravnosti.lower().strip():  # Porovná odpověď (ignoruje velikost a mezery).
                    print(">>> Správně!")  # Vypíše pochvalu.
                    skore += 1  # Přičte hráči jeden bod.
                else:  # Pokud hráč odpověděl špatně:
                    if otazka["typ"] == "volba":  # U otázek s volbou:
                        print(f">>> Špatně! Správná volba byla: {kontrola_spravnosti}) {otazka['spravne']}")  # Ukáže správné písmeno i text.
                    else:  # U ostatních otázek:
                        print(f">>> Špatně! Správně bylo: {otazka['spravne']}")  # Zobrazí jen samotný text správné odpovědi.
                    zivoty -= 1  # Odebere hráči jeden život za špatnou odpověď.
            
            if zivoty <= 0:  # Zkontroluje, jestli hráči počet životů neklesl na nulu nebo pod nulu.
                print("\n" + "💀" * 15)  # Vypíše mezeru a 15 lebek.
                print("   GAME OVER! DOŠLY TI ŽIVOTY.")  # Oznámí konec hry.
                print("💀" * 15)  # Vypíše znovu 15 lebek.
                break  # Okamžitě zastaví cyklus s otázkami a ukončí aktuální kolo.
        
        if skore > osobni_rekord:  # Po skončení kola zkontroluje, zda aktuální skóre je větší než historický rekord.
            osobni_rekord = skore  # Pokud ano, přepíše starý rekord na nové aktuální skóre.
            print("\n*** NOVÝ HISTORICKÝ REKORD! ***")  # Pogratuluje hráči k novému rekordu.
            
            with open("rekord.txt", "w", encoding="utf-8") as soubor:  # Otevře soubor rekord.txt v režimu zápisu ('w').
                soubor.write(str(osobni_rekord))  # Zapíše nové číslo rekordu do souboru (převádí číslo na text).
                print("> (Rekord byl bezpečně uložen na tvůj disk)")  # Informuje hráče o uložení.

        print("\n" + "=" * 35)  # Začátek výsledkové tabulky - oddělovací pruh.
        print(f"Hráč: {jmeno_hrace}")  # Vypíše jméno hráče.
        print(f"Skóre z této hry: {skore}")  # Vypíše body z tohoto konkrétního kola.
        print(f"Tvůj historický rekord: {osobni_rekord}")  # Vypíše aktuální historický rekord.
        print("=" * 35)  # Konec výsledkové tabulky.

        if input("Chceš hrát znovu? (ano/ne): ").lower().strip() != "ano":  # Zeptá se na další hru. Pokud není 'ano'...
            print(f"Díky za hru, {jmeno_hrace}! Měj se.")  # Rozloučí se s hráčem jménem.
            break  # Ukončí úplně hlavní nekonečnou smyčku 'while True' a hra se vypne.

if __name__ == "__main__":  # Zkontroluje, zda spouštíme přímo tento soubor.
    spustit_kviz()  # Pokud ano, zavolá hlavní funkci spustit_kviz() a celá hra se nastartuje.
