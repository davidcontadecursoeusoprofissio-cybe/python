nome = input("Digite o nome:")
preco_livro = float(input("Valor do livro:R$"))
membro_clube = input("É membro do clube do livro?(s/n):").lower()=='s'
genero = input("Escolha o gênero(ficcao/tecnico):").lower()

preco =preco_livro *0.75 if membro_clube else preco_livro

if genero =="ficcao":
    preco *= 0.95
    mensagem = "Desconto promocional de ficção aplicado!"
    
elif genero =="tecnico":
    preco *=0.90
    mensagem ="Desconto especial para livro técnicps aplicado!"
    
else:
    mensagem ="Preço regular para este gênero."
    
print("\n---RESUMO DA LIVRARIA---")
print(f"Leitor(a):{nome}")
print(f"{mensagem} Valor final do livro:R${preco:.2f}")


