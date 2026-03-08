# Program na hlidani penez - 2 verze (pridana logika)
nasetreno = float(input("Zadej, kolik mas celkem penez: "))
limit = float(input("Zadej svuj tydenni limit na utratu: "))

print("Zadej nyni svoje posledni tri nakupy:")
jidlo = float(input("1. Kolik jsi dal za jidlo: "))
zabava = float(input("2. Kolik jsi dal za zabavu: "))
ostatni = float(input("3. Kolik jsi dal za ostatni veci: "))

celkova_utrata = jidlo + zabava + ostatni
zbytek = nasetreno - celkova_utrata

# Tady kontroluju jestli uzivatel neni v minusu
if zbytek < 0:
    print("POZOR: Jsi v minusu! Musis vic setrit.")
    print("Chybi ti presne:", abs(zbytek), "Kc.")
else:
    print("Jsi v pohode, jeste mas:", zbytek, "Kc.")

# Vypocet prumeru na jednu polozku
prumer = celkova_utrata / 3
print("Prumerne za jednu vec utratis:", prumer)

# Kontrola tydenniho limitu
if celkova_utrata > limit:
    print("VAROVANI: Prekrocil jsi svuj tydenni limit!")
else:
    print("Limit jsi neprekrocil.")
