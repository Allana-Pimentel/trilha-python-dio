for i in range(1000**1000):
    
    Menu = input("\n\nDigite 1 para inserir os valores ou 2 para sair: ")
    if Menu == "1":
            
            salario = input("\n\nDigite o salário: ")
            salary = float(salario)

            beneficios = input("Digite os benefícios: ")
            benefits = float(beneficios)

            Outros = input("Digite outros ganhos: ")
            others = float(Outros)

            cartao = input("Digite quanto está o cartão 1: ")
            card = float(cartao)

            cartao2 = input("Digite quanto está o cartão 2: ")
            card2 = float(cartao2)

            investimentos = input("Digite quanto está o investimento: ")
            investments = float(investimentos)

            # Calcula a soma das entradas e saídas
            income = [salary, benefits, others]
            sum_income = sum(income)
            outcome = [card, card2, investments]
            sum_outcome = sum(outcome)

            # Calcula o saldo
            saldo = income - outcome
            print("\nSeu saldo é: " + str(saldo))

            # Calcula a porcentagem utilizada
            porcentagem_utilizada = (sum_outcome / sum_income) * 100

            # Calcula se os investimentos estão acima de 30%
            if investments > 0.3 * sum_income:
                print("\nSeus investimentos estão acima de 30% do seu salário\n")
            else:
                print("\nSeus investimentos estão abaixo de 30% do seu salário\n")

            # Verifica a porcentagem utilizada
            if porcentagem_utilizada > 70:
                print("\nVocê utilizou mais de 70% do seu salário")
                print("Você utilizou " + str(porcentagem_utilizada) + "% do seu salário\n")
            else:
                print("Você utilizou " + str(porcentagem_utilizada) + "% do seu salário\n")

    else:
        print("Saindo...")
        exit()