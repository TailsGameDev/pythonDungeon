from enum import Enum
state = Enum('state', 'descreve logOptions')

class Sala:
    #python nao permite construtores multiplos, mas permite default value
    def __init__ (self, desc= "batata"):
        self.descricao = desc
        self.directions = {}
        self.itens = {}

    def salaFSM(self, salaAtual):
        estadoAtual = state.descreve
        inpt = ""
        while(inpt != "quit" and inpt != "q"):
            #SAIDAS, PRINTS, INPUTS
            if(estadoAtual == state.descreve):
                print('\n'+salaAtual.descricao)

            elif(estadoAtual == state.logOptions):
                print("Suas opcoes sao:")
                for x in salaAtual.directions:
                    print(x)
                for x in salaAtual.itens:
                    print(x)
                inpt = input("O que voce faz?\n")

            #NEXT STATE LOGIC. le input e decide
            proximoEstado = estadoAtual

            if(estadoAtual == state.descreve):
                proximoEstado = state.logOptions

            elif(estadoAtual == state.logOptions):
                if inpt in salaAtual.directions:
                    salaAtual = salaAtual.directions[inpt]
                    proximoEstado = state.descreve
                elif inpt in salaAtual.itens:
                    salaAtual.itens[inpt]()
                    proximoEstado = state.descreve
            #ATUALIZA ESTADO
            estadoAtual = proximoEstado

        return salaAtual
