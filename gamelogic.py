import random
import os
import json
from pyfiglet import Figlet
f = Figlet(font='slant')

clear = lambda: os.system('cls')
turn = 0
totalpoints=0
arenaA={}
arenaA2={}
bottotalpoints=0
playertotalpoints=0


class Carta:
    def __init__(self,name,poder, custo,habilidade):
        self.nome=name
        self.poder=poder
        self.custo=custo
        self.habilidade=habilidade
    
    def __str__(self):
        return f"Nome {self.nome}, Poder: {self.poder}, Custo: {self.custo}, Habilidade: {self.habilidade}"
    


# Carregue os dados do JSON
with open('cartas.json', 'r') as file:
    data = json.load(file)

# Crie instâncias da classe Carta com base nos dados do JSON
cartas = []
cafe={}
for card_data in data['cards']:
    carta = Carta(card_data['name'], card_data['power'], card_data['cost'], card_data['effect'])
    cartas.append(carta)
    
    cafe[f'{len(cartas)}']=Carta(card_data['name'], card_data['power'], card_data['cost'], card_data['effect'])


def ability(card,player):
    
    if player ==1:
        case=card.habilidade
    else:
        case=card.habilidade
    
    print(f'efeito da carta: {case}\n')
    
    if case=='buff':
        if player==1:
            arenaA[chave1].poder=arenaA[chave1].poder+3
            
        elif player==2:
            arenaA2[chave2].poder=arenaA2[chave2].poder+3
    elif case=='debuff':
        if player==1:
            arenaA2[chave2].poder=arenaA2[chave2].poder-1
        else:
            arenaA[chave1].poder=arenaA[chave1].poder-1
    elif case == 'destroy':
        if player==1:
            if len(arenaA2) > 0:

                ultimo_item_removido = arenaA2.popitem()
                chave, valor = ultimo_item_removido

                print(f"Último item removido - Chave: {chave}, Valor: {valor}")
            else:
                print("A lista arenaA2 está vazia. Não é possível fazer o pop.")
        else:
            if len(arenaA) > 0:

                ultimo_item_removido = arenaA.popitem()
                chave, valor = ultimo_item_removido

                print(f"Último item removido - Chave: {chave}, Valor: {valor}")
            else:
                print("A lista arenaA está vazia. Não é possível fazer o pop.")
            
            
    elif case == 'clone':
        if player==1:
            chavex = list(arenaA.keys())[-1]
            arenaA[chavex+1] = card
        else:
            chavez = list(arenaA2.keys())[-1]
            arenaA2[chavez+1] = card
    else:
        print('Carta sem habilidade, Nenhum efeito ativado;')
        

while turn < 6:
    index_das_cartas = list(cafe.keys()) 
    id_da_carta_sorteada = random.choices(index_das_cartas)
    Carta_sorteada= cafe[f'{id_da_carta_sorteada[0]}']

    
    input(f'Aperte enter para começar o turno {turn}...')
    clear()

    print(f.renderText(f'Turno {turn}'))

    arenaA[turn]=Carta('Monster',3,3,'buff')
    arenaA2[turn]=Carta_sorteada



    print("----Campo do Player----")
    for carta in arenaA:
        print(arenaA[carta])

    print('----------------VS----------------')
    # Para o bot
    for carta in arenaA2:
        print(arenaA2[carta])
    print("----Campo do Bot----")

    chave1 = list(arenaA.keys())[-1]
    chave2 = list(arenaA2.keys())[-1]

    
    if len(arenaA) > 0:
        print('\n~~Ativando efeito da carta do player~~')
        ability(arenaA[chave1],1)
    else:
        print('\n~~player está sem carta sem carta no campo, passando turno.~~')
    if len(arenaA2) > 0:
        print('~~Ativando efeito da carta do bot~~')
        ability(arenaA2[chave2],2)
    else:
        print('~~O bot está sem carta no campo, passando turno.~~')
        
    print(f'\nCampo após o efeito~~~~~~')
    # Para o jogador
    print("----Campo do Player----")
    for carta in arenaA:
        print(arenaA[carta])

    print('----------------VS----------------')
    # Para o bot
    for carta in arenaA2:
        print(arenaA2[carta])
    print("----Campo do Bot----")

    turn=turn+1
    
    
for carta_nome, carta in arenaA.items():
    playertotalpoints += carta.poder

for carta_nome, carta in arenaA2.items():
    bottotalpoints += carta.poder
    
print("Player Total points:", playertotalpoints, "Points")
print("Bot Total points:", bottotalpoints, "Points")

if playertotalpoints > bottotalpoints:
    print("O jogador é o vencedor!")
elif playertotalpoints < bottotalpoints:
    print("O bot é o vencedor!")
else:
    print("É um empate!")