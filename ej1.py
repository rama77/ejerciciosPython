#Leer un número correspondiente a un año e imprimir un mensaje indicando si es bisiesto o no. Se recuerda que un año es bisiesto cuando es divisible por 4. Sin embargo, aquellos años que sean divisibles por 4 y también por 100 no son bisiestos, a menos que también sean divisibles por 400. Por ejemplo, 1900 no fue bisiesto, pero sí el 2000.

#Version Alma
'''
año = int (input("Ingrese un año: "))
if año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
    print ("Es un año bisiesto")
elif año % 4 == 0 and año % 100 and año % 400 != 0:
    print ("No es un año bisiesto")
elif año % 4 == 0 and año % 100 != 0:
    print ("Es un año bisiesto")
else:
    print ("No es un año bisiesto")
'''
#Version Papi
while True:
    año = int (input("Ingrese un año: "))
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                print ("Es un año bisiesto")
            else:
                print ("No es un año bisiesto")
        else:
            print ("Es un año bisiesto")
    else:
        print ("No es un año bisiesto")