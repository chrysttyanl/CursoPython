n = int(input("Contar de 1 ao número digitado.\nDigite um número final: "))
interv = int(input("\nIntervalo será a quantidade pulada n1 para n2.\nDigite um número para intervalo: "))

'''
x = 1
print("")
print("______RESULTADO WHILE_____")
print("")

while(x<=n) :
    print(x)
    x+=interv
'''

print("")
print("______RESULTADO FOR RANGE_____")
print("")

#range([start], stop[, step])

for i in range(1,n,interv):
    print(i)

