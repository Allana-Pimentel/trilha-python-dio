texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

#usamos o for para iterar sobre um iterável, no caso, uma string. 
#Iterar é percorrer cada elemento de um objeto que pode ser percorrido, como uma string, lista, tupla, dicionário, etc.

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print("\n")  # adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
# usamos range para criar uma sequência de números que será iterada pelo for.
start = int(input("Informe o início: "))
stop = int(input("Informe o limite: "))
step = int(input("Informe o passo: "))

for numero in range(start, stop, step):
    print(numero, end=" ")  # adiciona uma quebra de linha

# Exemplo utilizando a função built-in range
number= int(input("\n\nInforme um número: "))
print(list(range(number), "\n"))
print(range(number), "\n")

