masa = int(input('ingrese su peso en kilos(kg): '))
altura = int(input('ingrese su altura en centímetros(cm): '))
print('su índice de masa corporal es: ' + str(int((masa/pow((altura/100),2.0)))))