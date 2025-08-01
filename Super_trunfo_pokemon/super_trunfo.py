import sqlite3
import requests
import random




import querydb
querydb.criar_tabela_pokedex()

def pegar_nome_pokemon(pokemon_id):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        return dados['name'].capitalize()
    else:
        return None

def mostrar_3_pokemons():
    ids_sorteados = random.sample(range(1, 899), 3)
    pokemons = []
    print("\nPokémons sorteados:")
    for i, poke_id in enumerate(ids_sorteados, start=1):
        nome = pegar_nome_pokemon(poke_id)
        if nome:
            pokemons.append(nome)
            print(f"{i}. {nome}")
        else:
            print(f"{i}. Pokémon não encontrado.")
    
    while True:
        option = input("\nEscolha um pokemon\n ou \nDigite 'voltar' para retornar ao menu: ").strip().lower()
        if option == 'voltar':
            return None
        elif option in ['1', '2', '3']:
            escolhido = pokemons[int(option) - 1]
            print(f"O pokemon escolhido foi {escolhido}")
            break
        else:
            print("Comando inválido. Digite 'voltar' para retornar ao menu.")




def mostrar_menu():
    print("+====================+\n| 1 - Start          |\n| 2 - Score          |\n| 3 - Pokedex        |\n| 4 - Exit           |\n+====================+")

#menu exemplo - ainda em andandmento
while True:
    mostrar_menu()
    escolher = input("Escolha uma opção ")

    if escolher == '1':
     mostrar_3_pokemons()
    elif escolher == '2':
       print("Score do jogador: ")
    elif escolher == '3':
      print("Pokemons já encontrados: ")
    elif escolher == '4':
       print("Saindo do jogo")
       break
    else:
       print("opção imvalida tente novamente: ")


""""
def buscar_pokemon_por_id(pokemon_id):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    resposta = requests.get(url)

    if resposta.status_code == 200:
"""
