import random
import os

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
    



def ability(card,player):
    if player ==1:
        case=card.habilidade
    else:
        case='sem habilidade'
    
    print(f'efeito da carta: {case}\n')
    
    if case=='buff':
        if player==1:
            print('playbuff')
            print(arenaA)
            arenaA[chave1].poder=arenaA[chave1].poder+3
            
        elif player==2:
            print('botbuff')
            card.poder=card.poder+3
    else:
        print("carta sem habilidade!")

player_hand = Carta('Monster',3,3,'buff')

while turn < 6:
    arenaA[turn]=Carta('Monster',3,3,'buff')
    print('playerhand: ',player_hand)
    print("Campo do Player:")
    for carta in arenaA:
        print(arenaA[carta])
    print('vendo arenaA: ',arenaA[0])

    chave1 = list(arenaA.keys())[-1]
    

    if len(arenaA) > 0:
        print('ativando efeito da carta do player....')
        ability(arenaA[chave1],1)
    else:
        print('player está sem carta sem carta no campo, passando turno.')
    turn=turn+1
    print(f'fim do turno {turn}')