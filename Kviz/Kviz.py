# Kviz - PÁTÁ VERZE

import random

def spustit_kviz():
    otazky = [
        {"text": "Jaké je hlavní město ČR?", "moznosti": "a) Brno  b) Praha  c) Ostrava", "spravne": "b", "typ": "volba"},
        {"text": "Napiš jméno prvního československého prezidenta:", "spravne": "Tomáš Garrigue Masaryk", "typ": "otevrena"},
        {"text": "Kolik je 5 + 5?", "moznosti": "a) 10  b) 12  c) 8", "spravne": "a", "typ": "volba"},
        {"text": "Jak se jmenuje naše galaxie?", "spravne": "Mléčná dráha", "typ": "otevrena"}
    ]

    random.shuffle(otazky)
    skore = 0
    
    # Cyklus projde zamíchané otázky bez ohledu na jejich typ
    for otazka in otazky:
        print(otazka["text"])
        if otazka["typ"] == "volba":
            print(otazka["moznosti"])
            odpoved = input("Tvoje volba (a/b/c): ")
        else:
            odpoved = input("Tvoje odpověď: ")

        if odpoved.lower().strip() == otazka["spravne"].lower().strip():
            print("Správně!\n")
            skore += 1
        else:
            print(f"Špatně! Správně bylo: {otazka['spravne']}\n")
    
    print(f"Konec! Tvé skóre: {skore} z {len(otazky)}")

if __name__ == "__main__":
    spustit_kviz()
