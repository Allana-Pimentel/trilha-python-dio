def sacar(saque):
    saldo = 500

    if saldo >= saque:
        print("Você sacou", saque,"!")
        print("retire o seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")


def depositar(saque):
    saldo = 500
    saldo += saque


sacar(200)
