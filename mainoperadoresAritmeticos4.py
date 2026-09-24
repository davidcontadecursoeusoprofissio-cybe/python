idade = 22
tem_convite= False
e_vip = True

pode_entrar=(idade >= 18)and(tem_convite or e_vip)
print(f"Pode entrar na festa?{pode_entrar}")