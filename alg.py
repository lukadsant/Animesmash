import random

turn = 0
totalpoints=0
arenaA=[]
arenaA2=[]



def ability(card):
    
    escolhas=['buff','debuff','destroy','clone']
    case=random.choice(escolhas)
    print(f'efeito da carta: {case}')
    if case=='buff':
        cardbuff=card
        arenaA[-1]=cardbuff+3
    elif case=='debuff':
        enemy=arenaA2[-1]
        arenaA2[-1]=enemy-1
    elif case == 'destroy':
        arenaA2.pop()
    elif case == 'clone':
        arenaA.append(card)

        
    
while turn < 6:
    print("Turn", turn)
    
    card=int(input('Insira seu card '))
    
    
    arenaA.append(card)
    arenaA2.append(2)
    print(f'player: {arenaA}')
    print(f'bot: {arenaA2}')
    print('ativando efeito da carta....')

    ability(arenaA[-1])
    print(f'player: {arenaA}')
    print(f'bot: {arenaA2}')
    
    totalpoints=sum(arenaA)
    turn=turn+1
    
print("Total points:", totalpoints, "Points")