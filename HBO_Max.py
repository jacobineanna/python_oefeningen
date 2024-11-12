import pandas as pd

df_HBO = pd.read_csv("HBO_Max.csv")

print("Laden dataframe gelukt.")

print(df_HBO.info())

"""
Onderzoeksvragen
--------------------------------------

1. Welke genres hebben de hoogste gemiddelde 
IMDb-score en zijn hierin verschillen tussen 
films en tv-series?

Benodigde kolommen:
- Genres
- Type
Imdb score

Plan van aanpak:
- Data groeperen per genre en type(film/tv serie)
- Gemiddelde imdb rating voor elk genre berekenen
- Visualiseren met een staafdiagram waarin films 
en tv series per genre kunnen worden vergeleken.


2. Welke invloed heeft het aantal stemmen op de 
IMDb-rating?

Benodigde kolommen:
- imdbNumVotes
- imdbAverageRating

Plan van aanpak:
- Gemiddelde, mediaan en standaarddeviatie van beide
variabelen berekenen om een beeld te krijgen van de 
algemene spreiding.
- correlatie analyse
- Visualiseren met een scatterplot met regressielijn
- Kan ook nog groepen vergelijken (weinig, gemiddeld,
en veel stemmen)

3. Hoe verschilt de gemiddelde IMDb-rating van titels 
die beschikbaar zijn in meerdere landen ten opzichte 
van titels die slechts in één land beschikbaar zijn?

Benodigde kolommen:
- Type
- Genre
- AvailableCountries

Plan van Aanpak:
- Aantal Landen per Titel Berekenen: Voeg een kolom toe 
die het aantal landen telt waarin elke titel beschikbaar 
is door de `availableCountries`-kolom te tellen.
- Maak twee categorieën aan: "Globaal beschikbaar" 
(titels beschikbaar in meerdere landen) en "Lokaal beschikbaar" 
(titels beschikbaar in slechts één land).
- Bereken de gemiddelde IMDb-rating voor beide categorieën om te 
zien of er verschillen zijn in de waardering tussen globaal en 
lokaal beschikbare titels.
- Boxplot om het gemiddelde en spreiding van IMDb-ratings voor de 
"globaal" en "lokaal" categorieën te visualiseren.

"""