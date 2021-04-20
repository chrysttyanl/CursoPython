data = input('Digite uma data no formato dd/mm/aaaa: ')



if len(data) == 10:

    if data[2] == '/' and data[5] == '/':

        dia = (data[0] + data[1])

        mes = (data[3] + data[4])

        ano = (data[6] + data[7] + data[8] + data[9])



        if dia.isnumeric() == True and mes.isnumeric() == True and ano.isnumeric() == True:

            numero_dia = int(dia)

            numero_mes = int(mes)

            numero_ano = int(ano)

            if numero_ano > 0:

                if numero_mes > 0 and numero_mes <= 12:

                    if numero_dia > 0 and numero_dia <= 31:

                        print(f'A data {data} foi validada com sucesso!')

                    else:

                        print('Houve um erro. O valor digitado não é valido para o formato de data.')

                else:

                    print('Houve um erro. O valor digitado não é valido para o formato de data.')

            else:

                print('Houve um erro. O valor digitado não é valido para o formato de data.')

        else:

            print('Houve um erro. O valor digitado não é valido para o formato de data.')

    else:

        print('Houve um erro. O valor digitado não é valido para o formato de data.')

else:

    print('Houve um erro. O valor digitado não é valido para o formato de data.')