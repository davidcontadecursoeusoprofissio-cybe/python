nome = input("Digite seu nome:")
preco_base = float(input("Digite o preço base do jogo:R$"))
eh_assinante = input("É assinante da plataforma?(s/n):").lower()=='s'
plataforma = input("Escolha a plataforma(pc/console):").lower()

preco = preco_base *0.85 if eh_assinante else preco_base   #15 porcento de desconto
# preco_base * 0.85
if plataforma == "pc":
    preco *=0.90  #10 porcento de desconto
    mensagem = "Desconto especial de PC aplicado!"
    
elif plataforma == "console":
    preco *=0.95 #5 porcento de desconto
    mensagem ="Plataforma padrão selecionada."
    
print("\n---RESUMO DA COMPRA DE GAMES---")
print(f"Comprador:{nome}")
print(f"{mensagem}Preço final a pagar:R${preco:.2f}")