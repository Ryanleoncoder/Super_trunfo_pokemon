import requests 
import random
import json
import os
import time
import datetime
# importes necessários


cache_file = 'kanto_pokemons.json' # armazenamento local dos dados dos pokémons

# Função para baixar dados dos pokémons da 1ª geração (Kanto) da API do PokéAPI
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


# função para carregar os dados dos pokémons do arquivo local ou baixar da API se o arquivo não existir
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

#import do módulo de banco de dados
import querydb  
querydb.criar_tabela_pokedex()
querydb.criar_tabela_score()




# funcao para sorteamento e escolha de pokémons
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

# função para selecionar um adversário aleatório
def adversario_aleatorio():
    adversario = random.choice(pokemons_kanto)
    print(f"Seu adversário é {adversario['nome']}! Prepare-se para a batalha! ⚔️")
    return adversario

# função para realizar a batalha entre o pokémon do jogador e o adversário       
def batalha(pokemon_jogador, pokemon_adversario):
    print(f"\nBatalha entre {pokemon_jogador['nome']} e {pokemon_adversario['nome']}!")
    pontos_jogador = pokemon_jogador['ataque'] + pokemon_jogador['defesa'] + pokemon_jogador['hp']
    pontos_adversario = pokemon_adversario['ataque'] + pokemon_adversario['defesa'] + pokemon_adversario['hp']

    print(f"""
       +====================================================== BATALHA! ======================================================+
          Pontos de {pokemon_jogador['nome']}: {pontos_jogador} VS Pontos de {pokemon_adversario['nome']}: {pontos_adversario}

          SEU POKÉMON:                                                   POKÉMON ADVERSÁRIO:
                                                                                                 
        {pokemon_jogador['nome']}                                                           {pokemon_adversario['nome']}
          HP: {pokemon_jogador['hp']}                                                          HP: {pokemon_adversario['hp']}
          Ataque: {pokemon_jogador['ataque']}                                                     Ataque: {pokemon_adversario['ataque']}
          Defesa: {pokemon_jogador['defesa']}                                                      Defesa: {pokemon_adversario['defesa']}
       +====================================================== BATALHA! ======================================================+


""")

    time.sleep(4)
# Determinar o vencedor
    if pontos_jogador > pontos_adversario:
        time.sleep(1)
        print(f"{pokemon_jogador['nome']} venceu a batalha! 🎉")
        print(f"""  
              
             +========================== Parabéns! ======================================+
              Agora {pokemon_adversario['nome']} está na sua Pokédex 📲
              você também ganhou 10 pontos para adicionar em um pokemon da sua equipe! 🎖️
             +===========================================================================+
              """)
        addpokedex = querydb.pokedex(
            pokemon_adversario['nome'],
            pokemon_adversario['tipo_primario'],
            pokemon_adversario['tipo_secundario'],
            pokemon_adversario['hp'],
            pokemon_adversario['ataque'],
            pokemon_adversario['defesa']
        )
        adicionar = input("Deseja adicionar pontos a um Pokémon da sua equipe? (sim/não): ").strip().lower()
        if adicionar == 'sim':
            print("Escolha um Pokémon da sua equipe para adicionar pontos:")
            for i, poke in enumerate(escolhidos, start=1):
                print(f"{i}. {poke['nome']}")
            escolha = input("Digite o número do Pokémon: ").strip()
            if escolha in ['1', '2', '3']:
                escolhido_add = escolhidos[int(escolha) - 1]
                pontos_para_adicionar = 10
                escolhido_add['ataque'] += pontos_para_adicionar
                print(f"Você adicionou {pontos_para_adicionar} pontos ao Pokémon {escolha} da sua equipe!")
            else:
                print("Escolha inválida. Nenhum ponto adicionado.")
        
                               
    elif pontos_jogador < pontos_adversario:
        time.sleep(1)
        print(f"{pokemon_adversario['nome']} venceu a batalha! 😞")
                                      
    else:
        time.sleep(1)
        print("A batalha terminou em empate! 🤝")
        print(f"""  
              
             +========================== EMPATE! ========================================+
              Agora {pokemon_adversario['nome']} está na sua Pokédex 📲
              você também ganhou 5 pontos para adicionar em um pokemon da sua equipe! 🎖️
             +===========================================================================+
              """)
        addpokedex = querydb.pokedex(
            nome=pokemon_adversario['nome'],
            tipo_primario=pokemon_adversario['tipo_primario'],
            tipo_secundario=pokemon_adversario['tipo_secundario'],
            hp=pokemon_adversario['hp'],
            ataque=pokemon_adversario['ataque'],
            defesa=pokemon_adversario['defesa'],
        )
        adicionar = input("Deseja adicionar pontos a um Pokémon da sua equipe? (sim/não): ").strip().lower()
        if adicionar == 'sim':
            print("Escolha um Pokémon da sua equipe para adicionar pontos:")
            for i, poke in enumerate(escolhidos, start=1):
                print(f"{i}. {poke['nome']}")
            escolha = input("Digite o número do Pokémon: ").strip()
            if escolha in ['1', '2', '3']:
                escolhido_add = escolhidos[int(escolha) - 1]
                pontos_para_adicionar = 5
                escolhido_add['ataque'] += pontos_para_adicionar
                menu_pos_escolha(escolhidos)
                print(f"Você adicionou {pontos_para_adicionar} pontos ao Pokémon {escolha} da sua equipe!")
            else:
                print("Escolha inválida. Nenhum ponto adicionado.")


      # >> Ao adicionar pontos em caso de empate ou vitória do pokemon de escolha do jogador, o pokemon e o mesmo pokemon salvo no cache ficam com os mesmo status atualizados <<
      # >> ver de resolver isso futuramente para apenas o pokemon da equipe do jogador ser atualizado <<

