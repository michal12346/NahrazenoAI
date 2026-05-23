# Název projektu
Univerzální modulární kvíz s časovým limitem a kategoriemi

# Popis a cíl projektu
Cílem projektu je vytvořit pokročilou konzolovou aplikaci v jazyce Python pro testování vědomostí. Projekt demonstruje, jak v praxi dynamicky pracovat s datovými strukturami, čistit uživatelské vstupy a implementovat časově závislou logiku (real-time management) bez nutnosti grafického rozhraní.

# Popis funkcionality programu
Program na začátku identifikuje uživatele pomocí vstupu pro jméno a inicializuje paměť pro osobní rekordy. Následně nabídne interaktivní menu se třemi tématickými kategoriemi: Geografie, Věda a technika, Rychlovky. 

Po výběru kategorie program dynamicky vyfiltruje příslušné otázky z databáze a spustí herní smyčku:
1. **Výběrové otázky:** Možnosti jsou před zobrazením náhodně promíchány a dynamicky indexovány písmeny a), b), c). Správná volba se tedy mění s každým spuštěním.
2. **Otevřené otázky:** Vyžadují přímý textový zápis odpovědi.
3. **Časové rychlovky:** Aktivují interní stopky. Pokud časový rozdíl mezi zobrazením otázky a odesláním odpovědi přesáhne 10 sekund, odpověď je neplatná.

Aplikace zpracovává vstupy robustně (ignoruje chyby v mezerách a velikosti písmen). Na konci kola vyhodnotí úspěšnost, aktualizuje osobní rekord hráče a umožní opakované spuštění.

# Technická část
* **Použité knihovny:** * `random`: Využití metod `random.shuffle()` pro míchání pořadí otázek i samotných textových odpovědí.
  * `time`: Využití funkce `time.time()` pro získání unixového času v sekundách a měření reakční doby.
* **Algoritmy a řídící struktury:** * **Filtrování dat (List comprehension / Cyklus):** Algoritmus na základě uživatelské volby projde celou databázi a sestaví seznam otázek s odpovídajícím ID kategorie.
  * **Enumerate a mapování:** Indexování zamíchaných polí a jejich provázání s kontrolními klíči.
  * **Řízení toku (continue / break):** Příkaz `continue` zajišťuje okamžité vypršení limitu bez závislosti na správnosti napsaného slova.
* **Vlastní datové struktury:** Komplexní vnořená struktura typu Seznam slovníků (`List of Dictionaries`), kde hodnota klíče `"moznosti"` obsahuje další vnořený Seznam (`List`) textových řetězců.
* **Volání externího API:** Program nevyužívá síťové přenosy a běží lokálně.
