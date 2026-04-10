# Generator nahodných příběhů - FINÁLNÍ VERZE

# Importujeme vestavěnou knihovnu 'random', která nám umožní vybírat náhodné prvky
import random 

# Definujeme novou funkci s názvem 'vygeneruj_pribeh'. Funkce slouží k tomu, abychom kód mohli spouštět opakovaně.
def vygeneruj_pribeh():
    # Proměnné se seznamy slov (přesunuty dovnitř funkce, aby patřily přímo k ní)
    postavy = ["Rytíř", "Drak", "Princezna", "Čaroděj"]
    mista = ["v temném lese", "na starém hradě", "v kouzelné jeskyni", "na létajícím ostrově"]
    deje = ["našel skrytý poklad.", "bojoval se strašlivou nestvůrou.", "usnul hlubokým spánkem.", "objevil tajemný portál."]

    # Pomocí random.choice() vybereme náhodný prvek z každého seznamu
    vybrana_postava = random.choice(postavy)
    vybrane_misto = random.choice(mista)
    vybrany_dej = random.choice(deje)

    # Zde používáme takzvaný f-string (písmeno 'f' před uvozovkami). 
    # Umožňuje nám to vkládat proměnné přímo do textu pomocí složených závorek {}, což je čistší než sčítání pomocí +.
    sestaveny_pribeh = f"{vybrana_postava} {vybrane_misto} {vybrany_dej}"
    
    # Příkaz return ukončí funkci a vrátí nám hotový, spojený příběh, abychom s ním mohli dál pracovat.
    return sestaveny_pribeh

# Vytiskneme úvodní nadpis pro uživatele
print("--- Generátor náhodných příběhů ---")

# Vytvoříme cyklus 'for', který se opakuje přesně třikrát (range(3) znamená čísla 0, 1, 2)
for cislo in range(3):
    # Zavoláme naši funkci vygeneruj_pribeh() a to, co nám vrátí (return), uložíme do proměnné
    novy_pribeh = vygeneruj_pribeh()
    
    # Vytiskneme číslo příběhu (přičítáme +1, aby číslování nezačínalo od nuly) a samotný text příběhu
    print(f"Příběh {cislo + 1}: {novy_pribeh}")
