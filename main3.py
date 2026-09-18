nome=input("Digite seu nome:")
idade =int(input("Digite sua idade:"))
salario=float(input("Digite sua pretensão salarial:R$"))

proximo_ano= idade + 1

print("n---RESUMO DO CADASTRO---")
print(f"Nome:{nome}")
print(f"Idade atual:{idade}anos(terá:{proximo_ano}anos no ano que vem)")
print(f"Pretensão Salarial:R${salario:.2f}")