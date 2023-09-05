import random

turn = 0
totalpoints=0
arenaA=[]
arenaA2=[]

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
    

minha_carta = Carta("Goku", 3, 3, "destroy")
print(minha_carta.poder)

def ability(card,player):
    
    escolhas=['buff','debuff','destroy','clone']
    if player ==1:
        case=card.habilidade
    else:
        case=random.choice(escolhas)
    
    print(f'efeito da carta: {case}')
    
    if case=='buff':
        cardbuff=card
        if player==1:
            arenaA[-1].poder=cardbuff.poder+3
        else:
            arenaA2[-1].poder=cardbuff.poder+3
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
        
    
while turn < 6:
    print(f"Turno {turn}\n")
    
    card=int(input('Insira seu card '))
    
    
    arenaA.append(minha_carta)
    arenaA2.append(minha_carta)
    print(f'player: {arenaA}')
    print(f'bot: {arenaA2}')
    
    if len(arenaA) > 0:
        print('ativando efeito da carta do player....')
        ability(arenaA[-1],1)
    else:
        print('player sem carta')
    if len(arenaA2) > 0:
        print('ativando efeito da carta do bot....')
        ability(arenaA2[-1],2)
    else:
        print('bot sem carta')
    # Para o jogador
    print("Player:")
    for carta in arenaA:
        print(f'Nome: {carta.nome}, Poder: {carta.poder}')

    # Para o bot
    print("Bot:")
    for carta in arenaA2:
        print(f'Nome: {carta.nome}, Poder: {carta.poder}')
    
    playertotalpoints=sum(carta.poder for carta in arenaA)
    bottotalpoints=sum(carta.poder for carta in arenaA2)
    turn=turn+1
    
print("Player Total points:", playertotalpoints, "Points")
print("Bot Total points:", bottotalpoints, "Points")

if playertotalpoints > bottotalpoints:
    print("O jogador é o vencedor!")
elif playertotalpoints < bottotalpoints:
    print("O bot é o vencedor!")
else:
    print("É um empate!")