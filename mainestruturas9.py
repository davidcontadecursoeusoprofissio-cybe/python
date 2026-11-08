nome = input("Digite seu nome:")
valor_pizza = float(input("Digite o valor:R$"))
tem_cupom = input("Possui cupom de fidelidade? (s/n):").lower()=='s'
borda = input("Escolha a borda(recheada/simples):").lower()
 
preco = valor_pizza *0.90 if tem_cupom else valor_pizza

if borda == "recheada":
    preco += 8.00
    mensagem = "Borda recheada adicionada com sucesso!"
    
elif borda == "simples":
    mensagem = "Borda simples escolhida."
    
else:
    mensagem = "Opção de borda não reconhecida."
    
print("\n---RESUMO DO PEDIDO DA PIZZA---")
print(f"Cliente:{nome}")
print(f"{mensagem} Valor total do pedido R${preco:.2f}")
 
 