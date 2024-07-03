# Title: Formatação de Strings

# %s - String
# %d - Inteiro
# %f - Float
# %r - Qual
# %x - Hexadecimal

nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))

#Aqui podemos tirar de ordem e mesmo assim o indice informa a ordem
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

#Aqui podemos usar o dicionario, argumentos em forma nomeada
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))

print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")
