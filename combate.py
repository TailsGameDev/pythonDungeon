from enum import Enum
estadosCombate = Enum('state', 'anunciaCombate combate ataques nenhum')

class Combate:
    def __init__(self, personagem, inimigos):
        self.personagem = personagem
        self.inimigos = inimigos
        self.combatOptions = {
            "fugir" : estadosCombate.nenhum ,
            "atacar": estadosCombate.combate
        }

    def combateFSM(self, state):
        estadoAtual = estadosCombate.anunciaCombate
        retornoCombate = state.combateFSM
        inpt = ""
        while inpt != "q":
            #LOGICA DE SAIDAS
            if estadoAtual == estadosCombate.anunciaCombate:
                print("Ha um inimigo hostil na sala.")
                print(self.inimigos[0].nome + " estah se preparando "+
                "para atacar!")
            elif estadoAtual == estadosCombate.combate:
                print("Suas opcoes sao: ")
                for x in self.combatOptions:
                    print(x)
                inpt = input("O que voce faz?\n")
            elif estadoAtual == estadosCombate.ataques:
                self.personagem.atacar(self.inimigos[0])
                if(self.inimigos[0].vida <= 0):
                    del self.inimigos[0]
                else:
                    self.inimigos[0].atacar(self.personagem)


            #LOGICA DE PROXIMO ESTADO
            proximoEstado = estadoAtual
            if estadoAtual == estadosCombate.anunciaCombate:
                proximoEstado = estadosCombate.combate
            elif estadoAtual == estadosCombate.combate:
                if inpt == "atacar":
                    proximoEstado = estadosCombate.ataques
                elif inpt == "fugir":
                    return state.logOptions
            elif estadoAtual == estadosCombate.ataques:
                if(self.personagem.vida <= 0):
                    return state.morte
                elif(len(self.inimigos)>0):
                    proximoEstado = estadosCombate.combate
                else:
                    return state.venceuCombate

            #ATUALIZACAO
            estadoAtual = proximoEstado

        return retornoCombate #a ideia eh nunca chegar nessa linha
