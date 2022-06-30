from enum import Enum
from Superheroes1 import Superheroe

class Organizaciones:
    def __init__(self,organizacion,integrantes):
        if type(organizacion) is not str:
            raise TypeError("Tipo de variable inadecuada")

        if type(integrantes) is not list:
            raise TypeError("Tipo de variable inadecuada")

        self.organizacion = organizacion
        self.integrantes = integrantes
        

    def get_organizacion(self):
        return self.organizacion

    def get_integrantes(self):
        return self.integrantes

    def set_integrantes(self,integrantes_updated):
        self.integrantes = integrantes_updated

    def  is_undefeated(self):
        z=0
        for x in self.integrantes:
            if x.get_stamina() > 0:
                z=1
        if z==1:
            return True

        else:
            return False

    def  surrender(self):
        for x in self.integrantes:
            x.set_stamina(0)

    def __str__(self):
        f = ""
        for x in self.integrantes:
            f= f+x.get_alias()+" with a "+x.get_movimientos()+" and health: "+x.get_stamina() + "\n"

        return f

    def __repr__(self):
        t=""
        for x in self.integrantes:
            t= t+x.get_id()+ "\n"
     

    def get_restantes(self):
        sup_restantes = []
        for i in range(0,len(self.integrantes)):
            if self.integrantes[i].is_alive():
                sup_restantes.append(self.integrantes[i])
        return sup_restantes
            



