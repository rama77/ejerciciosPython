#Leer  dos  números  naturales  A  y  B.  Calcular  A^B mediante  productos  sucesivos  y  mostrar  el resultado. Ejemplo: 4^3 = 4 *4 *4 (4 multiplicado 3 veces).
num1 = int (input("ingrese un numero: "))
num2 = int (input("Ingrese otro numero: "))
producto = 1

for x in range (num2+1):
    if x != 0:
        producto *= num1

print (producto)

