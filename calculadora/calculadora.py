def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def calculadora():
    print('Calculadora')
    print('Escolha uma opção:')
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')

    opcao = input('Digite uma opção:')

    if opcao == '1':
        num1 = float(input('Digite o primeiro número:'))
        num2 = float(input('Digite o segundo número:'))
        resultado = soma(num1, num2)
        print('Resultado:', resultado)

    elif opcao == '2':
        num1 = float(input('Digite o primeiro número:'))
        num2 = float(input('Digite o segundo número:'))
        resultado = subtracao(num1, num2)
        print('Resultado:', resultado)

    elif opcao == '3':
        num1 = float(input('Digite o primeiro número:'))
        num2 = float(input('Digite o segundo número:'))
        resultado = multiplicacao(num1, num2)
        print('Resultado:', resultado)

    elif opcao == '4':
        num1 = float(input('Digite o primeiro número:'))
        num2 = float(input('Digite o segundo número:'))
        resultado = divisao(num1, num2)
        print('Resultado:', resultado)

    else:
        print('Opção invalida. Tente novamente.')


calculadora()