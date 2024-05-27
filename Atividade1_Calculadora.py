import os

def apresentando():
    print('Bem vindo à Calculadora Digital')

def opcoes():
    print("""Escolha uma opção para realizar uma operação:
            \n1. Soma
            \n2. Subtração
            \n3. Divisão
            \n4. Multiplicação
            \n5. Sair""")

def escolhendo_operacao():
    while True:
        opcao_escolhida = int(input("Digite a opção: "))

        if opcao_escolhida == 1:
            soma()
        elif opcao_escolhida == 2:
            subtrair()
        elif opcao_escolhida == 3:
            dividir()
        elif opcao_escolhida == 4:
            multiplicar()
        elif opcao_escolhida == 5:
            finalizar_programa()
            break
        else:   
            print("Opção inválida. Por favor, escolha uma opção válida.")

def soma():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    resultado = numero1 + numero2
    print("Resultado:", resultado)

def subtrair():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    resultado = numero1 - numero2
    print("Resultado:", resultado)

def dividir():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    if numero2 != 0:
        resultado = numero1 / numero2
        numero = resultado
        formato = "Resultado: {:,.2f}".format(numero)
        print(formato)
    else:
        print("0")

def multiplicar():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    resultado = numero1 * numero2
    print("Resultado:", resultado)

def finalizar_programa():
    os.system('cls')  
    print('Programa finalizado.')

def main():
    apresentando()
    while True:
        opcoes()
        escolhendo_operacao()

if __name__ == '__main__':
    main()


    
