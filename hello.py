from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
import random
from pyfiglet import Figlet
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class Carta:
    def __init__(self, name, poder, custo, habilidade):
        self.nome = name
        self.poder = poder
        self.custo = custo
        self.habilidade = habilidade

    def __str__(self):
        return f"Nome {self.nome}, Poder: {self.poder}, Custo: {self.custo}, Habilidade: {self.habilidade}"

# Lógica do jogo
turno = 0
arenaA = {}
arenaA2 = {}
# Defina uma variável de controle fora da função para alternar o comportamento.
isSKILLTIME = False
def carregar_cartas():
    with open('cartas.json', 'r') as file:
        data = json.load(file)
    
    cartas = []
    for card_data in data['cards']:
        carta = Carta(card_data['name'], card_data['power'], card_data['cost'], card_data['effect'])
        cartas.append(carta)

    return cartas


def aplicar_habilidade(carta, player,chave1,chave2):
    if player == 1:
        arena = arenaA
        arenaenemy = arenaA2
    else:
        arena = arenaA2
        arenaenemy = arenaA

    print('carta com habiidade: ',carta)
    print(f'efeito da carta: {carta.habilidade}\n')

    if carta.habilidade == 'buff':
        arena[chave1].poder += 3
    elif carta.habilidade == 'debuff':
        arenaenemy[chave2].poder -= 5
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

# Carregue as cartas do JSON
cartas = carregar_cartas()
enemydeck=[]
enemyhand=[]
#def gerardeck():
#    for x in range(9):
#        enemydeck.append(random.choice(cartas))
    
def gerardeck():
    # Certifique-se de que você tem pelo menos 9 cartas disponíveis em 'cartas'.
    for x in cartas:
        print(x)
    if len(cartas) < 9:
        raise ValueError("Não há cartas suficientes para criar um deck.")

    # Use random.sample() para selecionar 9 cartas sem repetição.
    enemydeck.append(random.sample(cartas, 9))
    print('olha pnc: ')
    for x in enemydeck[0]:
        print(x)


gerardeck()

def decktohand():
    cardselected=random.choice(range(len(enemydeck[0])))
    carta_selecionada=enemydeck[0].pop(cardselected)
    enemyhand.append(carta_selecionada)
    print(f'cartas restantes: {len(enemydeck[0])}')
    print(f'!!!!!!!!xxxxxxxxxxxxxxxxxxx!!!!!!!!!!!!!: {enemyhand}')
    print(f'cartas restantes: {len(enemydeck[0])}')
def novo_turno():
    global turno
    turno += 1
    decktohand()

    x_sorteada =random.choice(range(len(enemyhand))) #random.choice(cartas)
    carta_sorteada =enemyhand.pop(x_sorteada)
    #carta_sorteada =random.choice(enemyhand) #random.choice(cartas)
    print(carta_sorteada)
    print('carta sorteada: ',carta_sorteada)
    arenaA[turno] = Carta('Monster', 3, 3, 'buff')
    arenaA2[turno] = carta_sorteada
    
    imprimir_arena(arenaA)
    print('----------------VS----------------')
    imprimir_arena(arenaA2)

    
        
def ativar_habilidade():
    chave1 = list(arenaA.keys())[-1]
    chave2 = list(arenaA2.keys())[-1]
    if len(arenaA) > 0:
        print('\n~~Ativando efeito da carta do player~~')
        aplicar_habilidade(arenaA[chave1], 1,chave1,chave2)
    else:
        print('\n~~player está sem carta no campo, passando turno.~~')
    if len(arenaA2) > 0:
        print('~~Ativando efeito da carta do bot~~')
        aplicar_habilidade(arenaA2[chave2], 2,chave2,chave1,)
    else:
        print('~~O bot está sem carta no campo, passando turno.~~')

        
@app.route('/')
def index():
    print(turno,arenaA,arenaA2)
    return render_template('index.html', turno=turno,playercard=arenaA,botcard=arenaA2,isSKILLTIME=isSKILLTIME)

@app.route('/novo_turno', methods=['POST'])
def proximo_turno():
    global isSKILLTIME  # Use a variável global para que ela possa ser modificada.
    
    if isSKILLTIME==False:
        novo_turno()
        isSKILLTIME = True
    return redirect(url_for('index'))

@app.route('/skill_turn', methods=['POST'])
def ativar_turno():
    global isSKILLTIME  # Use a variável global para que ela possa ser modificada.
    
    if isSKILLTIME==True:
        ativar_habilidade()
        isSKILLTIME = False  # Inverte o valor da variável para alternar o comportamento.
    

    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
