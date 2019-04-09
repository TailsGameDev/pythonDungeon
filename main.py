from sala import Sala
from enum import Enum
from personagem import Personagem

def constroiMapa():
    salaPrincipal = Sala("Voce esta em uma caverna umida e sombria, e "+
    "tudo que ve eh uma passagem estreita ao norte")
    salaNorte = Sala("Voce chegou ao fim desta trilha, encontrando apenas" +
    " paredes rochosas e agonia.")

    salaPrincipal.directions = {"ir para o norte": salaNorte }
    salaNorte.directions = {"ir para o sul": salaPrincipal }

    def olharEspelho():
        print("na penumbra voce ve sua propria silhueta")
    salaNorte.actions = { "olhar espelho": olharEspelho }

    goblin = Personagem("goblin")
    salaPrincipal.inimigos.append(goblin)

    return salaPrincipal

#INICIO DA EXECUCAO:
state = Enum('state', 'sala')
salaAtual = constroiMapa()
staticSala = Sala()
personagem = Personagem()
inpt = ""
estadoAtual = state.sala
salaAtual = staticSala.salaFSM(salaAtual, personagem)

'''
while (inpt != "quit" and inpt != "q"):
    #out
    if(estadoAtual == state.sala):
        salaAtual = staticSala.salaFSM(salaAtual, personagem)
        inpt = input("voce voltou para o menu. O que quer fazer?\n")
    #next state logic

    #memory element
'''
