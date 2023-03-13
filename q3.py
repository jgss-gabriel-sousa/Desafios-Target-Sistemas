import json

# Lendo o arquivo JSON com os dados de faturamento
with open('faturamento.json') as file:
    dados = json.load(file)

# Extraindo os valores diários de faturamento
faturamento_diario = dados['faturamento_diario']

# Calculando o menor e o maior valor de faturamento diário
menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)

# Calculando a média mensal de faturamento, ignorando dias sem faturamento
soma_valores = sum(valor for valor in faturamento_diario if valor > 0)
media_mensal = soma_valores / len(faturamento_diario)

# Calculando o número de dias no mês em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = sum(valor > media_mensal for valor in faturamento_diario)

# Imprimindo os resultados
print("Menor valor de faturamento diário:", menor_valor)
print("Maior valor de faturamento diário:", maior_valor)
print("Número de dias com faturamento acima da média mensal:", dias_acima_da_media)
