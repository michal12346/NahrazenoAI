# Kviz - DVACÁTÁDRUHÁ VERZE

import random  # Importuje vestavěný modul 'random' pro náhodné míchání otázek a možností.
import time  # Importuje vestavěný modul 'time' pro sledování přesného uplynulého času.

ZELENA = '\033[92m'  # Definuje ANSI kód do proměnné pro obarvení konzolového textu na zeleno.
CERVENA = '\033[91m'  # Definuje ANSI kód do proměnné pro obarvení konzolového textu na červeno.
ZLUTA = '\033[93m'  # Definuje ANSI kód do proměnné pro obarvení konzolového textu na žluto.
RESET = '\033[0m'  # Definuje ANSI kód pro resetování barvy zpět na výchozí nastavení terminálu.

def spustit_kviz():  # Definuje hlavní funkci programu s názvem 'spustit_kviz', ve které běží hra.
    otazky = [  # Inicializuje proměnnou 'otazky' jako seznam (list), který bude držet databázi.
        # --- KATEGORIE 1: Geografie ---  # Komentář pro vizuální oddělení 1. kategorie v kódu.
        {"text": "Jaké je hlavní město ČR?", "moznosti": ["Praha", "Brno", "Ostrava"], "spravne": "Praha", "typ": "volba", "kategorie": "1"},  # 1. otázka: slovník s klíči pro text, volby a správnou odpověď.
        {"text": "Jaká je nejvyšší hora České republiky?", "moznosti": ["Praděd", "Sněžka", "Lysá hora"], "spravne": "Sněžka", "typ": "volba", "kategorie": "1"},  # 2. otázka (Geografie, volba ze 3).
        {"text": "Napiš hlavní město Francie:", "spravne": "Paříž", "typ": "otevrena", "kategorie": "1"},  # 3. otázka: typ 'otevrena', tzn. nemá seznam možností k výběru.
        {"text": "Jak se jmenuje nejdelší řeka světa?", "spravne": "Amazonka", "typ": "otevrena", "kategorie": "1"},  # 4. otázka (otevřený textový vstup).
        {"text": "Kolik kontinentů je tradičně na Zemi?", "moznosti": ["5", "6", "7"], "spravne": "7", "typ": "volba", "kategorie": "1"},  # 5. otázka (volba ze 3).
        {"text": "Který oceán je největší na světě?", "moznosti": ["Tichý", "Atlantský", "Indický"], "spravne": "Tichý", "typ": "volba", "kategorie": "1"},  # 6. otázka (volba ze 3).
        {"text": "Napiš hlavní město Itálie:", "spravne": "Řím", "typ": "otevrena", "kategorie": "1"},  # 7. otázka (otevřený text).
        {"text": "Jaký je nejmenší stát světa?", "moznosti": ["Monako", "Vatikán", "San Marino"], "spravne": "Vatikán", "typ": "volba", "kategorie": "1"},  # 8. otázka (volba ze 3).
        {"text": "Na kterém kontinentu leží Egypt?", "moznosti": ["Asie", "Afrika", "Evropa"], "spravne": "Afrika", "typ": "volba", "kategorie": "1"},  # 9. otázka (volba ze 3).
        {"text": "Napiš jméno státu, který je naším východním sousedem:", "spravne": "Slovensko", "typ": "otevrena", "kategorie": "1"},  # 10. otázka (otevřený text).

        # --- KATEGORIE 2: Věda a technika ---  # Komentář pro vizuální oddělení 2. kategorie v kódu.
        {"text": "Kolik je 5 + 5?", "moznosti": ["10", "12", "8"], "spravne": "10", "typ": "volba", "kategorie": "2"},  # 11. otázka (Věda, volba ze 3).
        {"text": "Která planeta je nejblíže Slunci?", "moznosti": ["Venuše", "Merkur", "Země"], "spravne": "Merkur", "typ": "volba", "kategorie": "2"},  # 12. otázka (Věda, volba).
        {"text": "Jaký chemický prvek má značku O?", "moznosti": ["Zlato", "Kyslík", "Olovo"], "spravne": "Kyslík", "typ": "volba", "kategorie": "2"},  # 13. otázka (Věda, volba).
        {"text": "Který savec umí jako jediný aktivně létat?", "spravne": "netopýr", "typ": "otevrena", "kategorie": "2"},  # 14. otázka (Věda, otevřená).
        {"text": "Který programovací jazyk používáme pro tento kvíz?", "moznosti": ["Java", "Python", "C++"], "spravne": "Python", "typ": "volba", "kategorie": "2"},  # 15. otázka (Věda, volba).
        {"text": "Který orgán pumpuje krev v lidském těle?", "spravne": "srdce", "typ": "otevrena", "kategorie": "2"},  # 16. otázka (Věda, otevřená).
        {"text": "Kolik je 12 * 12?", "moznosti": ["144", "124", "142"], "spravne": "144", "typ": "volba", "kategorie": "2"},  # 17. otázka (Věda, volba).
        {"text": "Jak se jmenuje galaxie, ve které se nachází Země?", "moznosti": ["Andromeda", "Mléčná dráha", "Sombrero"], "spravne": "Mléčná dráha", "typ": "volba", "kategorie": "2"},  # 18. otázka (Věda, volba).
        {"text": "Napiš chemickou značku pro zlato:", "spravne": "Au", "typ": "otevrena", "kategorie": "2"},  # 19. otázka (Věda, otevřená).
        {"text": "Kdo zformuloval teorii relativity?", "moznosti": ["Isaac Newton", "Albert Einstein", "Nikola Tesla"], "spravne": "Albert Einstein", "typ": "volba", "kategorie": "2"},  # 20. otázka (Věda, volba).

        # --- KATEGORIE 3: Rychlovky ---  # Komentář pro vizuální oddělení 3. kategorie v kódu.
        {"text": "RYCHLOVKA: Kolik je 7 * 8?", "spravne": "56", "typ": "casovka", "limit": 10, "kategorie": "3"},  # 21. otázka. Typ 'casovka' vyžaduje uložení klíče 'limit' v sekundách.
        {"text": "RYCHLOVKA: Jaká je chemická značka vody?", "spravne": "H2O", "typ": "casovka", "limit": 10, "kategorie": "3"},  # 22. otázka (časovka).
        {"text": "RYCHLOVKA: Jaké je hlavní město Slovenska?", "spravne": "Bratislava", "typ": "casovka", "limit": 10, "kategorie": "3"},  # 23. otázka (časovka).
        {"text": "RYCHLOVKA: Kolik minut má jedna hodina?", "spravne": "60", "typ": "casovka", "limit": 10, "kategorie": "3"},  # 24. otázka (časovka).
        {"text": "RYCHLOVKA: Napiš zkratku České republiky:", "spravne": "ČR", "typ": "casovka", "limit": 10, "kategorie": "3"},  # 25. otázka (časovka).
        {"text": "RYCHLOVKA: Jaký je výsledek 100 / 4?", "spravne": "25", "typ": "casovka", "limit": 10, "kategorie": "3"},  # 26. otázka (časovka).
        {"text": "RYCHLOVKA: Kolik nohou má pavouk?", "spravne": "8", "typ": "casovka", "limit": 10, "kategorie": "3"},  # 27. otázka (časovka).
        {"text": "RYCHLOVKA: Jaký den v týdnu následuje po pátku?", "spravne": "sobota", "typ": "casovka", "limit": 10, "kategorie": "3"},  # 28. otázka (časovka).
        {"text": "RYCHLOVKA: Napiš oficiální zkratku pro Evropskou unii:", "spravne": "EU", "typ": "casovka", "limit": 10, "kategorie": "3"},  # 29. otázka (časovka).
        {"text": "RYCHLOVKA: Kolik měsíců má jeden kalendářní rok?", "spravne": "12", "typ": "casovka", "limit": 10, "kategorie": "3"}  # 30. otázka (časovka).
    ]  # Uzavírací závorka pro hlavní seznam 'otazky'.

    print(f"{ZLUTA}=== VÍTEJ V PARÁDNÍM MULTI-KVÍZU ===\n{RESET}")  # Vypíše úvodní nápis aplikace žlutou barvou a barvu zresetuje s odřádkováním (\n).
    jmeno_hrace = input("Zadej své jméno: ").strip()  # Požádá uživatele o zadání textu (jména) a odstraní přebytečné mezery na krajích.
    
    try:  # Vytváří 'try' blok, který se pokusí spustit rizikový kód, jenž by mohl vyhodit chybu.
        with open("rekord.txt", "r", encoding="utf-8") as soubor:  # Pokusí se otevřít soubor 'rekord.txt' v režimu pro čtení 'r'.
            osobni_rekord = int(soubor.read())  # Přečte obsah textového souboru a přetypuje ho na celé číslo.
            print(f"{ZELENA}> Načten tvůj historický rekord ze souboru: {osobni_rekord} bodů!{RESET}")  # Vypíše hlášku o načtení rekordu zeleně.
    except FileNotFoundError:  # Zpracuje specifickou chybu: Pokud se soubor nenašel (např. při prvním spuštění).
        osobni_rekord = 0  # Protože neexistuje soubor s rekordem, nastaví osobní rekord hráče na nulu.
        print(f"{ZLUTA}> Zatím nemáš uložený žádný rekord. Čas ho vytvořit!{RESET}")  # Informuje o neexistenci rekordu žlutým písmem.

    while True:  # Zakládá hlavní nekonečnou smyčku celé hry (kterou lze ukončit pouze pomocí 'break').
        print("\nVyber si téma kvízu:")  # Vypíše prázdný řádek a hlavičku pro menu s kategoriemi.
        print("1) Geografie")  # Vypíše volbu číslo 1.
        print("2) Věda a technika")  # Vypíše volbu číslo 2.
        print("3) Rychlovky")  # Vypíše volbu číslo 3.
        
        volba_kategorie = input("Zadej číslo kategorie (1/2/3): ").strip()  # Požádá hráče o napsání čísla kategorie z menu.
        if volba_kategorie not in ["1", "2", "3"]:  # Prověří, jestli vstup není nesmyslný (tzn. neobsahuje validní číslo 1, 2 nebo 3).
            print(f"{CERVENA}Neplatná volba! Zkus to znovu.{RESET}")  # Vypíše chybovou zprávu červenou barvou.
            continue  # Přeskočí veškerý kód pod sebou a spustí aktuální 'while' smyčku znovu od začátku.
            
        aktivni_otazky = []  # Vytvoří nový prázdný seznam pro uložení otázek jen z vybrané kategorie.
        for o in otazky:  # Inicializuje 'for' cyklus, který postupně bere jednu otázku po druhé z naší databáze.
            if o["kategorie"] == volba_kategorie:  # Zkontroluje, zda se klíč 'kategorie' otázky rovná vstupu od hráče.
                aktivni_otazky.append(o)  # Pokud ano, přidá danou otázku do našeho čistého seznamu 'aktivni_otazky'.

        random.shuffle(aktivni_otazky)  # Vezme vyfiltrovaný seznam a náhodně prohází pořadí prvků uvnitř něj.
        skore = 0  # Vynuluje hráči dosažené skóre před začátkem nového kola.
        zivoty = 3  # Nastaví hráči 3 pokusy/životy pro aktuální kolo.
        seznam_chyb = []  # Vytvoří prázdný seznam, do kterého budeme přidávat otázky zodpovězené špatně.
        
        for otazka in aktivni_otazky:  # Spustí 'for' cyklus, který bude procházet postupně zamíchané otázky zvolené kategorie.
            print("-" * 30)  # Vytiskne oddělovací horizontální čáru skládající se ze 30 pomlček.
            print(f"Tvůj stav: {'❤️ ' * zivoty}")  # Vytiskne emoji srdíček odpovídající aktuálnímu počtu životů v proměnné.
            print(f"(Pro ukončení kvízu napiš slovo 'konec')")  # Oznámí hráči existenci tajného klíčového slova.
            print(f"{ZLUTA}{otazka['text']}{RESET}")  # Vytiskne text samotné otázky zlovníku, přičemž text obarví žlutě.
            
            if otazka["typ"] == "casovka":  # Vyhodnocuje: Pokud klíč 'typ' ve slovníku otázky obsahuje hodnotu 'casovka'...
                print(f"{CERVENA}!!! POZOR, máš jen {otazka['limit']} sekund !!!{RESET}")  # Vytiskne varování červeně včetně informace o sekundách.
                start_cas = time.time()  # Zavolá metodu time.time() pro zachycení přesného momentálního času do proměnné.
                odpoved = input("Tvoje odpověď: ")  # Zobrazí prompt a čeká se zablokovaným programem, dokud hráč nestiskne Enter.
                konec_cas = time.time()  # Ihned po stisknutí Enteru zapíše nový časový otisk.
                uplynuly_cas = konec_cas - start_cas  # Odečtením času před začátkem od času na konci získá délku řešení.
                
                if odpoved.lower().strip() == "konec":  # Pokud hráč napsal magické slovo pro konec (zkonvertováno na malá písmena pro jistotu):
                    print(f"\n{ZLUTA}>>> HRA PŘEDČASNĚ UKONČENA HRÁČEM.{RESET}")  # Vypíše upozornění o vynuceném konci.
                    break  # Příkaz 'break' okamžitě zastaví běh tohoto 'for' cyklu a pošle program na vyhodnocování skóre.

                if uplynuly_cas > otazka["limit"]:  # Pokud vypočítaný strávený čas je vyšší než povolený limit z otázky:
                    print(f"{CERVENA}>>> Čas vypršel! Trvalo ti to {uplynuly_cas:.1f} s.{RESET}")  # Oznámí překročení limitu a zobrazí čas s 1 des. místem.
                    print(f"{CERVENA}>>> Správně bylo: {otazka['spravne']}{RESET}")  # Vypíše uživateli, co byla správná odpověď.
                    zivoty -= 1  # Odečte 1 bod z proměnné životy.
                    seznam_chyb.append(otazka["text"])  # Zapíše znění otázky do pole chyb pro závěrečnou zpětnou vazbu.
                else:  # V opačném případě (čas vypršet nestihl):
                    kontrola_spravnosti = otazka["spravne"]  # Připraví do společné proměnné pro porovnávání string se správnou odpovědí.
            
            elif otazka["typ"] == "volba":  # Zkontroluje druhou větev, pokud je 'typ' nastaven na 'volba' (multiple choice).
                aktualni_moznosti = otazka["moznosti"].copy()  # Vyrobí mělkou kopii seznamu možností (abychom nezamíchali originál).
                random.shuffle(aktualni_moznosti)  # Náhodně přeskupí odpovědi a, b, c.
                pismena = ["a", "b", "c"]  # Vytvoří pevný list písmen, která budeme vizuálně lepit k možnostem.
                pismeno_spravne_odpovedi = ""  # Inicializuje prázdný string, do kterého později zapíše správné písmeno.
                
                for index, moznost in enumerate(aktualni_moznosti):  # Funkce 'enumerate' vrátí zároveň pořadí prvku (0, 1, 2) a jeho text.
                    pismenko = pismena[index]  # Vezme z listu písmen konkrétní písmeno podle indexu (např. 'a' pro index 0).
                    print(f"{pismenko}) {moznost}")  # Vypíše na terminál sestavený řetězec: písmeno, závorka, mezera, text možnosti.
                    if moznost == otazka["spravne"]:  # Porovná, jestli je momentálně renderovaná možnost ta správná ze slovníku.
                        pismeno_spravne_odpovedi = pismenko  # Jestli jo, uložíme do proměnné její přiřazené písmeno k pozdější kontrole.
                
                odpoved = input("Tvoje volba (a/b/c nebo konec): ").lower().strip()  # Počká na odpověď uživatele, ořízne ji a hodí na malá písmena.
                if odpoved == "konec":  # Opět zachytává, zda hráč nenapsal trigger pro předčasný konec.
                    print(f"\n{ZLUTA}>>> HRA PŘEDČASNĚ UKONČENA HRÁČEM.{RESET}")  # Vypíše upozornění o ukončení.
                    break  # Přeruší smyčku s otázkami.
                kontrola_spravnosti = pismeno_spravne_odpovedi  # Řekneme programu, že s odpovědí hráče se má porovnávat získané písmenko.
                
            else:  # Blok 'else' znamená, že to není ani 'casovka' ani 'volba', zbývá jedině 'otevrena'.
                odpoved = input("Tvoje odpověď: ")  # Zobrazí čistý input field bez extra pravidel.
                if odpoved.lower().strip() == "konec":  # I zde hlídá, jestli hráč nezadal 'konec'.
                    print(f"\n{ZLUTA}>>> HRA PŘEDČASNĚ UKONČENA HRÁČEM.{RESET}")  # Oznámení pro hráče.
                    break  # Uteče ze smyčky otázek.
                kontrola_spravnosti = otazka["spravne"]  # Zde se porovnává přímo text odpovědi napsaný v proměnné otázky.

            if otazka["typ"] != "casovka" or (otazka["typ"] == "casovka" and uplynuly_cas <= otazka["limit"]):  # Zabrání kontrole správnosti textu v momentě, kdy hráč failnul kvůli limitu u časovky.
                if odpoved.lower().strip() == kontrola_spravnosti.lower().strip():  # Očistí a zmenší vstupy a porovná je.
                    print(f"{ZELENA}>>> Správně!{RESET}")  # Obojí se shoduje, takže vypíše zeleně povzbuzení.
                    skore += 1  # Matematicky přičte hráči jedničku na počítadle bodů.
                else:  # V opačném případě (vstupy se neshodují):
                    if otazka["typ"] == "volba":  # U otázek typu volba chceme ukázat nejen správný text, ale i správné písmeno.
                        print(f"{CERVENA}>>> Špatně! Správná volba byla: {kontrola_spravnosti}) {otazka['spravne']}{RESET}")  # Vytiskne písmeno i text červeně.
                    else:  # Pro ostatní typy otázek:
                        print(f"{CERVENA}>>> Špatně! Správně bylo: {otazka['spravne']}{RESET}")  # Vytiskne jen správný text bez písmene (červeně).
                    zivoty -= 1  # Odečte od životů hráče jedničku.
                    seznam_chyb.append(otazka["text"])  # Pošle znění otázky do chybového seznamu, abychom ho v závěru vypsali.
            
            if zivoty <= 0:  # Kontroluje zásadní pravidlo, zda hráč neklesl se životy na limit nebo pod něj.
                print(f"{CERVENA}\n" + "💀" * 15)  # Vypíše nový prázdný řádek a namnoží červenou lebku 15x.
                print("   GAME OVER! DOŠLY TI ŽIVOTY.")  # Vypíše klasickou obrazovku prohry.
                print("💀" * 15 + f"{RESET}")  # Znovu namnoží lebku, ale tady už nezapomene resetovat barvu.
                break  # Donutí 'for' cyklus s otázkami skončit, protože mrtvý hráč nemůže pokračovat.
        
        if skore > osobni_rekord:  # Pokud hráč dosáhl konce cyklu, zkontrolujeme, jestli jeho aktuální body přesáhly nejlepší načtený výkon.
            osobni_rekord = skore  # Pokud ano, překlopíme novou hodnotu skóre do proměnné starého rekordu.
            print(f"{ZELENA}\n*** NOVÝ HISTORICKÝ REKORD! ***{RESET}")  # Upozorní hráče zeleně na mimořádný výkon.
            
            with open("rekord.txt", "w", encoding="utf-8") as soubor:  # Otevře soubor rekord.txt, tentokrát však v přepisovacím režimu zápisu ('w').
                soubor.write(str(osobni_rekord))  # Vyžádá si číslo osobního rekordu, zabalí jej do typu text (str) a vtiskne do souboru.
                print(f"{ZELENA}> (Rekord byl bezpečně uložen na tvůj disk){RESET}")  # Upozorní uživatele na úspěšný fyzický zápis na HDD/SSD.

        print("\n" + "=" * 35)  # Začíná sekce závěrečného zhodnocení, vizuálně oddělená 35 rovnítky.
        print(f"Hráč: {jmeno_hrace}")  # Vypíše proměnnou uchovávající jméno hráče.
        print(f"Skóre z této hry: {skore}")  # Vypíše počet bodů získaných za toto proběhlé kolo.
        print(f"Tvůj historický rekord: {osobni_rekord}")  # Vypíše aktuální rekordní stav.
        print("=" * 35)  # Dokončí orámování tabulky výsledků.
        
        if len(seznam_chyb) > 0:  # Zkontroluje, jestli funkce `len` (délka seznamu) naměří víc než 0 špatně zodpovězených otázek.
            print(f"\n{CERVENA}Otázky, ve kterých jsi chyboval:{RESET}")  # Vypíše červený štítek oznamující začátek listu chyb.
            for chyba in seznam_chyb:  # Spustí malý 'for' cyklus, co proiteruje prvek po prvku celý list chyb.
                print(f"- {chyba}")  # Vykreslí každou špatně zodpovězenou otázku odsazenou malou pomlčkou.

        if input("\nChceš hrát znovu? (ano/ne): ").lower().strip() != "ano":  # Vyzve hráče k zadání potvrzení pro novou hru. Pokud odpoví jinak než přesně "ano"...
            print(f"Díky za hru, {jmeno_hrace}! Měj se.")  # Rozloučí se a vypíše poděkování a jméno.
            break  # Ukončí hlavní 'while True' herní smyčku programu, což povede k dojetí a samovolnému vypnutí konzole.

if __name__ == "__main__":  # Speciální programovací konstrukce. Podmínka zjišťuje, jestli byl tento Python soubor spuštěn na přímo uživatelem.
    spustit_kviz()  # Pokud je podmínka splněna (není importován přes jiný skript), dojde ke skutečnému vyvolání funkce.
