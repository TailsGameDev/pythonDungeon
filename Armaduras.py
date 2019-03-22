from random import randint

class Armadura:
    def __init__ (self, personagemEquipando = "nenhum"):
        if (personagemEquipando == "nenhum"):
            personagemEquipando = Personagem()
        self.personagem = personagemEquipando
    def defender(self, personagem):
        return self.personagem.defesa

class ArmaduraDeCouro(Armadura):
    def defender(self, atk):
        return atk - self.personagem.defesa + 3

class ArmaduraDeMadeira(Armadura):
    def defender(self, atk):
        return atk - self.personagem.defesa + 5
