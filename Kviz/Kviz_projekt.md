# Název projektu
Univerzální kvízová aplikace s časomírou

# Popis a cíl projektu
Cílem projektu je vytvořit flexibilní vzdělávací nástroj v jazyce Python. Aplikace dokáže kombinovat různé formáty testování: výběr z možností, otevřené otázky a stresové otázky s časovým limitem (tzv. rychlovky). Tím se výrazně zvyšuje náročnost a interaktivita pro uživatele.

# Popis funkcionality programu
Program po spuštění náhodně seřadí 15 otázek z databáze. U každé položky systém rozpozná její typ:
1. U výběrových otázek nabídne možnosti a) b) c).
2. U otevřených otázek vyzve uživatele k přímému vepsání odpovědi.
3. U časovek ("rychlovek") program zmáčky aktuální čas před a po zadání odpovědi. Pokud uživatel překročí limit (např. 10 sekund), odpověď se bere jako špatná bez ohledu na zadaný text.
Vstup od uživatele je automaticky očištěn o nadbytečné mezery a rozdíly ve velikosti písmen. Po každé odpovědi následuje okamžitá zpětná vazba. Na konci hry program vypočítá úspěšnost a nabídne uživateli možnost spustit test znovu s novým pořadím otázek.

# Technická část
* **Použité knihovny:** * Využit modul `random` pro metodu `shuffle`, která zajišťuje náhodnost testu.
  * Využit modul `time` pro funkci `time.time()`, která měří dobu reakce uživatele u časovek.
* **Algoritmy a řídící struktury:** * **Herní smyčka (while):** Zajišťuje plynulý chod a možnost restartu.
  * **Příkaz continue:** Použit u časových otázek k okamžitému přeskočení vyhodnocení, pokud vypršel čas.
  * **Rozpoznávání typu (if-elif-else):** Algoritmus uvnitř cyklu for mění chování programu na základě metadat otázky.
  * **Zpracování textu a proměnných:** Metody `.lower()` a `.strip()` pro eliminaci chyb a zaokrouhlování času pomocí f-stringů (`{promenna:.1f}`).
* **Vlastní datové struktury:** Seznam (`list`) obsahující komplexní slovníky (`dict`). Každý slovník nese unikátní klíče (text, typ, spravne, moznosti, limit).
* **Volání externího API:** Aplikace je plně autonomní a nevyžaduje připojení k síti.
