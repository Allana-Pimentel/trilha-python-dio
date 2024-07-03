saldo = 500
print(saldo)

saldo = 200
print(saldo)

saldo += 10
print(saldo)

saldo -= 5
print(saldo)

saldo //= 2
print(saldo)

saldo /= 2
print(saldo)

saldo *= 10
print(saldo)

saldo %= 4
print(saldo)

saldo **= 2
print(saldo)

#meu exemplo
saldo += 500
print(saldo)

saque = input("Digite o valor do 1saque: ")
saque = int(saque)

for i in range(1000**1000):
    if saldo < saque:
        print("Saldo insuficiente")
        break

    else:
        saldo -= saque
        print("Saldo atual:", saldo)
        saque = input("Digite o valor do saque: ")
        saque = int(saque)
print("Fim do programa")    