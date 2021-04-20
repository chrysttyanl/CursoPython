ip = str(input('Digite um endereço IP: '))
ip_endereco = int((ip[:3]))

if (ip_endereco <= 127):

    print("O IP digitado é de classe =>A")

elif (ip_endereco > 127 and ip_endereco <= 191):

    print("O IP digitado é de classe =>B")

elif (ip_endereco > 191 and ip_endereco <= 223):

    print("O IP digitado é de classe =>C")

elif (ip_endereco > 223 and ip_endereco <= 239):

    print("O IP digitado é de classe =>D")

elif (ip_endereco > 240):

    print("O IP digitado é de classe =>E")