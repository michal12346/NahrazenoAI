# Generátor hesel s lokální historií

## Popis a cíl projektu
Tato aplikace slouží k automatickému generování silných a bezpečných hesel. Cílem projektu je poskytnout jednoduchý nástroj, který uživateli nejen vytvoří bezpečné heslo, ale zároveň si ho zapamatuje – ukládá totiž veškerou historii vygenerovaných hesel do lokální databáze. 

Aplikace je určena pro uživatele, kteří potřebují rychle tvořit spolehlivá hesla a chtějí k nim mít zpětný přístup, i pro vývojáře hledající praktickou ukázku propojení Pythonu s databází SQLite.

## Funkcionalita programu
Program po spuštění funguje plně automaticky a skládá se z následujících technických kroků:
* **Inicializace databáze:** Aplikace si sama zkontroluje a případně vytvoří databázový soubor včetně potřebné tabulky pro ukládání dat.
* **Tvorba hesla:** Vygeneruje náhodné heslo ze sady velkých i malých písmen, číslic a speciálních znaků.
* **Trvalé uložení:** Záznam (heslo, jeho délku a aktuální čas) bezpečně vloží do databáze.
* **Zobrazení historie:** Načte a do konzole vypíše všechny záznamy, které kdy byly do databáze uloženy.

## Technická část
Projekt je naprogramován v jazyce Python. Nevyžaduje instalaci žádných externích balíčků třetích stran, staví čistě na vestavěných modulech:

* **Použité knihovny:**
    * `sqlite3`: Pro správu a komunikaci s lokální databází.
    * `secrets`: Klíčový bezpečnostní prvek. Místo běžného generátoru používá kryptograficky bezpečný výběr, aby hesla nešla matematicky předpovědět.
    * `string`: Poskytuje předdefinované konstanty pro abecedu a číslice, což zjednodušuje kód.
    * `datetime`: Pro získání a formátování aktuálního data a času vytvoření záznamu.
* **Datová struktura:** Využívá se lokální relační databáze ukládaná do souboru `hesla.db`. Hlavním prvkem je tabulka `historie` s následujícími sloupci:
    * `id`: Unikátní identifikátor (Auto-increment).
    * `heslo`: Samotný vygenerovaný textový řetězec.
    * `delka`: Celočíselná hodnota reprezentující počet znaků.
    * `cas`: Textové časové razítko ve formátu `YYYY-MM-DD HH:MM:SS`.
* **Algoritmus generování:** Pro tvorbu hesla je využit jednoduchý algoritmus spojující všechny povolené znaky do jednoho seznamu, ze kterého pak smyčka pomocí modulu `secrets` náhodně vybírá znak po znaku a skládá je do výsledného řetězce pomocí metody `.join()`.
