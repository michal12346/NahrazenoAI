# Dokumentace: Generátor náhodných příběhů

**Název projektu:** Generátor náhodných příběhů (Random Story Generator)

**Popis a cíl projektu:**
Jedná se o jednoduchou konzolovou aplikaci naprogramovanou v jazyce Python. Cílem projektu je pobavit uživatele generováním nesmyslných nebo vtipných situací a z hlediska vývoje procvičit základní programátorské koncepty (práce s poli, import knihoven, tvorba funkcí a používání cyklů).

**Popis funkcionality programu:**
Po spuštění skriptu program bez nutnosti dalšího uživatelského vstupu automaticky sestaví a vypíše do konzole tři krátké příběhy. Každý příběh je tvořen jednou větou. Program náhodně vybírá a spojuje tři části: hlavní postavu, místo děje a vykonanou akci. Výsledkem jsou pokaždé unikátní kombinace (např. "Drak na létajícím ostrově usnul hlubokým spánkem.").

**Technická část:**
* **Programovací jazyk:** Python 3
* **Použité knihovny:** `random` (standardní vestavěná knihovna Pythonu). Využívá se specificky metoda `random.choice()` pro pseudo-náhodný výběr jednoho prvku z dodané kolekce.
* **Datové struktury:** Pro uchovávání dat (slov) se využívají standardní jednorozměrná pole, v Pythonu nazývaná seznamy (`list`).
* **Algoritmy a logika:** Kód je strukturován procedurálně a zapouzdřen do vlastní funkce `vygeneruj_pribeh()`. Pro formátování textového výstupu jsou použity tzv. f-stringy (formátované řetězce). Pro generování více příběhů po sobě je využit iterační cyklus `for`.
