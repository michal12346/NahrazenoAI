# Kviz - ŠESNÁCTÁ VERZE

# Importujeme modul 'random' pro náhodné míchání seznamů (otázek a možností).
import random
# Importujeme modul 'time' pro práci se stopkami u časových otázek.
import time

# Vytvoříme hlavní funkci programu. Kód uvnitř čeká, až ho na konci zavoláme.
def spustit_kviz():
    # Do proměnné 'otazky' uložíme velký seznam (v hranatých závorkách []).
    # Každá položka je slovník (ve složených závorkách {}), který nese data o jedné otázce.
    otazky = [
        # Kategorie 1: Geografie
        {"text": "Jaké je hlavní město ČR?", "moznosti": ["Praha", "Brno", "Ostrava"], "spravne": "Praha", "typ": "volba", "kategorie": "1"},
        {"text": "Jaká je nejvyšší hora České republiky?", "moznosti": ["Praděd", "Sněžka", "Lysá hora"], "spravne": "Sněžka", "typ": "volba", "kategorie": "1"},
        {"text": "Napiš hlavní město Francie:", "spravne": "Paříž", "typ": "otevrena", "kategorie": "1"},
        {"text": "Jak se jmenuje nejdelší řeka světa?", "spravne": "Amazonka", "typ": "otevrena", "kategorie": "1"},
        {"text": "Kolik kontinentů je tradičně na Zemi?", "moznosti": ["5", "6", "7"], "spravne": "7", "typ": "volba", "kategorie": "1"},

        # Kategorie 2: Věda a technika
        {"text": "Kolik je 5 + 5?", "moznosti": ["10", "12", "8"], "spravne": "10", "typ": "volba", "kategorie": "2"},
        {"text": "Která planeta je nejblíže Slunci?", "moznosti": ["Venuše", "Merkur", "Země"], "spravne": "Merkur", "typ": "volba", "kategorie": "2"},
        {"text": "Jaký chemický prvek má značku O?", "moznosti": ["Zlato", "Kyslík", "Olovo"], "spravne": "Kyslík", "typ": "volba", "kategorie": "2"},
        {"text": "Který savec umí jako jediný aktivně létat?", "spravne": "netopýr", "typ": "otevrena", "kategorie": "2"},
        {"text": "Který programovací jazyk používáme pro tento kvíz?", "moznosti": ["Java", "Python", "C++"], "spravne": "Python", "typ": "volba", "kategorie": "2"},

        # Kategorie 3: Rychlovky
        {"text": "RYCHLOVKA: Kolik je 7 * 8?", "spravne": "56", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Jaká je chemická značka vody?", "spravne": "H2O", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Jaké je hlavní město Slovenska?", "spravne": "Bratislava", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Kolik minut má jedna hodina?", "spravne": "60", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Napiš zkratku České republiky:", "spravne": "ČR", "typ": "casovka", "limit": 10, "kategorie": "3"}
    ]

    # Vytiskneme uvítací nápis na obrazovku.
    print("=== VÍTEJ V PARÁDNÍM MULTI-KVÍZU ===")
    # Zeptáme se uživatele na jméno, odstraníme zbytečné mezery na krajích (.strip()) a uložíme ho.
    jmeno_hrace = input("Zadej své jméno: ").strip()
    
    # --- NAČTENÍ HISTORICKÉHO REKORDU ZE SOUBORU ---
    # Blok 'try' zkusí provést nebezpečný kód, který by mohl vyhodit chybu (např. když soubor neexistuje).
    try:
        # Otevřeme soubor "rekord.txt" v režimu čtení ("r"). 'encoding' zajišťuje správné čtení češtiny na Windows.
        with open("rekord.txt", "r", encoding="utf-8") as soubor:
            # Přečteme text ze souboru, převedeme ho na celé číslo (int) a uložíme do 'osobni_rekord'.
            osobni_rekord = int(soubor.read())
            # Informujeme hráče, že se rekord úspěšně načetl.
            print(f"> Načten tvůj historický rekord ze souboru: {osobni_rekord} bodů!")
    # 'except' zachytí konkrétní chybu: "Soubor nebyl nalezen" (hraje se úplně poprvé na tomto PC).
    except FileNotFoundError:
        # Soubor neexistuje, takže nastavíme rekord manuálně na nulu, aby měl program s čím pracovat.
        osobni_rekord = 0
        # Uklidníme hráče, že se nic neděje a začíná s čistým štítem.
        print("> Zatím nemáš uložený žádný rekord. Čas ho vytvořit!")

    # Startujeme nekonečný cyklus, který drží hru spuštěnou, dokud ji sami neukončíme.
    while True:
        # Vypíšeme menu s nabídkou kategorií.
        print("\nVyber si téma kvízu:")
        print("1) Geografie")
        print("2) Věda a technika")
        print("3) Rychlovky")
        
        # Počkáme, až hráč zadá číslo, ořízneme mezery a uložíme volbu.
        volba_kategorie = input("Zadej číslo kategorie (1/2/3): ").strip()
        # Zkontrolujeme, jestli hráč nezadal neplatný znak (např. '4' nebo 'A').
        if volba_kategorie not in ["1", "2", "3"]:
            # Pokud zadal nesmysl, upozorníme ho.
            print("Neplatná volba! Zkus to znovu.")
            # Příkaz 'continue' přeskočí zbytek kódu a vrátí smyčku 'while' zase úplně na začátek (zobrazí menu).
            continue
            
        # Připravíme si prázdný seznam pro otázky, které odpovídají vybrané kategorii.
        aktivni_otazky = []
        # Cyklem 'for' projdeme úplně všechny otázky z naší velké databáze nahoře.
        for o in otazky:
            # Pokud se číslo kategorie u otázky shoduje s volbou hráče...
            if o["kategorie"] == volba_kategorie:
                # ...přidáme tuto otázku do našeho nového seznamu aktivních otázek.
                aktivni_otazky.append(o)

        # Nový seznam vyfiltrovaných otázek náhodně zamícháme, aby nebyly vždy ve stejném pořadí.
        random.shuffle(aktivni_otazky)
        # Vynulujeme skóre pro aktuální kolo.
        skore = 0
        # Hráč dostane do začátku každého kola 3 životy.
        zivoty = 3
        
        # Začínáme postupně vytahovat jednu vyfiltrovanou otázku za druhou.
        for otazka in aktivni_otazky:
            # Vytiskneme oddělovací čáru pro lepší přehlednost v konzoli.
            print("-" * 30)
            # Vytiskneme ikonku srdíčka tolikrát, kolik má hráč aktuálně životů.
            print(f"Tvůj stav: {'❤️ ' * zivoty}")
            # Vytiskneme samotný text otázky.
            print(otazka["text"])
            
            # Zkontrolujeme, jestli se jedná o časovou otázku.
            if otazka["typ"] == "casovka":
                # Upozorníme hráče na časový limit načtený z databáze.
                print(f"!!! POZOR, máš jen {otazka['limit']} sekund !!!")
                # Zaznamenáme si přesný čas těsně předtím, než hráč začne psát.
                start_cas = time.time()
                # Požádáme hráče o odpověď a počkáme, dokud nezmáčkne Enter.
                odpoved = input("Tvoje odpověď: ")
                # Okamžitě po stisku Enter zaznamenáme nový čas.
                konec_cas = time.time()
                # Zjistíme, jak dlouho mu to trvalo (odečtením startovního času od konečného).
                uplynuly_cas = konec_cas - start_cas
                
                # Pokud čas překročil povolený limit...
                if uplynuly_cas > otazka["limit"]:
                    # Vypíšeme, že čas vypršel a zaokrouhlíme uplynulý čas na 1 desetinné místo (pomocí :.1f).
                    print(f">>> Čas vypršel! Trvalo ti to {uplynuly_cas:.1f} s.")
                    # Prozradíme správnou odpověď.
                    print(f">>> Správně bylo: {otazka['spravne']}")
                    # Odebereme hráči jeden život jako trest za pomalost.
                    zivoty -= 1
                # Pokud ale odpověděl včas...
                else:
                    # Připravíme si správnou odpověď pro finální kontrolu (samotná kontrola proběhne až níže).
                    kontrola_spravnosti = otazka["spravne"]
            
            # Pokud se jedná o otázku s možností výběru (a, b, c)...
            elif otazka["typ"] == "volba":
                # Vytvoříme si kopii seznamu možností (abychom nemíchali a neničili originální data v databázi).
                aktualni_moznosti = otazka["moznosti"].copy()
                # Náhodně zkopírované možnosti zamícháme.
                random.shuffle(aktualni_moznosti)
                # Připravíme si seznam písmen, která budeme možnostem na obrazovce přiřazovat.
                pismena = ["a", "b", "c"]
                # Do této proměnné si za chvíli uložíme písmeno, které zrovna připadlo na správnou odpověď.
                pismeno_spravne_odpovedi = ""
                
                # Pomocí funkce 'enumerate' získáme zároveň index (0, 1, 2) i samotný text možnosti z listu.
                for index, moznost in enumerate(aktualni_moznosti):
                    # Vytáhneme si příslušné písmeno ('a' pro index 0, 'b' pro index 1, atd.).
                    pismenko = pismena[index]
                    # Vytiskneme na obrazovku např. "a) Praha".
                    print(f"{pismenko}) {moznost}")
                    # Pokud je tato zrovna vypisovaná možnost ta správná podle databáze...
                    if moznost == otazka["spravne"]:
                        # ...zapamatujeme si, jaké písmeno dostala.
                        pismeno_spravne_odpovedi = pismenko
                
                # Požádáme hráče o volbu písmene, převedeme ho na malá písmena a odstraníme mezery.
                odpoved = input("Tvoje volba (a/b/c): ").lower().strip()
                # Do proměnné pro finální kontrolu nastavíme to správné písmeno zjištěné výše.
                kontrola_spravnosti = pismeno_spravne_odpovedi
                
            # Pokud se nejedná o časovku ani volbu, zbývá už jen otevřená otázka...
            else:
                # Požádáme hráče o přímé zapsání textové odpovědi.
                odpoved = input("Tvoje odpověď: ")
                # Kontrolovat budeme přímo přesný text z databáze.
                kontrola_spravnosti = otazka["spravne"]

            # --- FINÁLNÍ VYHODNOCENÍ ODPOVĚDI ---
            # Tento blok se spustí pro všechny normální otázky a pro ty časovky, KDE HRÁČ STIHNE LIMIT.
            # Tedy: "Pokud to NENÍ časovka, NEBO pokud to JE časovka a hráč se vešel do limitu".
            if otazka["typ"] != "casovka" or (otazka["typ"] == "casovka" and uplynuly_cas <= otazka["limit"]):
                # Porovnáme odpověď hráče s tou správnou (obě převedené na malá písmena bez mezer).
                if odpoved.lower().strip() == kontrola_spravnosti.lower().strip():
                    # Pokud se shodují, pochválíme ho.
                    print(">>> Správně!")
                    # Přidáme mu 1 bod ke skóre v tomto kole.
                    skore += 1
                # Pokud odpověděl špatně...
                else:
                    # Pokud šlo o výběrovou otázku, vypíšeme mu písmeno i text správné odpovědi.
                    if otazka["typ"] == "volba":
                        print(f">>> Špatně! Správná volba byla: {kontrola_spravnosti}) {otazka['spravne']}")
                    # U ostatních typů vypíšeme jen text.
                    else:
                        print(f">>> Špatně! Správně bylo: {otazka['spravne']}")
                    # Jelikož se spletl, odebereme mu jeden život.
                    zivoty -= 1
            
            # Po vyhodnocení každé otázky zkontrolujeme, jestli hráč nepadl na 0 (nebo méně) životů.
            if zivoty <= 0:
                # Pokud ano, vypíšeme lebky a hlášku.
                print("\n" + "💀" * 15)
                print("   GAME OVER! DOŠLY TI ŽIVOTY.")
                print("💀" * 15)
                # Příkaz 'break' okamžitě přeruší probíhající cyklus 'for' s otázkami. Hráč tak už nedostane další.
                break
        
        # --- KONEC CELÉHO KOLA ---
        # Zjistíme, jestli aktuální skóre z této hry překonalo dosavadní historický rekord.
        if skore > osobni_rekord:
            # Pokud ano, přepíšeme proměnnou novou hodnotou.
            osobni_rekord = skore
            # Pogratulujeme k rekordu.
            print("\n*** NOVÝ HISTORICKÝ REKORD! ***")
            
            # --- ZÁPIS REKORDU DO SOUBORU ---
            # Otevřeme soubor "rekord.txt" v režimu "w" (write), což přemaže jeho starý obsah novým.
            # (Pokud soubor na disku ještě neexistoval, Python ho tímto příkazem automaticky vytvoří).
            with open("rekord.txt", "w", encoding="utf-8") as soubor:
                # Do textového souboru můžeme zapisovat jen text (string). Proto číslo převedeme pomocí funkce str().
                soubor.write(str(osobni_rekord))
                # Informujeme uživatele, že se číslo uložilo.
                print("> (Rekord byl bezpečně uložen na tvůj disk)")

        # Vytiskneme závěrečné shrnutí právě odehraného kola.
        print("\n" + "=" * 35)
        print(f"Hráč: {jmeno_hrace}") # Jméno hráče.
        print(f"Skóre z této hry: {skore}") # Body získané teď.
        print(f"Tvůj historický rekord: {osobni_rekord}") # Nejlepší nahraný výsledek ze souboru.
        print("=" * 35)

        # Zeptáme se, jestli chce začít úplně nové kolo. Odpověď převedeme na malá písmena bez mezer.
        if input("Chceš hrát znovu? (ano/ne): ").lower().strip() != "ano":
            # Pokud zadal cokoliv jiného než slovo "ano", rozloučíme se.
            print(f"Díky za hru, {jmeno_hrace}! Měj se.")
            # Příkaz 'break' přeruší ten nekonečný hlavní cyklus 'while True', čímž se program úplně ukončí.
            break

# Speciální podmínka Pythonu. Říká: "Spusť kód pod tímto řádkem POUZE v případě, 
# že uživatel spustil tento soubor přímo (tedy přes tlačítko Run nebo z konzole)."
if __name__ == "__main__":
    # Zavoláme naši hlavní funkci, čímž se celý program fyzicky nastartuje.
    spustit_kviz()
