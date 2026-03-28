# Dokumentace: To-Do List s historií

**Název projektu:**
Konzolový To-Do list (Správce úkolů) s evidencí historie.

**Popis a cíl projektu:**
Jedná se o jednoduchou konzolovou aplikaci vytvořenou v jazyce Python. Cílem projektu je poskytnout uživateli snadný nástroj pro organizaci denních úkolů. Aplikace umožňuje nejen plánovat, co je potřeba udělat, ale také motivuje uživatele tím, že ukládá již splněné úkoly do dohledatelné historie.

**Popis funkcionality programu:**
Program funguje jako textové menu, kde uživatel vybírá akce zadáním příslušného čísla:
1.  **Přidat úkol:** Uživatel zadá text úkolu, který se uloží do aktivního seznamu.
2.  **Zobrazit úkoly:** Vypíše všechny aktuálně nesplněné úkoly očíslované od jedničky.
3.  **Dokončit úkol:** Uživatel vybere podle čísla úkol, který splnil. Program jej odstraní z aktivních úkolů a přesune do historie.
4.  **Zobrazit historii:** Vypíše seznam všech úkolů, které již uživatel dokončil.
5.  **Konec:** Bezpečně ukončí běh celého programu.

**Technická část:**
* **Použité knihovny:** Aplikace nevyužívá žádné externí moduly ani knihovny, využívá čistě základní (built-in) funkce jazyka Python.
* **Algoritmy:** K běhu programu slouží základní nekonečná smyčka `while True`, jejíhož řízení je dosaženo pomocí bloku podmíněných příkazů `if/elif/else`. Větvení slouží jako routování akcí na základě vstupu (`input()`).
* **Vlastní datové struktury:** Pro uchování stavu programu jsou použita dvě nezávislá jednorozměrná pole (datový typ `list`). Proměnná `aktivni_ukoly` slouží jako fronta pro stávající agendu, zatímco `historie_ukolu` archivuje smazaná data pomocí metod `.append()` a `.pop()`. Ke snadnému číslování a čtení obsahu seznamů je využita vestavěná funkce `enumerate()`.
