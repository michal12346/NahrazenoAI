# Název projektu
Kvízová aplikace v Pythonu

# Popis a cíl projektu
Jedná se o jednoduchou konzolovou aplikaci. Cílem projektu je vytvořit interaktivní hru, která otestuje znalosti uživatele v různých odvětvích (geografie, matematika, astronomie). Projekt slouží jako ukázka základní práce se vstupy uživatele, cykly a podmínkami.

# Popis funkcionality programu
Program po spuštění postupně vypisuje na obrazovku předem definované otázky. Po každé otázce program čeká, až uživatel z klávesnice zadá svou odpověď a potvrdí ji klávesou Enter. Aplikace následně odpověď vyhodnotí (přičemž ignoruje velikost písmen a zbytečné mezery, aby bylo hodnocení spravedlivé) a informuje uživatele, zda odpověděl správně, či nikoliv. Pokud uživatel chybuje, program mu vypíše správnou odpověď. Na konci kvízu se zobrazí celkové skóre – počet správných odpovědí z celkového počtu otázek.

# Technická část
* **Použité knihovny:** Program nevyužívá žádné externí knihovny, je napsán v čistém Pythonu pomocí standardní knihovny.
* **Algoritmy a řídící struktury:** Základem logiky je iterativní procházení dat (cyklus `for`) a kontrolní struktura větvení (podmínky `if-else`) pro vyhodnocení správnosti uživatelského vstupu vůči uloženým datům.
* **Vlastní datové struktury:** Pro uložení otázek a k nim přiřazených odpovědí je využita vestavěná datová struktura typu slovník (`dict`). Klíčem (key) je text otázky a hodnotou (value) je správná odpověď ve formátu textového řetězce (`String`).
* **Volání externího API:** Aplikace běží zcela offline a nekomunikuje s žádným externím API.
