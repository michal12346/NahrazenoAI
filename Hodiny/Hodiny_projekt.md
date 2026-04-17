**Název projektu:** Konzolové digitální hodiny

**Popis a cíl projektu:** Cílem tohoto projektu bylo vytvořit jednoduchý program v jazyce Python, který simuluje digitální hodiny přímo v příkazovém řádku (terminálu). Cílem bylo osvojit si základy programování, konkrétně tvorbu funkcí, práci s nekonečnými smyčkami a interakci se systémem.

**Popis funkcionality programu:** Program po spuštění okamžitě začne zobrazovat aktuální systémový čas ve formátu Hodiny:Minuty:Sekundy. Aby hodiny fungovaly vizuálně správně, program každou vteřinu vymaže obsah konzole a vypíše nový čas. Díky tomu se čas plynule přepisuje na jednom místě. Program běží nepřetržitě, dokud jej uživatel manuálně neukončí (např. klávesovou zkratkou Ctrl+C).

**Technická část:**
* **Použité knihovny:** * `time`: Byla použita standardní knihovna pro získání aktuálního času (pomocí `strftime`) a pro časovou prodlevu (pomocí `sleep`), která zajišťuje obnovování přesně po jedné vteřině.
  * `os`: Slouží pro detekci operačního systému a odeslání systémového příkazu k promazání obrazovky (`cls` nebo `clear`).
* **Algoritmy:** Jádrem programu je nekonečná smyčka `while True`, která neustále opakuje 4 kroky: smazání konzole, načtení času, výpis na obrazovku a uspání programu na 1 sekundu.
* **Vlastní datové struktury / API:** Program je koncipován jako jednoduchý skript pro začátečníky, nevyužívá složité datové struktury ani nevolá externí API (funguje zcela offline se systémovým časem zařízení).
