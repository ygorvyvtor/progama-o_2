from quest import *

while True:

    questao = int(input('Digite o numero da Questão 1 até 6 ou Digite 0 p/ Sair: '))

    if questao == 0:
        print('DEIXANDO DO PROGRAMA...')
        break
    elif questao == 1:
        questao_1()
    elif questao == 2:
        questao_2()
    elif questao == 3:
        questao_3()
    elif questao == 4:
        questao_4()
    elif questao == 5:
        questao_5()
    elif questao == 6:
        questao_6()
    else:
        print('[ERRO] OPÇÃO INVÁLIDA')