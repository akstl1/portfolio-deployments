# import pokebase as pb
# import webbrowser
# import dash
# from dash import html
# from dash import dcc
import pandas as pd
# import plotly.graph_objs as go
# from dash.dependencies import Input, Output, State
import requests
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Pokedex", layout="wide")

with open("./pages/pokedex.css") as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# get the total count of pokemon from pokeAPI, store as string variable
poke_count=requests.get("https://pokeapi.co/api/v2/pokemon-species")
poke_count_str = str(poke_count.json()['count'])

# request json object with names of all pokemon, using the upper limit of pokemon above
poke_names_json_request = requests.get("https://pokeapi.co/api/v2/pokemon-species/?offset=0&limit="+poke_count_str)
#store request in a variable as json
poke_names_request_response = poke_names_json_request.json()


# create empty list to store pokemon names, loop through request response to populate the list_
poke_names_list = []
for name in poke_names_request_response['results']:
    poke_names_list.append(name['name'])



st.header('Pokedex')

cola,colb,colc = st.columns([.3,.4,.3])
with cola:
    st.write()
with colb:
    poke_input = st.selectbox("Select a pokemon",poke_names_list,label_visibility="hidden")

pokemon_species_request = requests.get("https://pokeapi.co/api/v2/pokemon-species/"+str(poke_input)+"/")
species_data = pokemon_species_request.json()

pokemon_request = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(poke_input)+"/")
pokemon_data = pokemon_request.json()

poke_id=str(species_data['id'])

col1,col2 = st.columns([.4,.6])

image = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/"+poke_id+".png"

with col1:
    # st.write(species_data)
    st.write("##")
    st.image(image)

## Description callback
entry=species_data['flavor_text_entries'][0]['flavor_text'].replace('\x0c',' ')

## Ability Data
abilities_json=pokemon_data['abilities']
abilities = []
for ability in abilities_json:
    abilities.append(ability['ability']['name'].capitalize())
ability_str = ', '.join(abilities)

## Types Data
types_json=pokemon_data['types']
types = []
for type in types_json:
    types.append(type['type']['name'].capitalize())
types_str = ', '.join(types)
## Height Data
height=pokemon_data['height']/10

## Weight Data
weight=pokemon_data['height']/10

with col2:
    st.write("##")
    st.write("##")
    st.write("Description: "+ entry)
    st.write("Height: "+str(height)+" m") 
    st.write("Weight: "+str(weight)+" kg")
    st.write("Abilities: "+ability_str)
    st.write("Types: "+types_str)
    
stats_json=pokemon_data['stats']
stats=[]
#cycle through data and append it to the stats list
for stat in stats_json:
    stats.append([stat['stat']['name'], stat['base_stat']])
# generate df with the stats list data, generate bar plot
df = pd.DataFrame(stats, columns = ['Stat', 'Base Value'])
fig = px.bar(df, x="Stat", y="Base Value",text_auto=True)
fig.update_yaxes(range=[0, 270])
fig.update_xaxes(tickangle=45)
# return fig,{'height':'300px'}  


st.plotly_chart(fig, use_container_width=True,theme=None)
