nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
preco_ingresso = 40.0
tipo_sessao = input("Escolha o tipo de sessão(3d/normal):").lower()


preco = preco_ingresso*0.50 if(idade < 18 or idade >60)else preco_ingresso

if tipo_sessao == "3d":
    preco *=1.20#taxa 20% preco * 1.20
    mensagem = "Sessão 3D selecionada(taxa aplicada)."
    
elif tipo_sessao =="normal":
    mensagem = "Sessão normal sem taxas extras."
else:
    mensagem = "Sessão normal inválido, cobrando valor padrão."
    
print("\n---RESUMO DO CINEMA---")
print(f"Cliente:{nome}({idade}anos)")
print(f"{mensagem}Total do ingresso:R${preco:.2f}")