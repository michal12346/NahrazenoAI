# Název projektu: Parádní Multi-Kvíz

## Popis a cíl projektu
**Parádní Multi-Kvíz** je interaktivní konzolová hra vytvořená v jazyce Python. Hlavním cílem tohoto projektu je poskytnout hráčům zábavný a dynamický způsob, jak otestovat své vědomosti v různých oborech, a zároveň si procvičit rychlé rozhodování pod tlakem. Hra je koncipována tak, aby nabídla vysokou znovuhratelnost díky míchání otázek a ukládání nejvyššího skóre napříč spuštěními.

---

## Popis funkcionality programu

Program nabízí následující prvky a herní mechaniky, díky kterým je uživatelský zážitek bohatý:

* **Výběr herní kategorie:** Hráč není vázán na jeden druh otázek, ale na počátku herní smyčky si může vybrat ze třech tematických oblastí (Geografie, Věda a technika, Rychlovky).
* **Různé formáty otázek:** * Výběr z možností (hráč volí a, b, nebo c).
  * Otevřené otázky (hráč ručně vepisuje text).
  * Časovky (rychlé otázky, na které má hráč striktní časový limit).
* **Dynamický barevný výstup:** Prostředí terminálu ožívá díky barvám. Pozitivní zpětná vazba svítí zeleně, chybné odpovědi či varování červeně.
* **Systém životů:** Hráč disponuje třemi životy. Každá nesprávná odpověď (nebo nestihnutí časového limitu) život odečte. Jakmile klesnou na nulu, nastává Game Over.
* **Možnost předčasného ukončení:** Do jakéhokoliv pole pro odpověď lze napsat slovo `konec`. Tato funkce okamžitě ukončí aktuální hru a přesune hráče rovnou k vyhodnocení skóre.
* **Shrnutí chyb:** Pokud hráč ztratí životy, systém mu na konci kola pro zpětnou vazbu vypíše přesné znění otázek, ve kterých pochybil.

---

## Technická část

Aplikace je napsána strukturovaně a využívá základní principy programování pro efektivní chod:

* **Použité knihovny:** * `random`: Využíváno především pro metodu `random.shuffle()`, která zajišťuje náhodné pořadí otázek a náhodné prohazování možností u výběrových otázek, aby každá hra byla unikátní.
  * `time`: Slouží pro výpočet uplynulého času. Metoda `time.time()` poskytne UNIXový čas před a po inputu od uživatele a z jejich rozdílu je vypočtena rychlost.
* **Vlastní datové struktury:** Jádrem celého programu je struktura vrstvená kombinací **seznamů (List)** a **slovníků (Dictionary)**. Celá databáze je uložena v jediném seznamu `otazky`, kde každý prvek tvoří strukturovaný slovník reprezentující jednu otázku a její vlastnosti (typ, správná odpověď, kategorie). Toto řešení je velmi snadno rozšiřitelné (škálovatelné). Ke konci hry se navíc dynamicky plní pomocný seznam `seznam_chyb`.
* **Práce se soubory (I/O) a výjimky:** Nejvyšší dosažené skóre se trvale zapisuje do souboru `rekord.txt` na lokálním disku (`open(..., "w")`). Při zapnutí programu se skóre naopak načítá (`open(..., "r")`). V této fázi je použit blok `try-except`, který elegantně ošetřuje výjimku `FileNotFoundError` (pro případy, kdy uživatel spouští hru úplně poprvé a soubor ještě fyzicky neexistuje).
* **Formátování konzole:** Kód využívá nadefinované konstanty ANSI escape sekvencí (např. `\033[92m`) ke změně výstupní barvy textu zabudované přímo ve f-string výpisech.
