# Dokumentace projektu: Simulátor zásobování skladu

Popis a cíl projektu:
Tato aplikace slouží k jednoduché správě a sledování zásob ve skladu. Cílem je pomoci uživateli udržet přehled o aktuálním množství zboží a včas ho varovat, pokud zásoby klesnou pod kritickou hranici.

# Jak program používat:

Spuštění: Po spuštění programu uvidíte aktuální stav zásob na začátku dne.

Zadávání dat: Program vás postupně vyzve k zadání počtu prodaných kusů pro každý produkt. Zadávejte pouze celá čísla.

Vyhodnocení: Po zadání prodejů program automaticky vypočítá nový stav skladu a zobrazí varování, pokud je zboží nedostatek.

Opakování: Pokud chcete pokračovat dalším dnem, napište ano. Pokud chcete program ukončit, napište ne.

Funkcionalita programu:
Aplikace běží v nekonečné smyčce, dokud uživatel nerozhodne o jejím ukončení. Využívá proměnné pro uchování stavu zásob napříč jednotlivými dny (cykly).

# Technická část:

Algoritmus kontroly záporných hodnot: Program využívá matematickou funkci max(0, vypocet). To zaručuje, že i když uživatel zadá větší prodej, než je aktuálně na skladě, výsledný stav zůstane na nule a nepůjde do nesmyslných záporných čísel.

Logické větvení (Větvení): * Používá operátor and pro detekci totálního nedostatku zboží (kritický stav u obou položek).

Používá operátor or pro varování v případě, že dochází alespoň jeden typ produktu.

Datové struktury: Program pracuje s celočíselnými proměnnými (int) a řetězci (string) pro řízení smyčky.

Vstupy a výstupy: Využívá standardní funkci input() s přetypováním na čísla a formátované řetězce f-strings pro přehledný výpis v konzoli.
