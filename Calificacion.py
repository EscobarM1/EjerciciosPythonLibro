Calificacion=input('Ingrese una calificacion de 0.0 a 1.0 \n')
try:
    Calificacion=float(Calificacion)
    if  Calificacion<0.0 or Calificacion>1.0: 
        print('Calificacion fuera de rango')
    elif Calificacion>=0.9:
        print('Calificacion sobresaliente')
    elif Calificacion>=0.8 and Calificacion<0.9:
        print('Calificacion Notable')
    elif Calificacion>=0.7 and Calificacion<0.8:
        print('Calificacion Bien')
    elif Calificacion>=0.6 and Calificacion<0.7:
        print('Calificacion Suficiente')
    elif Calificacion<0.6:
        print('Calificacion insuficiente')
except:
    print('Ingrese un valor numerico')