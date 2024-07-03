opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")

#minhas anotações
for numero in range(10):
    if numero == 10:
        break
    if numero % 2 == 0:
        print("numero par")
    else:
        print("numero impar")

    print(numero)
    