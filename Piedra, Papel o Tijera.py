#INTRODUCCION AL PIEDRA PAPEL O TIJERA
#def  jugar ():
#    usuario  =  input ( "Elegí una opción: 'pi' para piedra, 'pa' para papel, 'ti' para tijera. \n " ). inferior ()
#    computadora  = alazar.elección ([ 'pi' , 'pa' , 'ti' ])
#
#    if  usuario  ==  computadora :
#        volver  '¡Empate!'
#
#    if  ganó_el_jugador ( usuario , computadora ):
#        volver  '¡Ganaste!'
#
#    volver  '¡Perdiste!'



import random

aleatorio = random.randrange(0, 3)
eligePc = ""
print("1)Piedra")
print("2)Papel")
print("3)Tijera")
opcion = int(input("Que elegis?: "))

if opcion == 1:
    eligeUsuario = "piedra"
elif opcion == 2:
    eligeUsuario = "papel"
elif opcion == 3:
    eligeUsuario = "tijera"
print("Elegiste: ", eligeUsuario)

if aleatorio == 0:
    eligePc = "piedra"
elif aleatorio == 1:
    eligePc = "papel"
elif aleatorio == 2:
    eligePc = "tijera"
print("PC eligió: ", eligePc)
print("...")
if eligePc == "piedra" and eligeUsuario == "papel":
    print("Ganaste, papel envuelve piedra")
elif eligePc == "papel" and eligeUsuario == "tijera":
    print("Ganaste, Tijera corta papel")
elif eligePc == "tijera" and eligeUsuario == "piedra":
    print("Ganaste, Piedra pisa tijera")
if eligePc == "papel" and eligeUsuario == "piedra":
    print("perdiste, papel envuelve piedra")
elif eligePc == "tijera" and eligeUsuario == "papel":
    print("perdiste, Tijera corta papel")
elif eligePc == "piedra" and eligeUsuario == "tijera":
    print("perdiste, Piedra pisa tijera")
elif eligePc == eligeUsuario:
    print("empate")