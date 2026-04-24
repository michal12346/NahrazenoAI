# Dokumentace projektu

## Název projektu
Hra Kámen, nůžky, papír (Konzolová verze)

## Popis a cíl projektu
Tento projekt je jednoduchou implementací klasické hry "Kámen, nůžky, papír" určenou pro příkazovou řádku (konzoli). Cílem projektu je vytvořit interaktivní hru proti počítači, kde si uživatel může zahrát libovolný počet kol, dokud se sám nerozhodne aplikaci ukončit. Slouží k procvičení základních algoritmických konceptů v Pythonu.

## Popis funkcionality programu
Po spuštění programu je uživatel vyzván k zadání svého tahu (kámen, nůžky, nebo papír). Počítač si následně skrytě vygeneruje svůj vlastní tah. Program oba tahy porovná, vyhodnotí podle tradičních pravidel této hry (kámen tupí nůžky, nůžky stříhají papír, papír balí kámen) a vypíše výsledek kola (výhra, prohra, remíza). Program je navíc chráněn proti překlepům – pokud uživatel zadá neplatné slovo, je vyzván k novému zadání. Hra běží v opakující se smyčce, dokud uživatel nezadá slovo "konec".

## Technická část
* **Použitý jazyk:** Python 3
* **Použité knihovny:** * Standardní modul `random` - použit ke generování náhodného výběru počítače.
* **Vlastní datové struktury:** * Jednorozměrné pole (List) `moznosti` - ukládá řetězce (stringy) s povolenými herními tahy.
* **Algoritmy a logika:**
    * *Řízení toku programu:* Ošetřeno pomocí nekonečné smyčky `while True`, která využívá řídící příkazy `break` (pro bezpečné ukončení hry) a `continue` (pro zachycení a opakování neplatného vstupu uživatele).
    * *Rozhodovací strom:* Vyhodnocení vítěze je řešeno pomocí vícenásobného větvení `if-elif-else`. Pravidla pro výhru hráče jsou sloučena do jedné sdružené podmínky pomocí logického operátoru `or`, což snižuje duplicitu kódu.
