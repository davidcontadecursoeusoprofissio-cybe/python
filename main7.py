nome = input("Seu nome:")
idade = int (input("sua idade:"))
salario = float(input("Digite sua pretensão salarial:R$"))

proximo_ano = idade + 1

print ("n---RESUMO CADASTRO---")
print (f"Nome:{nome}")
print (f"Idade:{idade}ano(terá:{proximo_ano})no ano que vem")
print(f"Pretensão salarial:R${salario:.2f}")


