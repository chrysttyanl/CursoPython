
qt = 0
sm = 0
'''
x = 0
print("")
print("______RESULTADO WHILE_____")
print("")

while(x<=100) :
    print(x)
    x+=2
'''


print("")
print("______RESULTADO FOR RANGE_____")
print("")

#range([start], stop[, step])

for i in range(0,100,2): #Imprime os números pares, ser ímpares inicia com 1
    sm+=i
    print(i)
    qt+=1
print("Quantidade de elemento: %i\nSoma dos elementos: %i" %(qt, sm))
