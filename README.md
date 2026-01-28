# Dataanalys – Köksglädje

## Beskrivning
Detta projekt är en individuell inlämning inom data science. Syftet med projektet
är att analysera försäljningsdata från Köksglädje med hjälp av Python, Pandas och
Matplotlib, samt att presentera analysen i en Jupyter Notebook.

Projektet fokuserar på att visa hur data kan läsas in, bearbetas och visualiseras
för att skapa insikter om försäljning.

---

## Datakälla
Datan som används i projektet kommer från en SQLite-databas:
- `köksglädje_copy.db`

Databasen innehåller information om försäljningstransaktioner, inklusive datum,
butik, stad och totalt försäljningsbelopp.

---

## Analys
Analysen genomförs i en Jupyter Notebook och omfattar bland annat:

- Inläsning av data från SQLite-databasen
- Databearbetning med Pandas
- Visualisering av försäljning med Matplotlib
- Analys av:
  - Försäljning per stad
  - Försäljning per veckodag
  - Försäljning över tid (trendanalys)

Eftersom datamängden är begränsad innehåller analysen även reflektioner kring
datans begränsningar och hur analysmetoderna kan användas på större dataset.

---

## Struktur
Projektet innehåller följande viktiga filer:

- `visualiseringar.ipynb` – Notebook med hela analysen
- `köksglädje_copy.db` – SQLite-databas med försäljningsdata
- `README.md` – Projektbeskrivning

---

## Kör projektet
1. Klona repot eller ladda ner filerna.
2. Säkerställ att Python och nödvändiga bibliotek är installerade:
   - pandas
   - matplotlib
   - sqlite3
3. Öppna `visualiseringar.ipynb` i Jupyter Notebook.
4. Kör notebooken uppifrån och ned.

---

## Verktyg
- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- SQLite
