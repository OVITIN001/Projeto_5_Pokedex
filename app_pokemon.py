import streamlit as st
import json
import requests

st.set_page_config(layout="wide")

with open('pokemon_index.json', 'r', encoding='utf-8') as arquivo:
    nomes_pokemons = json.load(arquivo)

nome = st.selectbox('Escolha um Pokemon', nomes_pokemons.values())

url = f'https://pokeapi.co/api/v2/pokemon/{nome}'
dados_pokemon = requests.get(url).json()

col1, col2, col3 = st.columns(3)

peso = dados_pokemon['weight']/10
altura = dados_pokemon['height']/10
imc = round(peso / (altura **2))

with col1:
    st.image(dados_pokemon['sprites']['front_default'], width=400)
    st.write('normal')

with col2:
    st.audio(dados_pokemon['cries']['latest'])
    st.audio(dados_pokemon['cries']['legacy'])

with col3:
    st.image(dados_pokemon['sprites']['front_shiny'], width=400)
    st.write('shiny')

col1, col2, col3 = st.columns(3)
with col1:
    st.metric('altura', f'{altura} m')

with col2:
    st.metric('IMC', imc)

with col3:
    st.metric('peso', f'{peso}KG')



