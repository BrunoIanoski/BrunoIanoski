# M(juros compostos) = montante final, C = capital inicial (valor investido ou emprestado inicialmente), i = taxa de juros por período (em decimal, por exemplo, 5% = 0,05), 
# t = número de períodos de capitalização (meses, anos, etc.)

c = float(input('Insira o valor que deseja investir: '))
meses = int(input('Insira em quantos meses deseja calcular: '))

taxa_selic = 0.1475 
taxa_cdi_anual = 0.1465
cdi_mercado_pago = 1.20

taxa_mensal = (1 + taxa_cdi_anual) ** (1/12) - 1
i = taxa_mensal * cdi_mercado_pago

juros_compostos = c * (1+i) ** meses
retorno = juros_compostos - c

juros_compostos = round(juros_compostos,2)
retorno = round(retorno,2)

print(f'\n🟢 Valor investido: R$ {c:,.2f}')
print(f'📈 Montante final após {meses} meses: R$ {juros_compostos:,.2f}')
print(f'💰 Retorno (juros ganhos): R$ {retorno:,.2f}')


# Fórmula de Juros Compostos: M = C * (1 + i)^t
# C = capital inicial
# i = taxa de juros mensal (em decimal)
# t = tempo em meses

# Entradas do usuário
c = float(input('Insira o valor que deseja investir: R$ '))
meses = int(input('Insira em quantos meses deseja calcular: '))

# Parâmetros financeiros
taxa_cdi_anual = 0.1465       # CDI de 14,65% ao ano (em decimal)
percentual_cdi = 1.20         # 120% do CDI

# Aplica os 120% sobre o CDI anual
taxa_anual_ajustada = taxa_cdi_anual * percentual_cdi

# Converte a taxa anual ajustada para taxa mensal composta
i = (1 + taxa_anual_ajustada) ** (1 / 12) - 1

# Calcula o montante com juros compostos
montante = c * (1 + i) ** meses
retorno = montante - c

# Arredondamento
montante = round(montante, 2)
retorno = round(retorno, 2)

# Saída formatada
print(f'\n🟢 Valor investido: R$ {c:,.2f}')
print(f'📅 Prazo: {meses} meses')
print(f'📈 Montante final: R$ {montante:,.2f}')
print(f'💰 Retorno (juros ganhos): R$ {retorno:,.2f}')

