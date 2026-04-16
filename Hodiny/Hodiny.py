# Hodiny - DRUHÁ VERZE

# Importujeme knihovnu time pro práci s časem a pozastavení programu
import time

# Začátek logicky složitější části: Nekonečná smyčka 'while'
# Podmínka 'True' znamená, že smyčka poběží donekonečna, dokud program natvrdo nevypneme
while True:
    # Získáme aktuální čas v každém průběhu smyčky
    aktualni_cas = time.strftime("%H:%M:%S")
    
    # Vypíšeme nový čas na nový řádek v konzoli
    print("Aktuální čas:", aktualni_cas)
    
    # Funkce sleep() uspí program přesně na 1 vteřinu
    # Děláme to proto, aby nám to nezahltilo počítač a čas se měnil po vteřinách
    time.sleep(1)
