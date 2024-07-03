saldo = 2000
saque = 2500

# caso o saque seja maior que saque será sucesso, caso contrário falha

#condição atendida  -    condição -       condição não atendida
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
