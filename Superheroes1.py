from enum import Enum
import random
from re import X

class Humanont(Enum):
    HOMOSAPIENS = 0
    EXTRATERRESTRE = 1

    def compr(tipo):
        tipo = tipo.upper()
        s=None
        for c in Humanont:
            if c.name==tipo:
                s = c
                break
                
        if type(s) is not Humanont:
            raise TypeError("Tipo de variable inadecuada")
        return s

class Movimiento_Type(Enum):
    ATAQUE =1
    DEFENSA =0

class Movimientos_ayuda:
    def __init__(self,x,a,daño):
        self.nombre = x
        self.tipo = a
        self.daño =daño

    def get_nombre(self):
        return self.nombre
    def get_daño(self):
        return self.daño
    def get_tipo(self):
        return self.tipo
    def set_daño(self,x):
        self.daño = X

class Movimientos_definidos(Movimientos_ayuda):
    def __init__(self,x,a,daño,superheroe):
        super().__init__(x,a,daño)
        self.superheroe = superheroe

    def get_superheroe(self):
        return self.superheroe

class Superheroe:
    contador = 0

    def __init__(self,nombre,alias,tipo,escenario):
        if type(tipo) is not Humanont:
            raise TypeError("Tipo de variable inadecuada")
        self.nombre = nombre
        self.alias = alias
        self.tipo = tipo
        self.id = Superheroe.contador
        self.movimientos = []

        if tipo.value:
            self.parrila_poderes = [random.randint(4,6),random.randint(1,7),random.randint(1,7),random.randint(3,7),random.randint(1,7),random.randint(3,6)]
        else:
            self.parrila_poderes = [random.randint(3,7),random.randint(1,6),random.randint(2,5),random.randint(2,5),random.randint(1,6),random.randint(1,7)]
        
        self.coste = (escenario.get_monedas()/escenario.get_miembros())*(sum(self.parrilla_poderes)/30)
        self.stamina = (escenario.get_stamina()*self.parrila_poderes[3])

        Superheroe.contador = Superheroe.contador+1
        


    def get_stamina(self):
        return self.stamina

    def get_tipo(self):
        return self.tipo

    def set_stamina(self,f):
        self.stamina = f
    
    def get_parrila_poderes(self):
        return self.parrila_poderes

    def get_movimientos(self):
        return self.movimientos

    def get_alias(self):
        return self.alias

    def get_id(self):
        return self.id

    def get_coste(self):
        return self.coste

    def is_alive(self):
        if self.stamina > 0:
            return True
        else:
            return False

    def die(self):
        self.stamina = 0

    def set_movimientos(self,x):

        for movimiento in x:
            if movimiento.get_tipo().value:
                movimiento.set_daño((movimiento.get_daño()/10)*(0.8*self.parrilla_poderes[1] + 0.25*self.parrilla_poderes[2] + 0.75*self.parrilla_poderes[5] + self.parrilla_poderes[4]))
            else:
                movimiento.set_daño((movimiento.get_daño()/10)*(self.parrilla_poderes[0] + 0.75*self.parrilla_poderes[2] + 0.25*self.parrilla_poderes[5] + 0.2*self.parrilla_poderes[1]))
            self.movimientos.append(movimiento)

    def fight_attack(self,defender,round):
        defender.fight_defense(self.movimientos[round].get_daño())

    def fight_attack(self,daño):
        self.stamina = self.stamina - daño
        if self.stamina<=0:
            self.die



