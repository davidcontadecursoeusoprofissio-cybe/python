senha = "Dev#Python2026"

tem_tamanho = len (senha) >=8

tem_numero = any(char.isdigit() for char in senha)

tem_maiuscula = any(char.isupper() for char in senha)

tem_especial = any(char in"!@#$%^&*" for char in senha)

if not tem_tamanho:
    print("❌ Senha muito curta! Use pelo menos 8 caracteres.")
elif not tem_numero:
    print("⚠Senha fraca!Adicione pelo menos um número.")
elif not tem_maiuscula:
    print("⚠ Senha média! Adicione pelo menos uma letra maiúscula.")
elif not tem_especial:
    print("⚠ Senha quanse boa! Adicionar um carectere especial (!@#$%^&*).")
else:
    print("✔ Senha excelente! Segurança alta")