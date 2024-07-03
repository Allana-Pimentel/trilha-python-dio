# Comparações que retornam valores booleanos
saldo = 200
saque = input("Digite o valor do saque: ")
saque = int(saque)

#Tabela com comparações
print(saldo == saque)
print(saldo != saque)
print(saldo > saque)
print(saldo >= saque)
print(saldo < saque)
print(saldo <= saque)

# Operadores de comparação em exemplos
if saldo == saque:
    print("\nSaldo igual ao saque")
    print("\nVocê sacou", saque, "reais. Seu Saldo é", saldo - saque, "\n")
elif saldo < saque:
    print("\nNão é possivel retirar nenhum valor! \nSaldo Menor que o saque\n")
else:
    print("\nVocê sacou", saque, "reais\nSeu Saldo é", saldo - saque, "\n")
    saque = input("Digite o valor do saque: ")
    saque = int(saque)
