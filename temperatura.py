tempCels=input('Ingrese la temperatura en grados Celsius \n')
try:
    tempFaren=float(tempCels)*(9/5)+32
    print('La temperatura en grados Farenheit es de ' + str(tempFaren))
except:
    print('Introduzca un caracter valido')
