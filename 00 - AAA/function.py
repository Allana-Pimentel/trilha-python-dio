class financeiro:
    
    months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    month = input("Digite o mês: ")
    if month not in months:
        print("Mês inválido")

    salario = input("Digite o salário: ")
    if salario is not float or salario < 0:
        print("Salário inválido")
    else:
        salary = float(salario)
    
    cartao = input("Digite quanto está o cartão 1: ")
    if cartao is not float or cartao < 0:
        print("Valor inválido")
    else:
        card = float(cartao)

    income = [salario]
    outcome = [cartao]
    saldo = income - outcome
    sum_income = sum(income)
    sum_outcome = sum(outcome)
    porcentagem_utilizada = (sum_outcome / sum_income) * 100
  

    def __init__(self, income, outcome):
        self.income = income
        self.outcome = outcome

    def __str__(self) -> str:
        return f"{self.income} - {self.outcome} - {self.saldo} - {self.porcentagem_utilizada}"
