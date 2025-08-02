# <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjM2MGRzZmRmemh2emJqOXYxZjRmemtlY2R2aTdnamNldmZqOXQ4NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/TZco470UACpNK/giphy.gif" alt="Pokemon" width="100"/> Super Trunfo Pokémon

> Projeto em fase de criação - um Super Trunfo Pokémon usando a API pública do PokéAPI.

---

## 1. Sobre o projeto

Este é um jogo estilo **Super Trunfo** com Pokémons, que permite ao usuário escolher pokémons sorteados aleatoriamente para formar um time.

O projeto está em desenvolvimento e atualmente implementa:

- Baixa os 151 pokemons de Kanto com [PokéAPI](https://pokeapi.co/) e salva em um arquivo JSON.
- Sorteio aleatório de 3 pokémons para o usuário escolher um.
- Armazenamento dos pokémons escolhidos em um banco de dados SQLite local (`supertrunfo.db`).
- Interface simples via terminal com menu para iniciar o jogo, ver score (em desenvolvimento), ver pokémons já encontrados e sair.

---

## 2. Estrutura do projeto

- `super_trunfo.py`:  
  Arquivo principal do jogo, com lógica para mostrar o menu, buscar pokémons, receber escolhas do usuário e chamar as funções do banco.

- `querydb.py`:  
  Contém funções para criar e manipular o banco de dados SQLite, como criar a tabela `pokedex` e inserir os pokémons escolhidos.

- `supertrunfo.db`:  
  Banco de dados SQLite onde são armazenados os pokémons escolhidos pelos jogadores.

---

## 3. Como rodar

1. Clone o repositório:

```bash
git clone https://github.com/Ryanleoncoder/Super_trunfo_pokemon.git
cd Super_trunfo_pokemon

````
2. Instale a biblioteca requests (se ainda não tiver):

````bash
pip install requests
````
3. Execute o arquivo principal:
`python super_trunfo.py`
## 4. Próximos passos
- Implementar sistema de pontuação (score) baseado em vitórias e derrotas.

- Melhorar o menu e a navegação entre telas.

- Criar a funcionalidade de Pokedex para listar pokémons já capturados.

- Salvar mais atributos dos pokémons no banco para facilitar comparações no jogo.

- Interface gráfica (GUI) para melhorar a experiência do usuário.

## 5. Licença
Projeto open source em desenvolvimento.

## 6. Contato
Para dúvidas ou contribuições, abra uma issue ou faça um pull request.

## 7. Observação
Este README será atualizado conforme o projeto evoluir.
