from combate import Combate
from enum import Enum
state = Enum('state', 'descreve combateFSM ' +
'morte fugir logOptions venceuCombate')

class Sala:
    #python nao permite construtores multiplos, mas permite default value
    def __init__ (self, desc= "batata"):
        self.descricao = desc
        self.directions = {}
        self.actions = {}
        self.inimigos = []
        #mais tarde poderia ser adicionado funções de combate proprias da sala
        #self.combatOptions = {"fugir" : state.fugir , "atacar": state.combate}

    def salaFSM(self, salaAtual, personagem):
        estadoAtual = state.descreve
        inpt = ""
        while(inpt != "quit" and inpt != "q"):
            #SAIDAS, PRINTS, INPUTS
            if(estadoAtual == state.descreve):
                print('\n'+salaAtual.descricao)

            elif(estadoAtual == state.combateFSM):
                combate = Combate(personagem, salaAtual.inimigos)
                retornoCombate = combate.combateFSM(state);

            elif(estadoAtual == state.logOptions):
                print("Suas opcoes sao:")
                for x in salaAtual.directions:
                    print(x)
                for x in salaAtual.actions:
                    print(x)

                inpt = input("O que voce faz?\n")
            elif estadoAtual == state.venceuCombate:
                print("parabens, voce venceu o combate!\n")
                self.inimigos = []

            #NEXT STATE LOGIC. le input e decide
            proximoEstado = estadoAtual

            if(estadoAtual == state.descreve):
                if(len(salaAtual.inimigos)>0):
                    proximoEstado = state.combateFSM
                else:
                    proximoEstado = state.logOptions

            elif(estadoAtual == state.combateFSM):
                proximoEstado = retornoCombate

            elif(estadoAtual == state.logOptions):
                if inpt in salaAtual.directions:
                    salaAtual = salaAtual.directions[inpt]
                    proximoEstado = state.descreve
                elif inpt in salaAtual.actions:
                    salaAtual.actions[inpt]()
                    proximoEstado = state.descreve

            elif estadoAtual == state.venceuCombate:
                proximoEstado = state.descreve


            #ATUALIZA ESTADO
            estadoAtual = proximoEstado

        return salaAtual
