# Generator hesel - FINALNÍ VERZE

import sqlite3  # práce s databází SQLite (soubor .db)
import secrets  # kryptograficky bezpečný náhodný výběr
import string   # předdefinované sady znaků (písmena, číslice)
from datetime import datetime  # datum a čas


# Automatické vytvoření databáze a tabulky
def init_db():
    # otevře (nebo vytvoří) soubor databáze hesla.db
    conn = sqlite3.connect("hesla.db")
    cursor = conn.cursor()  # kurzor pro spouštění SQL příkazů

    # vytvoří tabulku "historie", pokud neexistuje
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS historie (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        heslo TEXT NOT NULL,
        delka INTEGER,
        cas TEXT
    )
    """)

    conn.commit()  # uloží změny do databáze
    conn.close()   # zavře spojení


# Generátor hesla
def generate_password(length):
    # sestaví sadu znaků, ze které bude heslo náhodně vybíráno
    chars = string.ascii_letters + string.digits + "!@#$%^&*_-+"

    # vrátí řetězec délky `length`, každý znak je náhodně vybraný
    return "".join(secrets.choice(chars) for _ in range(length))


# Uložení hesla do databáze
def save_password(password):
    conn = sqlite3.connect("hesla.db")  # otevře databázi
    cursor = conn.cursor()

    # vytvoří časový řetězec v podobě "YYYY-MM-DD HH:MM:SS"
    cas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # vloží nový řádek do tabulky historie
    cursor.execute(
        "INSERT INTO historie (heslo, delka, cas) VALUES (?, ?, ?)",
        (password, len(password), cas)
    )

    conn.commit()  # uloží změny
    conn.close()   # zavře spojení


# Načtení historie
def show_history():
    conn = sqlite3.connect("hesla.db")  # otevře databázi
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM historie")  # načte všechna data
    data = cursor.fetchall()  # přečte všechny řádky výsledku

    conn.close()  # zavře spojení
    return data  # vrátí seznam záznamů


# Hlavní program
init_db()  # automaticky vytvoří databázi a tabulku

# vygeneruje heslo délky 16 znaků
heslo = generate_password(16)
print("Vygenerované heslo:", heslo)

# uloží heslo do databáze
save_password(heslo)

# vypíše historii všech uložených hesel
print("\nHistorie hesel:")
for row in show_history():
    print(row)
