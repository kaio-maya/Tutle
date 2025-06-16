from meu_modulo import *
num1 = int(input("digite um numero:"))
num2 = int(input("digite outro numero: "))

while True:
    print("digite uma função:" "\n"
          "[1] soma" "\n"
          "[2] subtração" "\n"
          "[3] multiplicação""\n"
          "[4] divisão""\n"
          "[5] potenciação""\n"
          "[6] raiz quadrada" "\n"
          "[7] seno""\n"
          "[8] cosseno" "\n"
          "[9] tangente""\n"
          "[0] sair")
    opcao = int(input("digite uma função: "))
    if opcao == 1:
        print(f"a soma de {num1} + {num2} é { somar(num1, num2)}")
    elif opcao == 2:
        print(f"a subtração de {num1} - {num2}é {subtracao(num1, num2)}")
    elif opcao == 3:
        print(f"a multiplicação de {num1} * {num2} é {mutiplicacao(num1, num2)}")
    elif opcao == 4:
        print(f"a divisão de {num1} / {num2} é {divisao(num1, num2)}")
    elif opcao == 5:
        print(f"a potencia de {num1} elevado a {num2} é {potenciacao(num1, num2)}")
    elif opcao == 6:
        raiz_quadrada(num1, num2)
    elif opcao == 7:
        seno(num1, num2)       
    elif opcao == 8:
        cosseno(num1, num2)
    elif opcao == 9:
        tangente(num1, num2)
    else:
        break
