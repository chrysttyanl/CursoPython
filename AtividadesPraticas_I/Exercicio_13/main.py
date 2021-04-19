dia = int(input("Digite quantidade de dias: "))
horas = int(input("Digite quantidade de horas: "))
minutos = int(input("Digite quantidade de minutos: "))
segundos = int(input("Digite quantidade de segundos: "))

diaSeg = (((dia * 24) * 60) * 60)
horasSeg = ((horas * 60) * 60)
minutosSeg = (minutos * 60)
resultado = diaSeg + horasSeg + minutosSeg + segundos

print("")
print("____________RESULTADO____________")
print("")
print("%i dia para segundo = %i\n%i hora para segundo = %i\n%i minutos para segundo = %i\n%i segundos  = %i\nO Total de segundos é igual: %i" %(dia, diaSeg, horas, horasSeg,minutos, minutosSeg, segundos, segundos, resultado))