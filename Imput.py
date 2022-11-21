
horasTrabajadas=input('Introduzca las horas que trabajo \n')
try:
    horasTrabajadas=float(horasTrabajadas)
except:
    print('Error por favor ingrese un numero')
    exit()
tarifaHora=input('Introduzca la tarifa \n')
try:
    tarifaHora=float(tarifaHora)
except:
    print('Error por favor ingrese un numero')
    exit()
salario=tarifaHora*horasTrabajadas
if horasTrabajadas>40:
    salario=40*tarifaHora+1.5*(horasTrabajadas-40)*tarifaHora
print(salario)
