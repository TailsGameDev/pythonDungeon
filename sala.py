from enum import Enum
state = Enum('state', 'descreve anunciaCombate combate ataques ' +
'morte fugir logOptions')

class Sala:
    #python nao permite construtores multiplos, mas permite default value
    def __init__ (self, desc= "batata"):
        self.descricao = desc
        self.directions = {}
        self.actions = {}
        self.inimigos = []
        self.combatOptions = {"fugir" : state.fugir , "atacar": state.combate}

    def salaFSM(self, salaAtual, personagem):
        estadoAtual = state.descreve
        inpt = ""
        while(inpt != "quit" and inpt != "q"):
            #SAIDAS, PRINTS, INPUTS
            if(estadoAtual == state.descreve):
                print('\n'+salaAtual.descricao)

            elif(estadoAtual == state.anunciaCombate):
                print("Ha um inimigo hostil na sala.")
                print(salaAtual.inimigos[0].nome + " estah se preparando "+
                "para atacar!")

            elif(estadoAtual == state.combate):
                print("Suas opcoes sao: ")
                for x in salaAtual.combatOptions:
                    print(x)
                inpt = input("O que voce faz?\n")

            elif(estadoAtual == state.ataques):
                personagem.atacar(salaAtual.inimigos[0])
                if(salaAtual.inimigos[0].vida < 1):
                    del salaAtual.inimigos[0]
                else:
                    salaAtual.inimigos[0].atacar(personagem)

            elif(estadoAtual == state.logOptions):
                print("Suas opcoes sao:")
                for x in salaAtual.directions:
                    print(x)
                for x in salaAtual.actions:
                    print(x)

                inpt = input("O que voce faz?\n")

            #NEXT STATE LOGIC. le input e decide
            proximoEstado = estadoAtual

            if(estadoAtual == state.descreve):
                if(len(salaAtual.inimigos)>0):
                    proximoEstado = state.anunciaCombate
                else:
                    proximoEstado = state.logOptions

            elif(estadoAtual == state.anunciaCombate):
                proximoEstado = state.combate

            elif(estadoAtual == state.combate):
                if(len(salaAtual.inimigos)>0):
                    proximoEstado = state.combate
                else:
                    proximoEstado = state.descreve

            elif(estadoAtual == state.ataques):
                if(personagem.vida < 1):
                    proximoEstado = state.morte
                elif(len(salaAtual.inimigos)>0):
                    proximoEstado = state.combate
                else:
                    proximoEstado = state.descreve

            elif(estadoAtual == state.logOptions):
                if inpt in salaAtual.directions:
                    salaAtual = salaAtual.directions[inpt]
                    proximoEstado = state.descreve
                elif inpt in salaAtual.actions:
                    salaAtual.actions[inpt]()
                    proximoEstado = state.descreve
            #ATUALIZA ESTADO
            estadoAtual = proximoEstado

        return salaAtual
