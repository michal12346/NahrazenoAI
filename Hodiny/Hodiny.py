# Hodiny - PRVNÍ VERZE

# Importujeme knihovnu time, která v Pythonu slouží k práci s časem
import time

# Získáme aktuální čas a zformátujeme ho
# %H znamená hodiny, %M minuty a %S sekundy
aktualni_cas = time.strftime("%H:%M:%S")

# Jednoduše vypíšeme získaný čas do konzole
print("Aktuální čas:", aktualni_cas)
