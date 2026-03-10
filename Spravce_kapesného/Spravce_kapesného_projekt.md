# Dokumentace k projektu: Správce kapesného

## Uživatelská příručka (User Guide)
Tento program slouží k jednoduchému hlídání vašich výdajů. 

**Jak program používat:**
1. Po spuštění zadejte, kolik máte celkem peněz a jaký je váš týdenní limit.
2. Postupně zadávejte částky, které jste utratili za jídlo, zábavu a ostatní věci.
3. Program vám vypočítá, kolik vám zbývá, a upozorní vás, pokud jste překročili limit.
4. Na konci se vás program zeptá, zda chcete zadávat data znovu (napište "ano"), nebo skončit.

## Technický popis
Program je napsaný v jazyce Python. 

**Struktura:**
* **Vstupy:** Používám funkci `input()` s přetypováním na `float`, aby uživatel mohl zadávat i desetinná čísla.
* **Logika:** Hlavní část tvoří cyklus `while`, který umožňuje opakované spouštění programu bez restartu. 
* **Podmínky:** Pomocí `if-elif-else` program vyhodnocuje, v jakém stavu je peněženka uživatele.
* **Výpočty:** Program provádí základní matematické operace jako sčítání a odčítání pro zjištění zůstatku.
