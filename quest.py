from functions import *

def questao_1():
    frase = input('Digite uma frase: ').lower()
    palavra = input('Digite uma palavra pra buscar: ').lower()

    busca_palavra = frase.split()

    contador = 0
    
    for i in busca_palavra:
        if i == palavra:
            contador += 1
    
    print(contador)

######################################################################################

def questao_2():
    print('Conversor de Temperaturas')
    print('1 - Celsius p/ Fahrenheit')
    print('2 - Fahrenheit p/ Celsius')

    opc = int(input('Digite a opção que deseja: '))

    if opc == 1:
        celsius = float(input('Digite a temperatura que deseja converter: '))
        print(f'Temperatura convertida: {celsius_fahrenheit(celsius):.1f}F')
    elif opc == 2:
        fahrenheit = float(input('Digite a temperatura que deseja converter: '))
        print(f'Temperatura convertida: {fahrenheit_celsius(fahrenheit):.1f}C')
        
    else:
        print('Opção Inválida')

######################################################################################

def questao_3():
    usuarios = {
        'admin': '1234',
        'maria': 'abc@2025',
        'joao': 'senha123'
    }

    login = input('Digite o Usuário: ')
    senha = input('Digite a senha: ')

    if usuarios.get(login) == senha:
        print(f'Usuário Logado com Sucesso, Seja Bem-Vindo {login}')
    else:
        print('Usuário ou Senha Incorretos')

######################################################################################

def questao_4():
    numero = int(input('Digite um número pra verificar se ele é par ou ímpar: '))
    print(verificar_par_impar(numero))

######################################################################################

def questao_5():
    notas_aluno = []

    print("=== Controle de Notas ===")
    while True:
        entrada = input("Digite uma nota (ou 'sair' para encerrar): ")

        if entrada.lower() == "sair":
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas_aluno.append(nota)
            else:
                print("Digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número ou 'sair'.")

    if notas_aluno:
        print("\n--- Resultados ---")
        print(f"Média: {media(notas_aluno):.2f}")
        print(f"Maior: {maior(notas_aluno):.2f}")
        print(f"Menor: {menor(notas_aluno):.2f}")
    else:
        print("Nenhuma nota foi informada.")

######################################################################################

def questao_6():
    print('1 - Converter de Real p/ Dólar')
    print('2 - Converter de Dólar p/ Real')
    
    opcao = int(input('Digite a opção que deseja: '))
    valor = float(input('Digite o Valor que deseja converter: '))
    cotacao = float(input('Digite a cotação atual: '))

    if opcao == 1:
        print(f'R${valor:.2f} equivale a US${real_dolar(valor, cotacao):.2f}')
    elif opcao == 2:
        print(f'US${valor:.2f} equivale a R${dolar_real(valor, cotacao):.2f}')
    else:
        print('OPÇÃO INVÁLIDA')