#produtos=["Mouse","Teclado","Monitor","Notebook"]
#produto = input("Digite o produto:")

#if produto in produtos:
    #print("Produto disponível!")
#else:
    #print("Produto não disponível!")
    
    
    
#numeros=[10,20,30,40,50,]
#numero = int(input("Digite o número:"))

#if numero in numeros:
    #print("Existe esse número na lista")
#else:
    #print("Não existe esse número na lista")
    
    
    
#=====================================================


#animais = ["Cachorro","Porco"]

#novo_animal = input("Digite o novo animal:")
#animais.append(novo_animal)

#print("Novo anima adicionado!")
#print(animais)


#=======================================================

#produtos = ["pão","leite","café","ovo"]

#produto = input("Qual produto deseja remover?")

#if produto in produtos:
    #produtos.remove(produto)
    #print("Produto removido!")
#else:
    #print("Produto não encontrado!")
    #print(produtos)
    
#======================================================

#produtos = ["Celular","sofá","mesa"]
#quantidae =len(produtos)
#print("Quantidade de produtos:",quantidae)

#==========================================================
#produtos = ["Mouse","Teclado","Monitor"]
#print("Primeiro produto:", produtos[0])

#==========================================================
#produtos = ["Mouse","Teclado","Monitor","Notebook"]
#print("Último produto:",produtos[-1])
#-1 = notebook, -2 = monitor
#==========================================================
#produtos =["Mouse","Teclado","Monitor"]
#produtos[0] = "Mouse Gamer"
#print(produtos)
#==================================================
#numeros = [1,2,3,4,5]
#numeros.clear()
#print(numeros)
#===========================================================
numeros = [100,200,300,400,500,600]
numero = int(input("Digite o número:"))

if numero in numeros:
    posicao = numeros.index(numero)
    print("Posição:",posicao)
else:
    print("número não encontrado!")