#dano_base = 50
#elemento_ataque = "fogo"
#elemento_defensor = "gelo"
#eh_critico = True

#dano = dano_base*2 if eh_critico else dano_base

#if elemento_ataque == elemento_defensor:
    #dano*=0.5
    #mensagem="O ataque não foi muito eficaz..."
#elif(elemento_ataque == "fogo" and elemento_defensor =="gelo") or \
        #(elemento_ataque == "agua" and elemento_defensor == "fogo") or\
        #(elemento_ataque == "planta" and elemento_defensor == "agua"):
            #dano *=1.5
            #mensagem = "Super eficaz! Dano bônus aplicado."
#else:
   # mensagem = "Dano normal aplicado."
    
#print(f"{mensagem} Dano final decretado: {dano} HP.")

#=================================================