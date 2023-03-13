string = input("Informe uma string: ")

# Convertendo a string em uma lista de caracteres
caracteres = list(string)

# Invertendo os caracteres da lista
for i in range(len(caracteres) // 2):
    temp = caracteres[i]
    caracteres[i] = caracteres[len(caracteres) - 1 - i]
    caracteres[len(caracteres) - 1 - i] = temp

# Convertendo a lista de caracteres de volta para uma string
string_invertida = "".join(caracteres)

print(string_invertida)