#As expressões aritméticas são avaliadas da seguinte forma da esquerda para a direita e de acordo com a seguinte ordem de precedência:
#1. Parênteses
#2. Exponenciação
#3. Multiplicação e Divisão
#4. Adição e Subtração
produto_1 = 20
produto_2 = 10
# Operadores aritméticos padrões
print("Soma:", produto_1 + produto_2)
print("Subtração:", produto_1 - produto_2)
print("Divisão:", produto_1 / produto_2)
# Operadores aritméticos adicionais
print("Divisão Inteira(Resultado não volta quebrado, volta em int)", produto_1 // produto_2) # divisão inteira - numero int volta e não o float - ex: 5 // 2 = 2 e não 2.5
print("Multiplicação:", produto_1 * produto_2)
print("Módulo(resto da divisão):", produto_1 % produto_2) # MODULO - resto da divisão
print("Exponenciação:", produto_1 ** produto_2) # Exponenciação numero elevado a outro numero
x = (1 + 5) ** 4
y = (10 / 2) + 25 * ((2 - 2) ** 2)
print(x)
print(y)