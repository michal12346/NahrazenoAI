# Název projektu
Simulátor dopravy ve městě

# Popis a cíl projektu
Tento projekt je jednoduchý konzolový program pro sledování provozu na městské křižovatce. Cílem projektu je vytvořit nástroj, který uživateli umožní průběžně zadávat počty vozidel a na základě těchto dat uživatele včas varovat před vznikem dopravní zácpy.

# Popis funkcionality programu
Program běží v cyklu a opakovaně se uživatele ptá na počet aut a autobusů, které právě projely. Na základě zadaných čísel okamžitě vyhodnotí situaci – autobus přitom křižovatku zatěžuje více než osobní auto. Pokud je celkové zatížení vysoké, program vypíše varování. Uživatel může simulaci kdykoliv ukončit zadáním slova "konec". Po ukončení se zobrazí finální statistiky (celkový počet vozidel a průměr aut na jedno měření).

# Technická část
* **Použité knihovny:** Program využívá pouze čistý Python bez externích a standardních knihoven.
* **Datové struktury:** Pro ukládání stavu jsou použity pouze základní celočíselné proměnné (`int`) a textové řetězce (`str`).
* **Algoritmy:** * Hlavní logika běží v nekonečné smyčce (`while True`), která je v případě potřeby ukončena příkazem `break`.
  * Algoritmus pro vyhodnocení zácpy používá vážený součet (auto = 1, autobus = 3) a následné podmíněné větvení (`if/else`).
  * Program obsahuje ochrannou podmínku proti dělení nulou při závěrečném výpočtu průměru.
