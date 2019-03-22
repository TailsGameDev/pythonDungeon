from Armas import Arma
from Armaduras import Armadura

class Personagem:
    def __init__ (self, name = "fulano", vvida = 10, vstrength = 5, vdefesa = 4):
        self.nome = name

        self.vida = vvida

        self.strength = vstrength
        desarmado = Arma(self)
        self.atk = desarmado.atk

        self.defesa = vdefesa
        semArmadura = Armadura(self)
        self.defender = semArmadura.defender

    def equipar(self, arma):
        arma.personagem = self;
        self.atk = arma.atk

    def atacar(self, atacado):
        dmg = atacado.defender(self.atk())
        if (dmg > 0):
            atacado.vida = atacado.vida - dmg
            print("O ataque infligiu " + str(dmg) + " de dano.")
        else:
            print("Nao houve dano.")
