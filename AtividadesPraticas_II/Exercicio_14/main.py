numero1 = 1
numero2 = 2
numero3 = 1

if (numero1 < numero2 < numero3):

    print(numero1, numero2, numero3)

elif (numero1 < numero3 < numero2):

    print(numero1, numero3, numero2)

elif (numero2 < numero1 < numero3):

    print(numero2, numero1, numero3)

elif (numero2 < numero3 < numero1):

    print(numero2, numero3, numero1)

elif (numero3 < numero1 < numero2):

    print(numero3, numero1, numero2)

elif (numero3 < numero2 < numero1):

    print(numero3, numero2, numero1)

elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:

    print('Existe repetição de números!')