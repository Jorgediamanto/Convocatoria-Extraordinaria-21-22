from Organizaciones1 import Organizaciones
from enum import Enum
from Escenarios1 import Escenarios
from Superheroes1 import *
import random



# 60 nombres ya que el maximo de un equipo es 30 y solo hay dos equipos
Nombres_superheroes = [
"Michael", 
"David", 
"John", 
"James", 
"Robert", 
"Mark", 
"William", 
"Richard", 
"Thomas", 
"Jeffrey", 
"Steven", 
"Joseph", 
"Timothy", 
"Kevin", 
"Scott", 
"Brian", 
"Charles", 
"Paul", 
"Daniel", 
"Christopher", 
"Kenneth", 
"Anthony", 
"Gregory",
"Ronald", 
"Donald",
"Gary",
"Stephen", 
"Eric", 
"Edward", 
"Douglas",
"Todd",
"Patrick",
"George", 
"Keith",
"Larry", 
"Matthew", 
"Terry",
"Andrew", 
"Dennis", 
"Randy", 
"Jerry",
"Peter", 
"Frank", 
"Craig",
"Raymond", 
"Jeffery", 
"Bruce", 
"Rodney",
"Mike",
"Roger", 
"Tony",
"Ricky", 
"Steve", 
"Jeff", 
"Troy", 
"Alan", 
"Carl",
"Danny", 
"Russell",
"Chris", 
]


organizaciones = [ "A-Force","Avengers", "Mercs for Money", "League of Realms", "Strange Academy" ,"X-Men"]

var1 = input("Introduzca en que escenario desea competir. Hay 3 opciones: sanctum_sanctorum , stark_tower, xavier_school :  ")

escenario = Escenarios.from_str(var1)

alien_o_no = ["HOMOSAPIENS","EXTRATERRESTRE"]

superheroes = []
list_costes=[]
for i in range(0,60):

    tipo = alien_o_no[random.randint(0,1)]
    tipo = Humanont.compr(tipo)
    n11 = int(input("Deseas agregar un alias a los superheroes? 1 si 0 no: "))
    if n11==1:
        alias = input("introduzca el alias que desea que tenga el superheroe de nombre "+ Nombres_superheroes[i]+": ")
        superheroes.append(Superheroe(Nombres_superheroes[i],alias,tipo,escenario))
        list_costes.append(superheroes[i].get_coste())  
    else:
        superheroes.append(Superheroe(Nombres_superheroes[i],Nombres_superheroes[i],tipo,escenario))
        list_costes.append(superheroes[i].get_coste())  
    
      

organizacion = []

f = []

f.append(superheroes[0:10])
f.append(superheroes[10:20])
f.append(superheroes[20:30])
f.append(superheroes[30:40])
f.append(superheroes[40:50])
f.append(superheroes[50:60])




organizacion.append(Organizaciones("A-Force",f[0]))
organizacion.append(Organizaciones("Avengers",f[1]))
organizacion.append(Organizaciones("Mercs for Money",f[2]))
organizacion.append(Organizaciones("League of Realms",f[3]))
organizacion.append(Organizaciones("Strange Academy",f[4]))
organizacion.append(Organizaciones("X-Men",f[5]))



print("Estos son todos los superheroes de lso que puedes elegir: ")   
for x in organizacion:
    print(x.__str__()) 


monedas = [escenario.get_monedas(),escenario.get_monedas()]
superheroe1 = []
superheroe2 = []
superheroe3 = []

for x in range(0,2):
    while len(superheroe1)<escenario.get_miembros() and monedas[x] >= min(list_costes):
        num = int(input("Jugador " + str(x+1) + " elija un superheore de la lista por su número: "))
        if num not in superheroe3:
            superheroe1.append(superheroes[num])
            superheroe3.append(num)
            monedas[x] -= superheroes[num].get_coste()
        else:
            print("Ese superheroe ya ha sido elejido")
    superheroe2.append(superheroe1)
    print("Estos son los superheroes elegidos: ")
    for zzz in superheroe1:
        print(str(
                    zzz.get_id()) + ". Alias: " + zzz.get_alias() + ", Tipo:" + zzz.get_tipo().name + ", Coste:" + str(
                zzz.get_coste()) + ", Energia:" + str(zzz.get_stamina()) + "\n")

    superheroe1 = []


mov_list = []

mov_punetazo = Movimientos_ayuda("puñetazo", Movimientos_ayuda.ATAQUE, random.randint(0,15))
mov_list.append(mov_punetazo)
mov_navajazo = Movimientos_ayuda("navajazo", Movimientos_ayuda.ATAQUE, random.randint(0, 20))
mov_list.append(mov_navajazo)
mov_escudo = Movimientos_ayuda("Escudo", Movimientos_ayuda.DEFENSA, random.randint(0, 5))
mov_list.append(mov_escudo)
mov_abrazo_del_oso = Movimientos_ayuda("Abrazo del oso", Movimientos_ayuda.DEFENSA, random.randint(0, 12))
mov_list.append(mov_abrazo_del_oso)


for i in range(0,2):
    for superheroe in superheroe2[i]:
        list_mov = [int(x) for x in input("Los movimientos son: [0. puñetazo| 1. navajazo| 2. escudo| 3. abrazo del oso]. Elija " + str(escenario.get_movimientos()) + " movimientos, en base a su ID y separados por comas, para el superheroe " + superheroe.get_alias() + " ").split(",")]
        list_mov_esp = [Movimientos_ayuda(mov_list[list_mov[i]].get_nombre(), mov_list[list_mov[i]].get_tipo(), mov_list[list_mov[i]].get_daño(), superheroe) for i in range(0, min(escenario.get_movimientos(), len(list_mov)))]
        superheroe.set_movimientos(list_mov_esp)
        for mov in list_mov_esp:
            print(mov.get_nombre() + " " + mov.get_tipo().name + " daño: " + str(mov.get_daño()) + "\n")

    

    list_campobatalla = [None, None]
    list_organizaciones = [organizacion("Jugador1", superheroe2[0]), organizacion("Jugador2", superheroe2[1])]
    movement = 0
    while list_organizaciones[0].is_undefeated() and list_organizaciones[1].is_undefeated():
        for i in range(0,len(list_campobatalla)):
            if not list_campobatalla[i] or not list_campobatalla[i].is_alive():
                print("Jugador " + str(i+1) + " su superheroe ha sido derrotado, estos son los que le quedan")
                undefeated = list_organizaciones[i].get_restantes()
                for j in range(0, len(undefeated)):
                    print(str(j) + ". Alias: " + undefeated[j].get_alias() + "\n")
                suplente_sup = int(input("Elija un nuevo superheroe: "))
                list_campobatalla[i] = undefeated[suplente_sup]

        while list_campobatalla[0].is_alive() and list_campobatalla[1].is_vivo():
            list_campobatalla[0].fight_attack(list_campobatalla[1], movement)
            list_campobatalla[1].fight_attack(list_campobatalla[0], movement)
            movement = 0 if movement == escenario.get_movimientos() - 1 else movement + 1
            print("Esta es la energia del jugador 1: "+str(list_campobatalla[0].get_stamina())+ " y esta la del jugador 2: "+str(list_campobatalla[1].get_stamina()))

    if list_organizaciones[0].is_undefeated():
        print("¡Ha ganado el jugador 1!")

    elif list_organizaciones[1].is_undefeated():
        print("¡Ha ganado el jugador 2!")

    else:
        print("Ha habido un empate")


