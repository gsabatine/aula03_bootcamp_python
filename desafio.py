## Primeiro passo - inserir nome
nome = str(input("Digite seu nome: "))

## Segundo passo - inserir salário
salario = float(input("Insira seu salário: "))

## Terceiro passo - inserir % de bonus recebido
pct_bonus = float(input("Insira o percentual de bonus recebido: "))

## Calculo do KPI Bonus

bonus_recebido = 1000 + salario * pct_bonus

print(f"Olá {nome}, seu bonus foi de {bonus_recebido}")