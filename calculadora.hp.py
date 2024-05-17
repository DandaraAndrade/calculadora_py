'''
Calculadora.py
Aluno: Dandara Soares de Andrade
Data: 02/05/2024
Esta calculadora apresenta estilo similar ao HP, utilizando Python como linguagem de programção. Sua estrutura permite ao usuário 
escolher entre diferentes operações matemáticas (adição, subtração, multiplicação e divisão) 
e realizar cálculos repetidamente até que ele decida sair utilizando um comando básico.
O código utiliza de estruturas como if e while para o objetivo final.
'''
#importar estrutura matemática que ira ser utilizada para os cálculos.
import functools
#Criação de um menu para orientar o usuário com as funções disponíveis e a utilização do while para criar uma estrutura de repetição.
while True: 
    print(f"BEM-VINDO!")
    print(f"Opções de operações disponíveis:")
    print(f"1 - Adição")
    print(f"2 - subtração")
    print(f"3 - divisão")
    print(f"4 - multiplicação")

    #Solicitar as informações de entrada para realizar os cálculos.
    numero1 = float(input("Dígite um número inicial:"))
    operacao = input ("Dígite o número correpondente á operação:")

    #Estrutura para definir se as opções de operações são válidas e dar continuidade a entrada de informações.
    if operacao in ['1', '2', '3', '4']:
        numeros = []
        while True:
            valor = input("Digite um número ou 'P' para calcular o resultado final: ")
            if valor.upper() == 'P':
                break
            try:
                numeros.append(float(valor))
            except ValueError:
                print("Valor inválido! Por favor, insira um número válido.")

     #Desenvolvimento de uma estrutura if para realizar os cálculos base.
    if operacao == '1':
            resultado = numero1 + sum(numeros)
            print(f"Resultado da adição corresponde á {resultado}")
    elif operacao == '2':
            resultado = numero1 - sum(numeros)
            print(f"Resultado da subtração corresponde á {resultado}")
    elif operacao == '3':
            resultado = numero1 * functools.reduce(lambda x, y: x * y, numeros, 1)
            print(f"Resultado da multiplicação corresponde á {resultado}")
    elif operacao == '4':
            resultado = numero1 / functools.reduce(lambda x, y: x / y, numeros)
            print(f"O resultado da divisão corresponde á {resultado}")
    elif operacao == 'X':
            print(f"Finalizando á calculadora. Até á próxima!")
    else:
                print("Não foi possível realizar á operação. Por favor, utilizar números e operações válidas.")

    #finalização de uma operação e desligar a calculadora, ou dar continuidade a outra operação.
    opcao_continuar = input("Pressione Enter para continuar ou 'X' para sair: ")
    if opcao_continuar.upper() == 'X':
        print("Finalizando a calculadora. Até a próxima!")
        break



