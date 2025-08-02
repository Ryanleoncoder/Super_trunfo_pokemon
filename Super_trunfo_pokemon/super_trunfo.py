import requests # importe da API
import random
import json
import os

cache_file = 'kanto_pokemons.json' # Parte essencial: baixa os 151 pokemons da regiao de kanto sem sobrecarregar a api de requests


### aparte abaixo foi desenvolvida para seguir a regra de Fair Use Policy
def baixar_pokemons_kanto():
    pokemons = []
    print("baixando dados dos Pokémons da 1ª geração (Kanto)... ⏰")
    for poke_id in range(1, 152):
        url = f'https://pokeapi.co/api/v2/pokemon/{poke_id}'
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            
            pokemon_data = {
                'id': dados['id'],
                'nome': dados['name'].capitalize(),
                'tipo_primario': dados['types'][0]['type']['name'],
                'tipo_secundario': dados['types'][1]['type']['name'] if len(dados['types']) > 1 else None,
                'hp': next(stat['base_stat'] for stat in dados['stats'] if stat['stat']['name'] == 'hp'),
                'ataque': next(stat['base_stat'] for stat in dados['stats'] if stat['stat']['name'] == 'attack'),
                'defesa': next(stat['base_stat'] for stat in dados['stats'] if stat['stat']['name'] == 'defense'),
            }
            pokemons.append(pokemon_data)
        else:
            print(f"Erro ao baixar Pokémon ID {poke_id} ❌")

    with open(cache_file, 'w', encoding='utf-8') as f:
        json.dump(pokemons, f, indent=2)
    print(f"Dados salvos em {cache_file}")

def carregar_cache_file():
    if os.path.exists(cache_file):
        with open(cache_file, 'r', encoding='utf-8') as f:
            pokemons = json.load(f)
        print(f"Carregados {len(pokemons)} pokémons do arquivo local. ✅")
        return pokemons
    else:
        print("Arquivo local não encontrado. Baixando da API... 📥")
        baixar_pokemons_kanto()
        return carregar_cache_file()



pokemons_kanto = carregar_cache_file()


import querydb #importando do arquivo que vai executar querys 
querydb.criar_tabela_pokedex()
querydb.criar_tabela_score()





def mostrar_pokemons():
    escolhidos = []

    while len(escolhidos) < 3:
        ids_sorteados = random.sample(range(len(pokemons_kanto)), 3)
        print("\nPokémons sorteados:")
        for i, idx in enumerate(ids_sorteados, start=1):
            poke = pokemons_kanto[idx]
            print(f"{i}. {poke['nome']}")
        
        option = input("\nEscolha um Pokémon (1-3) ou digite 'voltar' para sair: ").strip().lower()
        
        if option == 'voltar':
            return None
        
        elif option in ['1', '2', '3']:
            idx_escolhido = ids_sorteados[int(option) - 1]
            escolhido = pokemons_kanto[idx_escolhido]
            escolhidos.append(escolhido)
            print(f"Você escolheu: {escolhido['nome']}. Total escolhidos: {len(escolhidos)}/3")
        
        else:
            print("Opção inválida.")
    return escolhidos  


def menu_pos_escolha(escolhidos):
    while True:
        print("\n=== MENU DE EQUIPE ===")
        print("1. Ver detalhes dos Pokémons")
        print("2. Escolher 1 para batalhar")
        print("3. Salvar equipe")
        print("4. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\nSeus Pokémons:")
            for i, poke in enumerate(escolhidos, start=1):
                print(f"{i}. {poke['nome']} - Tipo primario: {poke['tipo_primario']}, tipo_secundario {poke['tipo_secundario']} HP: {poke['hp']}, Ataque: {poke['ataque']}, Defesa: {poke['defesa']}")
        
        elif opcao == '2':
            for i, poke in enumerate(escolhidos, start=1):
                print(f"{i}. {poke['nome']}")
            escolha = input("Escolha qual Pokémon vai batalhar: ")
            if escolha in ['1', '2', '3']:
                escolhido = escolhidos[int(escolha)-1]
                print(f"{escolhido['nome']} entrou em batalha! 🥊")
                print(f'Seu adversario é...')
                
            else:
                print("Escolha inválida.")
        
        elif opcao == '3':
            print("Equipe salva com sucesso!")
            
        
        elif opcao == '4':
            print("Voltando ao menu principal...")
            break

        else:
            print("Opção inválida.")
   

def mostrar_menu():
    print("+====================+\n| 1 - Start          |\n| 2 - Score          |\n| 3 - Pokedex        |\n| 4 - Exit           |\n+====================+")

#menu exemplo  (ainda em desenvolvimento)
while True:
    mostrar_menu()
    escolher = input("Escolha uma opção ")

    if escolher == '1':
     escolhidos = mostrar_pokemons()
     if escolhidos:
      menu_pos_escolha(escolhidos)
    elif escolher == '2':
       print("Score do jogador: ")
    elif escolher == '3':
      print("Pokemons já encontrados: ")
    elif escolher == '4':
       print("Saindo do jogo")
       break
    else:
       print("opção invalida tente novamente: ")



