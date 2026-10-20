nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
numero = int(input("Qual seu número?"))
atendimento = input("Qual o problema?(vacinação/atendimento medico):").lower()

atenção = numero if(idade < 50 or idade > 50) else idade

if idade == "vacinação":
    mensagem ="Por favor sala número um"