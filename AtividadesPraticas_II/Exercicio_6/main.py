import re
entrada = input("Digite algo: ")

if re.match('^\d+$', entrada):
    print("Inteiro")
elif re.match('^\d+\.\d+$', entrada):
    print("Decimal")
else :
    print("Texto")
