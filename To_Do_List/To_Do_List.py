# To Do List - DRUHA VERZE

aktivni_ukoly = []
# Nový seznam pro ukládání úkolů, které již byly splněny
historie_ukolu = []

def zobrazit_menu():
    print("\n--- To-Do List ---")
    print("1. Přidat úkol")
    print("2. Zobrazit úkoly")
    print("3. Dokončit úkol") # Nová možnost v menu
    print("0. Konec")

while True:
    zobrazit_menu()
    volba = input("Vyberte akci (0-3): ")

    if volba == '1':
        novy_ukol = input("Zadejte název úkolu: ")
        aktivni_ukoly.append(novy_ukol)
        print(f"Úkol '{novy_ukol}' byl úspěšně přidán.")
        
    elif volba == '2':
        print("\n--- Vaše aktivní úkoly ---")
        if len(aktivni_ukoly) == 0:
            print("Nemáte žádné aktivní úkoly.")
        else:
            for index, ukol in enumerate(aktivni_ukoly, 1):
                print(f"{index}. {ukol}")
                
    elif volba == '3':
        # Logika pro přesun úkolu z aktivních do historie
        if len(aktivni_ukoly) == 0:
            print("Nemáte žádné úkoly k dokončení.")
        else:
            cislo_ukolu = input("Zadejte číslo úkolu, který chcete dokončit: ")
            
            # Jednoduché ošetření, aby uživatel zadal číslo, které dává smysl
            if cislo_ukolu.isdigit():
                index = int(cislo_ukolu) - 1 # Převedení na index seznamu (počítá se od 0)
                
                # Kontrola, zda zadaný index existuje v seznamu aktivních úkolů
                if 0 <= index < len(aktivni_ukoly):
                    # Metoda pop() úkol vyjme ze seznamu a rovnou ho vrátí
                    dokonceny_ukol = aktivni_ukoly.pop(index)
                    historie_ukolu.append(dokonceny_ukol) # Přesun do historie
                    print(f"Výborně! Úkol '{dokonceny_ukol}' byl přesunut do historie.")
                else:
                    print("Úkol s tímto číslem neexistuje.")
            else:
                print("Prosím zadejte platné číslo.")
                
    elif volba == '0':
        print("Ukončuji program. Mějte hezký den!")
        break
    else:
        print("Neplatná volba, zkuste to znovu.")
        
