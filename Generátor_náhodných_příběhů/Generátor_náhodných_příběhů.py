# Generator nahodných příběhů - DRUHÁ VERZE

# Importujeme vestavěnou knihovnu 'random', která nám umožní vybírat náhodné prvky
import random 

# Vytvoření proměnné 'postavy', do které uložíme seznam (list) textových řetězců (jmen postav)
postavy = ["Rytíř", "Drak", "Princezna", "Čaroděj"]

# Vytvoření proměnné 'mista', do které uložíme seznam různých lokací
mista = ["v temném lese", "na starém hradě", "v kouzelné jeskyni", "na létajícím ostrově"]

# Vytvoření proměnné 'deje', do které uložíme seznam činností, které postavy dělají
deje = ["našel skrytý poklad.", "bojoval se strašlivou nestvůrou.", "usnul hlubokým spánkem.", "objevil tajemný portál."]

# Funkce random.choice() vezme náš seznam 'postavy' a vybere z něj jeden náhodný prvek, ten uloží do nové proměnné
vybrana_postava = random.choice(postavy)

# To samé uděláme pro místo
vybrane_misto = random.choice(mista)

# A to samé uděláme pro děj
vybrany_dej = random.choice(deje)

# Spojíme vybraná slova dohromady pomocí znaménka plus (+). 
# Přidáváme mezi ně i prázdné mezery v uvozovkách (" "), aby slova nebyla nalepená na sobě.
pribeh = vybrana_postava + " " + vybrane_misto + " " + vybrany_dej

# Vypíšeme výsledný příběh do konzole (na obrazovku)
print(pribeh)
