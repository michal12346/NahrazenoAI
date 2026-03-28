# To Do List - FINALNÍ VERZE

# --- PŘÍPRAVA DAT ---
aktivni_ukoly = []   # Vytvořím prázdný seznam (krabici) pro úkoly, co musím udělat
historie_ukolu = []  # Vytvořím druhý seznam pro úkoly, které už jsou hotové

# --- DEFINICE FUNKCÍ ---
def zobrazit_menu(): # Definuji funkci (balíček příkazů) s názvem 'zobrazit_menu'
    print("\n--- To-Do List ---") # Vypíše nadpis ( \n udělá prázdný řádek nad ním )
    print("1. Přidat úkol")       # Vypíše možnosti, které uživatel má
    print("2. Zobrazit úkoly")
    print("3. Dokončit úkol")
    print("4. Zobrazit historii")
    print("0. Konec")

# --- HLAVNÍ ČÁST PROGRAMU ---
while True: # Spustím nekonečnou smyčku - program poběží stále dokola
    zobrazit_menu() # Zavolám funkci nahoře, aby se uživateli ukázalo menu
    
    # input() zastaví program a čeká, až uživatel něco napíše a potvrdí Enterem
    volba = input("Vyberte akci (0-4): ") 

    if volba == '1': # POKUD uživatel napsal jedničku:
        novy_ukol = input("Zadejte název úkolu: ") # Zeptám se na název úkolu
        aktivni_ukoly.append(novy_ukol) # .append přidá ten text na konec seznamu
        print(f"Úkol '{novy_ukol}' byl přidán.") # f-string vloží název úkolu do věty

    elif volba == '2': # JINAK POKUD uživatel napsal dvojku:
        print("\n--- Vaše aktivní úkoly ---")
        if len(aktivni_ukoly) == 0: # len() zjišťuje délku. Pokud je 0, je prázdno
            print("Nemáte žádné aktivní úkoly.")
        else: # V opačném případě (pokud tam nějaké úkoly jsou):
            # enumerate projde seznam a ke každé věci (ukol) přidá číslo (index)
            for index, ukol in enumerate(aktivni_ukoly, 1): 
                print(f"{index}. {ukol}") # Vypíše úkol i s jeho číslem

    elif volba == '3': # JINAK POKUD uživatel napsal trojku (dokončení):
        if len(aktivni_ukoly) == 0: # Kontrola, jestli je vůbec co dokončovat
            print("Nemáte žádné úkoly k dokončení.")
        else:
            cislo_ukolu = input("Zadejte číslo úkolu: ") # Uživatel napíše číslo
            if cislo_ukolu.isdigit(): # Kontrola, jestli uživatel nezadal písmeno
                # int() změní text "1" na číslo 1. Odečteme 1, protože Python počítá od 0
                index = int(cislo_ukolu) - 1 
                
                # Kontrola, jestli zadané číslo není mimo rozsah seznamu
                if 0 <= index < len(aktivni_ukoly):
                    # .pop(index) vyjme úkol ze seznamu a uloží ho do proměnné
                    dokonceny_ukol = aktivni_ukoly.pop(index)
                    # .append ho pak vloží do druhého seznamu (historie)
                    historie_ukolu.append(dokonceny_ukol)
                    print(f"Hotovo! Úkol '{dokonceny_ukol}' je v historii.")
                else:
                    print("Takové číslo úkolu v seznamu není.")

    elif volba == '4': # JINAK POKUD uživatel napsal čtyřku:
        print("\n--- Historie úkolů ---")
        if len(historie_ukolu) == 0:
            print("Zatím jste nic nedokončili.")
        else:
            for index, ukol in enumerate(historie_ukolu, 1): # Vypíše historii
                print(f"{index}. [HOTOVO] {ukol}")

    elif volba == '0': # JINAK POKUD uživatel napsal nulu:
        print("Ukončuji program...")
        break # Příkaz break „rozbije“ smyčku while True a program skončí

    else: # JINAK (pokud uživatel napsal cokoliv jiného, co není v menu):
        print("Neplatná volba, zkuste to znovu.")
