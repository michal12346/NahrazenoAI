# Generator hesel - 2 VERZE 

import sqlite3  # Importuje knihovnu pro práci s SQL databází
import secrets  # Importuje modul pro kryptograficky bezpečnou náhodu
import string   # Importuje předdefinované sady znaků (písmena, čísla)
from datetime import datetime  # Importuje nástroj pro práci s aktuálním časem

# FUNKCE PRO PŘÍPRAVU DATABÁZE
def init_db():
    conn = sqlite3.connect("hesla.db")  # Připojí se k souboru hesla.db (vytvoří ho, pokud není)
    cursor = conn.cursor()  # Vytvoří kurzor, který provádí SQL příkazy

    # Spustí příkaz pro vytvoření tabulky historie, pokud v souboru ještě neexistuje
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS historie (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  # Unikátní číslo pro každý řádek (1, 2, 3...)
        heslo TEXT NOT NULL,                  # Sloupec pro uložení samotného hesla
        delka INTEGER,                        # Sloupec pro uložení délky hesla
        cas TEXT                              # Sloupec pro uložení času vytvoření
    )
    """)

    conn.commit()  # Potvrdí a fyzicky zapíše změny do databázového souboru
    conn.close()   # Uzavře spojení s databází, aby se uvolnily prostředky systému


# FUNKCE PRO GENEROVÁNÍ HESLA
def generate_password(length=12):
    # Definice povolených znaků: malá + velká písmena + čísla + vybrané symboly
    chars = string.ascii_letters + string.digits + "!@#$%^&*_-+"
    # Náhodně vybere 'length' znaků z 'chars' a spojí (join) je do jednoho textu
    return "".join(secrets.choice(chars) for _ in range(length))


# FUNKCE PRO ULOŽENÍ HESLA
def save_password(password):
    conn = sqlite3.connect("hesla.db")  # Otevře spojení s databází
    cursor = conn.cursor()  # Připraví kurzor pro zápis dat

    # Zjistí aktuální čas a převede ho na čitelný textový formát
    cas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Vloží (INSERT) nové heslo, jeho délku a čas do připravených sloupců v tabulce
    cursor.execute(
        "INSERT INTO historie (heslo, delka, cas) VALUES (?, ?, ?)",
        (password, len(password), cas)  # Hodnoty, které nahradí otazníky v SQL dotazu
    )

    conn.commit()  # Uloží provedené změny (vložení dat) do souboru
    conn.close()   # Ukončí spojení s databází


# HLAVNÍ SPOUŠTĚCÍ ČÁST PROGRAMU
init_db()  # Nejdříve spustíme přípravu databáze (vytvoření tabulky)

# Vygeneruje náhodné heslo o délce 16 znaků a uloží ho do proměnné
heslo = generate_password(16)
print("Vygenerované heslo:", heslo)  # Zobrazí vygenerované heslo na obrazovce

# Vezme vygenerované heslo a pošle ho do funkce pro trvalé uložení do databáze
save_password(heslo)