# menu após a escolha dos pokémons
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
                print(f"{i}. {poke['nome']} \n Tipo primario: {poke['tipo_primario']}\n tipo_secundario {poke['tipo_secundario']}\n HP: {poke['hp']}\n Ataque: {poke['ataque']}\n Defesa: {poke['defesa']}\n")
        
        elif opcao == '2':
            for i, poke in enumerate(escolhidos, start=1):
                print(f"{i}. {poke['nome']}")
            escolha = input("Escolha qual Pokémon vai batalhar: ")
            if escolha in ['1', '2', '3']:
                escolhido = escolhidos[int(escolha)-1]
                print(f"{escolhido['nome']} entrou em batalha! 🥊")
                print("Batalha iniciando em 1️⃣  ")
                time.sleep(1)
                print("Batalha iniciando em 2️⃣ ")
                time.sleep(1)
                print("Batalha iniciando em 3️⃣ ")
                time.sleep(1)
                batalha(escolhido, adversario_aleatorio())
                
            else:
                print("Escolha inválida.")
        
        elif opcao == '3':
            print("Equipe salva com sucesso!")
            
        
        elif opcao == '4':
            print("Voltando ao menu principal...")
            time.sleep(1)
            break

        else:
            print("Opção inválida.")
   



# LOOP DO MENU PRINCIPAL
def mostrar_menu():
    print("""
        +=============== MENU ================+
        |           1 - Start🎮               |
        |           2 - Score🎰               |
        |           3 - Pokedex📱             |
        |           4 - Exit🔚                |
        +=====================================+
          
          """)

#menu  (ainda em desenvolvimento)
while True:
    mostrar_menu()
    escolher = input("Escolha uma opção ")

    if escolher == '1' or escolher.lower() == 'start':
     escolhidos = mostrar_pokemons()
     if escolhidos:
      menu_pos_escolha(escolhidos)
    elif escolher == '2' or escolher.lower() == 'score':
       print("Score do jogador: ")
    elif escolher == '3' or escolher.lower() == 'pokedex':
      print("Pokemons já encontrados: ")
      pokedex_registrada = querydb.mostrar_pokedex()
      for poke in pokedex_registrada:
        print(f"- {poke[0]}")
    elif escolher == '4' or escolher.lower() == 'exit':
       print("Saindo do jogo")
       break
    else:
       print("opção invalida tente novamente: ")


