from random import randint
from personagem import *

class Arma:
    def __init__ (self, personagemEquipando):
        self.personagem = personagemEquipando
    def atk(self):
        return self.personagem.strength

class Espada(Arma):
    def atk(self):
        return self.personagem.strength + 3 + randint(1,8)

class Clava(Arma):
    def atk(self):
        return self.personagem.strength + 5 + randint(1,4)
