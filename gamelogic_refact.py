import random
import os
import json
from pyfiglet import Figlet

# Função para limpar a tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Carta:
    def __init__(self, name, poder, custo, habilidade):
        self.nome = name
        self.poder = poder
        self.custo = custo
        self.habilidade = habilidade

    def __str__(self):
        return f"Nome {self.nome}, Poder: {self.poder}, Custo: {self.custo}, Habilidade: {self.habilidade}"

def carregar_cartas():
    with open('cartas.json', 'r') as file:
        data = json.load(file)
    
    cartas = []
    for card_data in data['cards']:
        carta = Carta(card_data['name'], card_data['power'], card_data['cost'], card_data['effect'])
        cartas.append(carta)
    
    return cartas

def aplicar_habilidade(carta, player):
    if player == 1:
        arena = arenaA
        arenaenemy = arenaA2
    else:
        arena = arenaA2
        arenaenemy = arenaA

    print(f'efeito da carta: {carta.habilidade}\n')

    if carta.habilidade == 'buff':
        arena[chave1].poder += 3
    elif carta.habilidade == 'debuff':
        arena[chave2].poder -= 1
    elif carta.habilidade == 'destroy':
        if len(arena) > 0:
            chave, valor = arenaenemy.popitem()
            print(f"Último item removido - Chave: {chave}, Valor: {valor}")
        else:
            print(f"A lista arena{'A2' if player == 2 else 'A'} está vazia. Não é possível fazer o pop.")
    elif carta.habilidade == 'clone':
        chavex = list(arena.keys())[-1]
        arena[chavex + 1] = carta
    else:
        print('Carta sem habilidade, Nenhum efeito ativado;')

def imprimir_arena(arena):
    print("----Campo----")
    for carta in arena.values():
        print(carta)
    print("-------------")

def calcular_total_pontos(arena):
    total = sum(carta.poder for carta in arena.values())
    return total

f = Figlet(font='slant')
clear_screen()
turno = 0
arenaA = {}
arenaA2 = {}

# Carregue as cartas do JSON
cartas = carregar_cartas()

while turno < 6:
    carta_sorteada = random.choice(cartas)

    input(f'Aperte enter para começar o turno {turno}...')
    clear_screen()
    print(f.renderText(f'Turno {turno}'))

    arenaA[turno] = Carta('Monster', 3, 3, 'buff')
    arenaA2[turno] = carta_sorteada

    imprimir_arena(arenaA)
    print('----------------VS----------------')
    imprimir_arena(arenaA2)

    chave1 = list(arenaA.keys())[-1]
    chave2 = list(arenaA2.keys())[-1]

    if len(arenaA) > 0:
        print('\n~~Ativando efeito da carta do player~~')
        aplicar_habilidade(arenaA[chave1], 1)
    else:
        print('\n~~player está sem carta no campo, passando turno.~~')
    
    if len(arenaA2) > 0:
        print('~~Ativando efeito da carta do bot~~')
        aplicar_habilidade(arenaA2[chave2], 2)
    else:
        print('~~O bot está sem carta no campo, passando turno.~~')

    print(f'\nCampo após o efeito~~~~~~')
    imprimir_arena(arenaA)
    print('----------------VS----------------')
    imprimir_arena(arenaA2)

    turno += 1

playertotalpoints = calcular_total_pontos(arenaA)
bottotalpoints = calcular_total_pontos(arenaA2)

print("Player Total points:", playertotalpoints, "Points")
print("Bot Total points:", bottotalpoints, "Points")

if playertotalpoints > bottotalpoints:
    print("O jogador é o vencedor!")
elif playertotalpoints < bottotalpoints:
    print("O bot é o vencedor!")
else:
    print("É um empate!")
