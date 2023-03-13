faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento_por_estado.values())

# Calculando o percentual de cada estado no faturamento total
percentuais = {}
for estado, faturamento in faturamento_por_estado.items():
    percentuais[estado] = (faturamento / faturamento_total) * 100

# Resultados
print("Representação do faturamento mensal:")
for estado, percentual in percentuais.items():
    print(estado+":", round(percentual, 1),"%")
