# Program na hlidani penez - 1 verze
print("-----------------------------------------")
print("Vitejte v programu Spravce kapesneho")
print("-----------------------------------------")

# Tady si nastavim kolik mam penez na zacatku
nasetreno = float(input("Zadej, kolik mas celkem penez: "))
limit = float(input("Zadej svuj tydenni limit na utratu: "))

# Seznam vydaju - zatim jen tri polozky at to neni slozity
print("Zadej nyni svoje posledni tri nakupy:")
jidlo = float(input("1. Kolik jsi dal za jidlo: "))
zabava = float(input("2. Kolik jsi dal za zabavu: "))
ostatni = float(input("3. Kolik jsi dal za ostatni veci: "))

# Zakladni vypocet celkove utraty
celkova_utrata = jidlo + zabava + ostatni

print("-----------------------------------------")
print("Zadal jsi vsechny udaje.")
print("Tvoje aktualni utrata je zatim:", celkova_utrata)
print("V penezence ti zbyva:", nasetreno - celkova_utrata)
print("-----------------------------------------")