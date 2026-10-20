nome = input("Digite o nome do livro:")
numero = int(input("Número do livro:"))
valor_livro =40.0
tipo_livro = input("Escolha o tipo do livro(terror/ação):").lower()      

valor = valor_livro*0.90 if(numero < 28 or numero >150)else valor_livro

if tipo_livro == "terror":
    valor *=0.90 # %100 - %90 = 10 = então ficar 0.90 ou dez por cento de desconto
    mensagem = "Desconto do dia."   
    
    
elif tipo_livro == "ação":
    
    mensagem = "Sem desconto nesse livro."
    
else:
    mensagem ="Valor normal."
    
print("\n---RESUMO DO LIVRO---")
print(f"livro:{nome}({numero}número)")
print(f"{mensagem}total do livro:R${valor:.2f}")
                                      