uso_cpu = 92 

uso_memoria = 85

if uso_cpu > 90 and uso_memoria > 90:
    nivel="🔴CRÍTICO"
    acao ="Reiniciar serviços imediatamente e alertar a equipe de DevOps!"
    
elif uso_cpu > 80 or uso_memoria > 80:
    nivel="🟠ALERTA"
    acao="Redirecionar tráfego para servidores secundários."
elif uso_cpu>50 or uso_memoria > 50:
    nivel="🟡ATENÇÂO"
    acao="Registrar pico de uso nos logs de monitoramento."
else:
    nivel="🟢NORMAL"
    acao = "Sistema operando dentro dos parâmetros ideais."
    
print(f"Status: {nivel}\nAção recomendada:{acao}")
