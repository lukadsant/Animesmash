import random
import os
import json

clear = lambda: os.system('cls')
turn = 0
totalpoints=0
arenaA={}
arenaA2={}
bottotalpoints=0
playertotalpoints=0
#ao revelar
#constante
#sem habilidade
#descartar
#mover
#destruir



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

# Exemplo: Imprima informações sobre as cartas
#for carta in cartas:
#    print(carta)

chaves = list(cafe.keys())
player_hand = random.choices(chaves)
x=player_hand[0]

player_hand = cafe[f'{1}']
enemy_hand= cafe[f'{x}']



def ability(card,player):
    
    escolhas=['buff','debuff','destroy','clone','sem habilidade']
    if player ==1:
        case=card.habilidade
    else:
        case='sem habilidade'#random.choice(escolhas)
    
    print(f'efeito da carta: {case}\n')
    
    if case=='buff':
        if player==1:
            print('playbuff')
            #card.poder=card.poder+3
            
            print(arenaA[0].nome)
                
            #print(arenaA[chave1])
            arenaA[0].poder=arenaA[0].poder+3
            
        elif player==2:
            print('botbuff')
            card.poder=card.poder+3
    elif case=='debuff':
        if player==1:
            enemy=arenaA2[-1].poder
            arenaA2[-1].poder=enemy-1
        else:
            enemy=arenaA[-1].poder
            arenaA[-1].poder=enemy-1
    elif case == 'destroy':
        if player==1:
            if len(arenaA2) > 0:
                arenaA2.pop()
            else:
                print("A lista arenaA2 está vazia. Não é possível fazer o pop.")
        else:
            if len(arenaA) > 0:
                arenaA.pop()
            else:
                print("A lista arenaA está vazia. Não é possível fazer o pop.")
            
    elif case == 'clone':
        if player==1:
            arenaA.append(card)
        else:
            arenaA2.append(card)
    else:
        print('Carta sem habilidade, Nenhum efeito ativado;')
        
    
while turn < 6:
    
    card=input(f'Aperte enter para continuar o turno {turn}...')
    clear()
    ascii_art = '''
                     _     _                    
                    | |   | |                   
     _ __   _____  _| |_  | |_ _   _ _ __ _ __  
    | '_ \ / _ \ \/ / __| | __| | | | '__| '_ \ 
    | | | |  __/>  <| |_  | |_| |_| | |  | | | |
    |_| |_|\___/_/\_\\__|  \__|\__,_|_|  |_| |_|
    '''

    print(ascii_art)
    print(f'turno {turn}')

    arenaA[turn]=player_hand
    arenaA2[turn]=enemy_hand

    print("Campo do Player:")



    for carta in arenaA:
        print(arenaA[carta])
    # Para o bot
    print("Campo do Bot:")
    for carta in arenaA2:
        print(arenaA2[carta])
    
    chave1 = list(arenaA.keys())[-1]
    chave2 = list(arenaA2.keys())[-1]

    
    if len(arenaA) > 0:
        print('ativando efeito da carta do player....')
        ability(arenaA[chave1],1)
    else:
        print('player está sem carta sem carta no campo, passando turno.')
    if len(arenaA2) > 0:
        print('ativando efeito da carta do bot....')
        ability(arenaA2[chave2],2)
    else:
        print('O bot está sem carta no campo, passando turno.')
        
    print(f'\n Campo após o efeito:')
    # Para o jogador
    print("Player:")
    for carta in arenaA:
        print(arenaA[carta])


    # Para o bot
    print("Bot:")
    for carta in arenaA2:
        print(arenaA2[carta])


    for carta_nome, carta in arenaA.items():
        playertotalpoints += carta.poder
    
    for carta_nome, carta in arenaA2.items():
        bottotalpoints += carta.poder

    
    turn=turn+1

    
print("Player Total points:", playertotalpoints, "Points")
print("Bot Total points:", bottotalpoints, "Points")

if playertotalpoints > bottotalpoints:
    print("O jogador é o vencedor!")
elif playertotalpoints < bottotalpoints:
    print("O bot é o vencedor!")
else:
    print("É um empate!")