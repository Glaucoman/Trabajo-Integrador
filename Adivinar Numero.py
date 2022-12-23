import random

intentos = 0

print ("JUEGO DE AZAR....")

print ("Cual es tu nombre?...")
nombre = input()

x = random.randint (1, 20)

print ("Hola " + nombre + ", Bienvenido a mi primer juego...." )

while intentos < 6:
    intentos = intentos + 1
print ("Elige un numero del 1 al 20")
numero = input()
numero = int (numero)
if numero < x:
    print ("Tu numero es mas bajo")
if numero > x:
    print ("Tu numero es mas alto")
if numero == x:

    if numero == x:
        print ("Eres un genio....")
    print (nombre + " lo lograste con %d intentos" % (intentos))
    print ("Nos vemos....")

if numero != x:
    print ("Has perdido, sera en otra oportunidad...")
    print ("Nos vemos")