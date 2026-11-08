nome = input("Digite seu nome:")
mensalidade_base = 120.0
eh_veterano = input("Você já é aluno antigo?(s/n):")=='s'
modalidade = input("Escolha a modalidade(musculacao/natacao):").lower()

preco =mensalidade_base *0.80 if eh_veterano else mensalidade_base

if modalidade == "natacao":
    preco +=40.00
    mensagem = "Plano de natação ativada."
    
elif modalidade == "musculacao":
    mensagem = "Plano de musculação padrão ativada."
    
else:
    mensagem = "Modalidade padrão aplicada."
    
print("\n---RESUMO DA MATRÍCULA---")
print(f"Aluno{nome}")
print(f"{mensagem}Mensalidade a pagar:R${preco:.2f}")