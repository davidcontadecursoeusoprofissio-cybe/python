preco_produto = 200
cliente_eh_vip = True
categoria = "eletronicos"

preco = preco_produto *0.80 if cliente_eh_vip else preco_produto
# 200 x 0.80 = 160.0 20% de desconto
if categoria == "Vestuario":
    # 160.0 x 0.70 = 112.0 = 30% de desconto 100% - 70% = 30%
    preco *= 0.70
    mensagem = "Super promoção de vestuário aplicada!"
    
elif categoria == "eletronicos":
    # 160.0 x 0.95 =152.0 5% de desconto
    preco *=0.95
    mensagem = "Desconto leve de eletrônicos aplicado."
    
else:
    mensagem = "Preço regular para esta categoria."
    
print(f"{mensagem} Preço final a pagar: R${preco:.2f}")