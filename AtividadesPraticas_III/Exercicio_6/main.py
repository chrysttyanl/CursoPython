n = int(input("Verificar numeros primos ate: "))
mult=0

'''
x = 2
print("")
print("______RESULTADO WHILE_____")
print("")

while(x<=n) :
    if (n % count == 0):
        print("Múltiplo de",count)
        mult += 1

if(mult==0):
    print("É primo")
else:
    print("Tem",mult," múltiplos acima de 2 e abaixo de",n)

'''


print("")
print("______RESULTADO FOR RANGE_____")
print("")

#range([start], stop[, step])
for count in range(2,n):
    if (n % count == 0):
        print("Múltiplo de",count)
        mult += 1

if(mult==0):
    print("É primo")
else:
    print("Tem",mult," múltiplos acima de 2 e abaixo de",n)


