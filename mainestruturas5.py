valor_hora_base = 50.0
trabalhou_no_feriado = True
departamento = "TI"

valor_hora = valor_hora_base * 2.0 if trabalhou_no_feriado else valor_hora_base
if departamento == "TI" or departamento == "Vendas":
    #50.0 x 2.0 = 100.0
    valor_hora *=1.2 # 100.0 x 1.2 = 120.0
    mensagem = "Adicionar de departamento aplicado."
    
elif departamento == "Estágio":
    # 100.0
    valor_hora *= 0.8 # 100.0 x 0.8 =80.0 Reduz 20%
    
    mensagem = "Valor ajustado para bolsa estágio."
    
else:
    
    mensagem = "Pagamento de hora padrão."
    
print(f"{mensagem} Valor final da hora:R${valor_hora:2f}")
    
