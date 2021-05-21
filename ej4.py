#Ingresar por teclado la cantidad de términos a generar de la siguiente serie: 1 7 19 43 91 187 379 763 1531 3067 6139 El primer término es el 1 y cada término se genera como el doble del término anterior más 5. Mostrar la serie por pantalla e informar la suma de los términos generados.

numero = int (input("ingrese un numero: "))
cantidad = int (input("ingrese la cantidad de veces que se va a repetir la serie: "))
producto = 0
resultado = 0

for x in range (cantidad + 1):
    producto = numero * 2 
    resultado = producto + 5
    
print (resultado)


terminos = int (input("ingrese la cantidad de terminos: "))
serie = []
suma = 0

for x in range (terminos):
    if x == 0:
        serie.append(1)
        suma = 1
        valor = 1
    else:
        valor = valor*2+5
        serie.append(valor)
        suma += valor

print("Serie: " + str(serie))
print("Suma: " + str(suma))




