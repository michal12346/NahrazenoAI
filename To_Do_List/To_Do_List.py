# To Do List - PRVNÍ VERZE

# Hlavní seznam pro ukládání aktivních úkolů
aktivni_ukoly = []

def zobrazit_menu():
    # Funkce pro vypsání uživatelského rozhraní do konzole
    print("\n--- To-Do List ---")
    print("1. Přidat úkol")
    print("2. Zobrazit úkoly")
    print("0. Konec")

# Hlavní smyčka programu, která běží, dokud ji uživatel neukončí volbou 0
while True:
    zobrazit_menu()
    volba = input("Vyberte akci (0-2): ")

    if volba == '1':
        novy_ukol = input("Zadejte název úkolu: ")
        # Přidání položky na konec seznamu
        aktivni_ukoly.append(novy_ukol)
        print(f"Úkol '{novy_ukol}' byl úspěšně přidán.")
        
    elif volba == '2':
        print("\n--- Vaše aktivní úkoly ---")
        # Pokud je seznam prázdný, upozorníme uživatele
        if len(aktivni_ukoly) == 0:
            print("Nemáte žádné aktivní úkoly.")
        else:
            # Cyklus projde všechny úkoly a vypíše je s jejich pořadovým číslem
            # enumerate počítá od 1, aby to bylo pro uživatele přirozenější
            for index, ukol in enumerate(aktivni_ukoly, 1):
                print(f"{index}. {ukol}")
                
    elif volba == '0':
        print("Ukončuji program. Mějte hezký den!")
        break # Příkaz break ukončí hlavní smyčku a tím i program
        
    else:
        print("Neplatná volba, zkuste to znovu.")