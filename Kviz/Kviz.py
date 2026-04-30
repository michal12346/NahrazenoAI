# Kviz - PRVNÍ VERZE

# Datová struktura (slovník) pro uložení otázek a správných odpovědí.
# Klíč je otázka, hodnota je odpověď.
otazky = {
    "Jaké je hlavní město ČR?": "Praha",
    "Kolik je 5 + 5?": "10"
}

# Cyklus, který projde všechny otázky ve slovníku.
# V této fázi se jen ptáme, ale zatím odpovědi nevyhodnocujeme.
for otazka in otazky:
    print(otazka)
    # Získání odpovědi od uživatele přes konzoli
    odpoved = input("Tvoje odpověď: ")
