nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
numero = int(input("Qual seu número?"))
atendimento = input("Qual o problema?(vacinação/atendimento medico):").lower()

atencao = numero if(idade <=50 or idade >= 50) else idade

if idade == "vacinação":
    mensagem ="Por favor sala número um"
    atencao = "fila de vacinação"
    
elif idade == "atendimento":
    mensagem = "Por favor sala número um"
    atencao = "Prioridade"
    
else:
    mensagem = "Fila normal"
    
print("\n---RESUMO---")
print(f"nome{nome}({numero}número)")
print(f"{mensagem}Agradecemos a atenção")