import pandas as pd 

df = pd.read_csv('pokemon.csv')
df.info()

# print(df.head(10))


# BESTAAT DEZE POKEMON
poke_naam = input("Bestaat deze pokemon")

pokemon_bestaat = False

for a in df["Name"]: # of een pokemon betstaat die iemand intypt
    if a == poke_naam:
        print('Pokemon ', poke_naam, ' bestaat!')
        pokemen_bestaat = True
        break

if pokemon_bestaat == False:
    print('Pokemon ', poke_naam, ' bestaat niet!')





# POKEMON MET ATTACK HOGER DAN 90
for i, pok in df.iterrows():
    if pok['Attack'] > 90:
        print(pok['Name'], pok['Attack'])



# Denk na welke info je uit dit bestand wil halen

"""
1. Welke pokemon wint van de pokemon die overal het sterkst is? 
2. Welke generatie pokemons hebben de hoogste attack score em welke variabele heeft daar de grootste invloed op?
3. Welke twee pokemons lijken het meest op elkaar?
4. Welke twee pokemons zijn het meest verschillend van elkaar?
"""