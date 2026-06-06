# Dokumentace k projektu: Parádní Multi-Kvíz

## 1. Úvodní informace
**Parádní Multi-Kvíz** je interaktivní konzolová hra naprogramovaná v jazyce Python. Hráčům nabízí možnost otestovat své znalosti v různých kategoriích a typech otázek. Program je navržen tak, aby byl uživatelsky přívětivý, obsahoval herní mechaniky (životy) a pamatoval si historicky nejlepší výsledek hráče.

---

## 2. Herní mechaniky a funkce

Program nabízí následující klíčové vlastnosti:

* **Bohatá databáze otázek:** Hra aktuálně operuje s databází 30 různých otázek, aby bylo každé spuštění pestré a výzva byla reálná.
* **Výběr kategorií:** Hráč si na začátku volí ze tří tematických okruhů (1. Geografie, 2. Věda a technika, 3. Rychlovky). Program vyfiltruje a nabídne z každé sekce 10 otázek.
* **Tři typy otázek:**
    * **Výběrové (volba):** Hráč vybírá z možností a), b), c). Možnosti se při každém spuštění náhodně míchají.
    * **Otevřené:** Hráč musí přímo napsat přesný text odpovědi (systém je ovšem benevolentní k velikosti písmen).
    * **Časovky:** Speciální otázky s pevným časovým limitem (zpravidla 10 sekund). Pokud hráč neodpoví včas, ztrácí bod i život.
* **Systém životů (Game Over mechanika):** Hráč začíná každé kolo se 3 životy (reprezentovanými symboly ❤️). Za každou špatnou odpověď nebo vypršení časového limitu ztrácí jeden život. Jakmile životy klesnou na nulu, hra okamžitě končí.
* **Nekonečná smyčka:** Po dokončení (nebo prohře) se program hráče zeptá, zda chce hrát znovu. Hra běží, dokud ji hráč sám neukončí.

---

## 3. Technické řešení

Kód je napsán s ohledem na čitelnost a je plně okomentován. Využívá základní struktury jazyka Python:

### Použité moduly
* `import random`: Využito pro náhodné míchání pořadí otázek i samotných odpovědí (možností) u výběrových otázek pomocí funkce `random.shuffle()`.
* `import time`: Využito pro logiku časovek. Zaznamenává se čas před odesláním odpovědi (`time.time()`) a po něm. Rozdíl těchto hodnot určuje uplynulý čas.

### Struktura dat
Všechny otázky jsou uloženy v jednom hlavním **seznamu** (List). Každá z 30 položek je reprezentována jako **slovník** (Dictionary) s klíči jako `"text"`, `"spravne"`, `"typ"` a `"kategorie"`. Díky této modulární struktuře lze další stovky otázek přidávat bez nutnosti měnit aplikační logiku programu.

### Práce se soubory a výjimky (I/O)
Program umí trvale ukládat nejlepší skóre (osobní rekord), aby data přežila i vypnutí aplikace:
* **Čtení:** Na začátku hry se program pomocí chráněného bloku `try-except` pokusí otevřít textový soubor `rekord.txt` v režimu čtení (`r`). Pokud soubor neexistuje, program nespadne, ale výjimka `FileNotFoundError` tuto situaci odchytí a nastaví rekord na hodnotu `0`.
* **Zápis:** Pokud hráč na konci kola překoná historický rekord, program otevře soubor `rekord.txt` v režimu zápisu (`w`) a novou hodnotu do něj uloží (přepíše tu starou).

---

## 4. Spuštění programu

**Požadavky:** Nainstalovaný Python verze 3.x.

1.  Otevři příkazový řádek (Terminál / CMD).
2.  Pomocí příkazu `cd` se přesuň do složky, kde je projekt uložen.
3.  Zadej příkaz:
    ```bash
    python kviz.py
    ```
4.  Dále už jen postupuj podle instrukcí na obrazovce.

---
*Vytvořeno jako projekt pro pochopení základů programování, kolekcí a práce s daty v Pythonu.*
