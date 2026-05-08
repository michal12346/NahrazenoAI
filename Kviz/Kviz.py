# Kviz - ČTVRTÁ VERZE

def spustit_kviz():
    # Seznam nyní obsahuje klíč "typ", podle kterého program pozná, jak se má ptát.
    # Pokud je typ "volba", vypíše možnosti. Pokud "otevrena", jen se zeptá.
    otazky = [
        {"text": "Jaké je hlavní město ČR?", "moznosti": "a) Brno  b) Praha  c) Ostrava", "spravne": "b", "typ": "volba"},
        {"text": "Napiš jméno prvního československého prezidenta:", "spravne": "Tomáš Garrigue Masaryk", "typ": "otevrena"}
    ]

    for otazka in otazky:
        print(otazka["text"])
        
        # Podmínka kontroluje typ otázky. Pokud je to volba, zobrazí možnosti.
        if otazka["typ"] == "volba":
            print(otazka["moznosti"])
            odpoved = input("Tvoje volba (a/b/c): ")
        else:
            # U otevřené otázky možnosti nejsou, rovnou čekáme na text.
            odpoved = input("Tvoje odpověď: ")

        # Vyhodnocení zůstává podobné, díky .lower() a .strip()
        if odpoved.lower().strip() == otazka["spravne"].lower().strip():
            print("Správně!\n")
        else:
            print(f"Špatně! Správně bylo: {otazka['spravne']}\n")

if __name__ == "__main__":
    spustit_kviz()
