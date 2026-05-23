# Kviz - DVANÁCTÁ VERZE

# 'import' říká Pythonu, aby si přibral speciální nástroje, které v základu nejsou aktivní.
# Modul 'random' nám dovolí náhodně míchat seznamy (otázky i možnosti a, b, c).
import random
# Modul 'time' nám umožní pracovat se stopkami pro měření času u "rychlovek".
import time

# Vytvoříme hlavní funkci programu. Kód uvnitř se nespustí sám od sebe, 
# dokud tuto funkci na úplném konci programu nezavoláme.
def spustit_kviz():
    
    # Do proměnné 'otazky' uložíme velký Seznam (hranaté závorky []).
    # Každá položka v seznamu je Slovník (složené závorky {}), který obsahuje informace o jedné otázce.
    otazky = [
        # KATEGORIE 1: Geografie
        # Každý slovník má klíče (např. "text", "typ") a k nim přiřazené hodnoty.
        {"text": "Jaké je hlavní město ČR?", "moznosti": ["Praha", "Brno", "Ostrava"], "spravne": "Praha", "typ": "volba", "kategorie": "1"},
        {"text": "Jaká je nejvyšší hora České republiky?", "moznosti": ["Praděd", "Sněžka", "Lysá hora"], "spravne": "Sněžka", "typ": "volba", "kategorie": "1"},
        # Otevřená otázka nemá klíč "moznosti", protože uživatel píše text sám.
        {"text": "Napiš hlavní město Francie:", "spravne": "Paříž", "typ": "otevrena", "kategorie": "1"},
        {"text": "Jak se jmenuje nejdelší řeka světa?", "spravne": "Amazonka", "typ": "otevrena", "kategorie": "1"},
        {"text": "Kolik kontinentů je tradičně na Zemi?", "moznosti": ["5", "6", "7"], "spravne": "7", "typ": "volba", "kategorie": "1"},

        # KATEGORIE 2: Věda a technika
        {"text": "Kolik je 5 + 5?", "moznosti": ["10", "12", "8"], "spravne": "10", "typ": "volba", "kategorie": "2"},
        {"text": "Která planeta je nejblíže Slunci?", "moznosti": ["Venuše", "Merkur", "Země"], "spravne": "Merkur", "typ": "volba", "kategorie": "2"},
        {"text": "Jaký chemický prvek má značku O?", "moznosti": ["Zlato", "Kyslík", "Olovo"], "spravne": "Kyslík", "typ": "volba", "kategorie": "2"},
        {"text": "Který savec umí jako jediný aktivně létat?", "spravne": "netopýr", "typ": "otevrena", "kategorie": "2"},
        {"text": "Který programovací jazyk používáme pro tento kvíz?", "moznosti": ["Java", "Python", "C++"], "spravne": "Python", "typ": "volba", "kategorie": "2"},

        # KATEGORIE 3: Rychlovky
        # Časovka má navíc klíč "limit", který říká, kolik sekund má hráč na odpověď.
        {"text": "RYCHLOVKA: Kolik je 7 * 8?", "spravne": "56", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Jaká je chemická značka vody?", "spravne": "H2O", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Jaké je hlavní město Slovenska?", "spravne": "Bratislava", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Kolik minut má jedna hodina?", "spravne": "60", "typ": "casovka", "limit": 10, "kategorie": "3"},
        {"text": "RYCHLOVKA: Napiš zkratku České republiky:", "spravne": "ČR", "typ": "casovka", "limit": 10, "kategorie": "3"}
    ]

    # Běžný výpis textu na obrazovku.
    print("=== VÍTEJ V PARÁDNÍM MULTI-KVÍZU ===")
    
    # Příkaz 'input' pozastaví program a čeká, co uživatel napíše na klávesnici.
    # Metoda '.strip()' z textu automaticky odstraní mezery na začátku a na konci (kdyby se uživatel přepsal).
    # Výsledek se uloží do proměnné 'jmeno_hrace'.
    jmeno_hrace = input("Zadej své jméno: ").strip()
    
    # Připravíme si proměnnou pro nejlepší výsledek a nastavíme ji na nulu.
    osobni_rekord = 0

    # 'while True' vytvoří tzv. nekonečný cyklus. 
    # Všechno, co je pod ním odsazené, se bude opakovat pořád dokola, dokud cyklus násilně neukončíme.
    while True:
        # Výpis nabídky (Menu) na obrazovku.
        print("\nVyber si téma kvízu:")
        print("1) Geografie (Uzavřené i otevřené otázky)")
        print("2) Věda a technika (Matematika, vesmír, IT)")
        print("3) Rychlovky (Všechny otázky mají limit 10 sekund!)")
        
        # Čekáme, až uživatel napíše číslo 1, 2, nebo 3 a uložíme ho do 'volba_kategorie'.
        volba_kategorie = input("Zadej číslo kategorie (1/2/3): ").strip()
        
        # Zkontrolujeme, jestli uživatel nezadal nějaký nesmysl (např. písmeno 'A' nebo číslo '5').
        if volba_kategorie not in ["1", "2", "3"]:
            print("Neplatná volba! Zkus to znovu.")
            # Příkaz 'continue' zastaví aktuální oběh cyklu 'while' a vrátí ho úplně na začátek (znovu zobrazí menu).
            continue
            
        # Vytvoříme si nový, zatím prázdný seznam pro filtrované otázky.
        aktivni_otazky = []
        
        # Cyklus 'for' projde úplně všechny otázky v naší velké databázi (jednu po druhé).
        for o in otazky:
            # Ptáme se: Rovná se číslo kategorie u této otázky tomu číslu, které zadal hráč?
            if o["kategorie"] == volba_kategorie:
                # Pokud ano, přidáme (.append) tuto otázku do našeho nového seznamu.
                aktivni_otazky.append(o)

        # Vezmeme ten nový seznam správných otázek a náhodně jim přeházíme pořadí.
        random.shuffle(aktivni_otazky)
        
        # Vynulujeme skóre pro toto konkrétní kolo.
        skore = 0
        
        # Začíná cyklus, který postupně vytahuje jednu otázku za druhou ze seznamu 'aktivni_otazky'.
        for otazka in aktivni_otazky:
            # Vytiskne oddělovací čáru (znak '-' zopakovaný 30x) pro hezčí vzhled.
            print("-" * 30)
            # Vypíše na obrazovku samotný text otázky z databáze.
            print(otazka["text"])
            
            # --- ZPRACOVÁNÍ ČASOVKY ---
            # Zeptáme se programu, jestli je tato konkrétní otázka typu "casovka".
            if otazka["typ"] == "casovka":
                print(f"!!! POZOR, máš jen {otazka['limit']} sekund !!!")
                
                # Funkce time.time() si zjistí přesný aktuální čas v počítači a my si ho uložíme.
                start_cas = time.time()
                # Čekáme na Enter od uživatele.
                odpoved = input("Tvoje odpověď: ")
                # Jakmile hráč zmáčkne Enter, hned si znovu uložíme aktuální čas.
                konec_cas = time.time()
                
                # Odečteme starý čas od nového. Tím zjistíme, kolik sekund to přesně trvalo.
                uplynuly_cas = konec_cas - start_cas
                
                # Zkontrolujeme, jestli to hráči netrvalo déle, než byl povolený limit.
                if uplynuly_cas > otazka["limit"]:
                    # Příkaz ':.1f' zařídí, že se čas zaokrouhlí na 1 desetinné místo.
                    print(f">>> Čas vypršel! Trvalo ti to {uplynuly_cas:.1f} s.")
                    print(f">>> Správně bylo: {otazka['spravne']}")
                    # Hráč to nestihl. 'continue' přeskočí zbytek kódu a jde rovnou na další otázku.
                    continue
            
            # --- ZPRACOVÁNÍ VÝBĚROVÝCH OTÁZEK ---
            # 'elif' znamená "jinak pokud". Pokud to nebyla časovka, ptáme se, jestli to je "volba".
            elif otazka["typ"] == "volba":
                # Vytvoříme si přesnou kopii seznamu možností (abychom nepomíchali originál).
                aktualni_moznosti = otazka["moznosti"].copy()
                # Tuto kopii náhodně zamícháme.
                random.shuffle(aktualni_moznosti)
                
                # Připravíme si seznam písmenek.
                pismena = ["a", "b", "c"]
                # Prázdná proměnná pro uchování správného písmene.
                pismeno_spravne_odpovedi = ""
                
                # 'enumerate' nám k seznamu vygeneruje čísla (indexy). 0, 1, 2...
                for index, moznost in enumerate(aktualni_moznosti):
                    # Podle čísla (indexu) vytáhneme správné písmenko (0 = a, 1 = b, 2 = c).
                    pismenko = pismena[index]
                    # Vytiskneme uživateli např.: "a) Ostrava"
                    print(f"{pismenko}) {moznost}")
                    
                    # Zkontrolujeme: "Je tento vypsaný text tou správnou odpovědí?"
                    if moznost == otazka["spravne"]:
                        # Pokud ano, zapamatujeme si jeho písmenko.
                        pismeno_spravne_odpovedi = pismenko
                
                # Získáme od hráče písmenko. '.lower()' zaručí malá písmena.
                odpoved = input("Tvoje volba (a/b/c): ").lower().strip()
                # Správná odpověď, kterou budeme kontrolovat, je to uložené písmenko.
                kontrola_spravnosti = pismeno_spravne_odpovedi
                
            # --- ZPRACOVÁNÍ OTEVŘENÝCH OTÁZEK ---
            # 'else' znamená "pokud to nebylo nic z předchozího" (zbývá jen otevřená).
            else:
                # Chceme jen textový vstup od uživatele.
                odpoved = input("Tvoje odpověď: ")
                # Správná odpověď je přesně ten text z databáze.
                kontrola_spravnosti = otazka["spravne"]

            # --- FINÁLNÍ VYHODNOCENÍ ODPOVĚDI ---
            # Porovnáme to, co hráč napsal, s tím, co měl napsat.
            # Obě strany zmenšíme a osekneme o mezery pro férovou kontrolu.
            if odpoved.lower().strip() == kontrola_spravnosti.lower().strip():
                print(">>> Správně!")
                # Přidáme 1 bod.
                skore += 1
            else:
                # Odpověděl špatně. U voleb vypíšeme i písmenko pro lepší orientaci.
                if otazka["typ"] == "volba":
                    print(f">>> Špatně! Správná volba byla: {kontrola_spravnosti}) {otazka['spravne']}")
                else:
                    print(f">>> Špatně! Správně bylo: {otazka['spravne']}")
        
        # --- KONEC CELÉHO KOLA ---
        # Cyklus for (průchod otázkami) skončil. 
        # Zjistíme, jestli hráč nepřekonal svůj osobní rekord.
        if skore > osobni_rekord:
            # Pokud ano, přepíšeme rekord novým skóre.
            osobni_rekord = skore
            print("\n*** NOVÝ OSOBNÍ REKORD V TÉTO KATEGORII! ***")

        # Vytiskneme závěrečné zhodnocení se jménem, body a rekordem.
        print("\n" + "=" * 35)
        print(f"Hráč: {jmeno_hrace}")
        print(f"Skóre z této hry: {skore} / {len(aktivni_otazky)}")
        print(f"Tvůj nejlepší výsledek: {osobni_rekord} / {len(aktivni_otazky)}")
        print("=" * 35)

        # Zeptáme se, jestli chce hrát další kolo.
        if input("Chceš hrát znovu? (ano/ne): ").lower().strip() != "ano":
            # Pokud napsal cokoliv jiného než slovo "ano", rozloučíme se.
            print(f"Díky za hru, {jmeno_hrace}! Měj se.")
            # Příkaz 'break' okamžitě zabije tu nekonečnou hlavní smyčku 'while True'. Hra skončí.
            break

# Technické pravidlo Pythonu. Říká: "Pokud je tento soubor spuštěn napřímo, 
# zavolej a spusť funkci 'spustit_kviz()'."
if __name__ == "__main__":
    spustit_kviz()
