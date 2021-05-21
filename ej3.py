#Realizar un programa que calcule el factorial de un numero. Ejemplo : Factorial de 6 (6*5*4*3*2*1 = 720)

numero = int (input("ingrese un numero: "))
lista = []
producto = 0

for x in range (numero + 1):
    lista.append (x)

print (lista)



numero = int (input("ingrese un numero: "))
producto = 1

for x in range (numero + 1):
    if x != 0:
        producto *= x
print ("Papi: " + str(producto))