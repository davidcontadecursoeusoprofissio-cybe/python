#uso_cpu = 92 

#uso_memoria = 85

#if uso_cpu > 90 and uso_memoria > 90:
    #nivel="🔴CRÍTICO"
    #acao ="Reiniciar serviços imediatamente e alertar a equipe de DevOps!"
    
#elif uso_cpu > 80 or uso_memoria > 80:
   #nivel="🟠ALERTA"
   # acao="Redirecionar tráfego para servidores secundários."
#elif uso_cpu>50 or uso_memoria > 50:
    #nivel="🟡ATENÇÂO"
   # acao="Registrar pico de uso nos logs de monitoramento."
#else:
    #nivel="🟢NORMAL"
    #acao = "Sistema operando dentro dos parâmetros ideais."
    
#print(f"Status: {nivel}\nAção recomendada:{acao}")




nome_letras = 17
letra_mauiscura = 1
#0 da else 1 elif
if nome_letras <= 5 and letra_mauiscura >= 1:
    nome= "David"
    quantasletras= "Nome pequeno"
    
    
elif nome_letras <= 11 and letra_mauiscura >= 1:
    nome= "HiagoAlarcon"
    quantasletras= "Nome médio"
    
    
elif nome_letras > 11 and letra_mauiscura >= 1:
    nome= "HiagoAlarconCamisão"
    quantasletras= "Nome grande"
    
    
else:
    nome = "Desconhecido"
    quantasletras= "N/A"
    print("Não há esse numero de letras")
    
    
print(f"Seu nome é considerado: {quantasletras}, Nome: {nome}")
