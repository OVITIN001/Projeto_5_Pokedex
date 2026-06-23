import streamlit as st
import requests

st.set_page_config(layout="wide")

# Busca lista de Pokémons na API
url_lista = "https://pokeapi.co/api/v2/pokemon?limit=1025"
nomes_pokemons = [
    pokemon["name"]
    for pokemon in requests.get(url_lista).json()["results"]
]

nome = st.selectbox("Escolha um Pokémon", nomes_pokemons)

url = f"https://pokeapi.co/api/v2/pokemon/{nome}"
dados_pokemon = requests.get(url).json()

col1, col2, col3 = st.columns(3)

peso = dados_pokemon["weight"] / 10
altura = dados_pokemon["height"] / 10

if altura > 0:
    imc = round(peso / (altura ** 2), 2)
else:
    imc = 0

with col1:
    st.image(dados_pokemon["sprites"]["front_default"], width=400)
    st.write("Normal")

with col2:
    st.audio(dados_pokemon["cries"]["latest"])
    st.audio(dados_pokemon["cries"]["legacy"])

with col3:
    st.image(dados_pokemon["sprites"]["front_shiny"], width=400)
    st.write("Shiny")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Altura", f"{altura} m")

with col2:
    st.metric("IMC", imc)

with col3:
    st.metric("Peso", f"{peso} kg")

tipos, status, locais, habilidades = st.tabs(['Tipos','Status','Locais','habiilidades'])

with tipos:
    for i in dados_pokemon['types']:
        st.markdown(f'-{i['type']['name']}')

with status:
  hp, ataque, defesa, ataque_esp, defesa_esp, velocidade = st.columns(6) 
  with hp:
       st.metric('HP', dados_pokemon['stats'][0]['base_stat'])
  with ataque:
      st.metric('Ataque', dados_pokemon['stats'][1]['base_stat'])

  with defesa:
       st.metric('Defesa', dados_pokemon['stats'][2]['base_stat']) 
  
  with ataque_esp:
       st.metric('Ataque Especial', dados_pokemon['stats'][3]['base_stat'])

  with defesa_esp: 
       st.metric('Defesa Especial', dados_pokemon['stats'][4]['base_stat'])

  with velocidade:

       st.metric('Velocidade', dados_pokemon['stats'][5]['base_stat'])

with locais:
    locais = requests.get(dados_pokemon['location_area_encounters']).json()
    for local in locais:
        st.markdown(f'-{local['location_area']['name']}')

with habilidades:
    for habilidade in dados_pokemon['abilities']:
        st.markdown(f'-{habilidade['ability']['name']}')