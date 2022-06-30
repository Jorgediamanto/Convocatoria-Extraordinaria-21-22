from enum import Enum

class ayuda_enum(Enum):
    sanctum_sanctorum = [10000,10,10,100]
    stark_tower = [20000,20,25,200]
    xavier_school = [80000,30,40,300]

class Escenarios:
    
    def __init__(self,monedas,miembros,movimientos,stamina):
        self.monedas=monedas
        self.miembros=miembros
        self.movimientos=movimientos
        self.stamina=stamina

    def get_monedas(self):
        self.monedas
    def get_miembros(self):
        self.miembros
    def get_movimientos(self):
        self.movimientos
    def get_stamina(self):
        self.stamina




    def from_str(escenario):
        escenario=escenario.lower()
        s=None
        for c in ayuda_enum:
            if c.name == escenario:
                z=c.value
                s=Escenarios(z[0],z[1],z[2],z[3])
                break

        if type(s) is not Escenarios:
            raise TypeError("Tipo de variable inadecuada")

        return s