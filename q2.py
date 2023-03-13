num = int(input("Informe um número: "))

# Calculando a sequência de Fibonacci até que o próximo número seja maior que "num"
a, b = 0, 1
while b < num:
    a, b = b, a + b

# Verificando se "num" pertence à sequência
if b == num:
    print(num, "pertence à sequência de Fibonacci")
else:
    print(num, "não pertence à sequência de Fibonacci")
