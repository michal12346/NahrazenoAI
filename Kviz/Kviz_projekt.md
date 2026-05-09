# Název projektu
Univerzální kvízová aplikace

# Popis a cíl projektu
Cílem projektu je vytvořit flexibilní vzdělávací nástroj v jazyce Python. Aplikace je navržena tak, aby dokázala kombinovat různé formáty testování (výběr z možností i otevřené otázky), čímž zvyšuje náročnost a interaktivitu pro uživatele.

# Popis funkcionality programu
Program po spuštění náhodně seřadí otázky z databáze. U každé položky systém rozpozná její typ:
1. U výběrových otázek nabídne možnosti a) b) c).
2. U otevřených otázek vyzve uživatele k přímému vepsání odpovědi.
Vstup od uživatele je automaticky očištěn o nadbytečné mezery a rozdíly ve velikosti písmen. Po každé odpovědi následuje okamžitá zpětná vazba. Na konci hry program vypočítá úspěšnost a nabídne uživateli možnost spustit test znovu s novým pořadím otázek.

# Technická část
* **Použité knihovny:** Využit modul `random` pro metodu `shuffle`, která zajišťuje náhodnost testu.
* **Algoritmy a řídící struktury:** * **Herní smyčka (while):** Zajišťuje plynulý chod a možnost restartu.
    * **Rozpoznávání typu (if-else):** Algoritmus uvnitř cyklu for mění chování programu (výpis možností vs. volný vstup) na základě metadat otázky.
    * **Zpracování textu:** Metody `.lower()` a `.strip()` pro eliminaci chyb uživatele při psaní.
* **Vlastní datové struktury:** Seznam (`list`) obsahující komplexní slovníky (`dict`). Každý slovník nese unikátní klíče (text, typ, spravne, moznosti), které definují chování dané otázky.
* **Volání externího API:** Aplikace je plně autonomní a nevyžaduje připojení k síti.
