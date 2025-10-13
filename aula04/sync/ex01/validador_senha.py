senha = 'SenhaForte123@'

def validador(senha):
    if len(senha) < 8:
        return False

    tem_maiuscula = False 
    tem_minuscula = False
    tem_numero = False
    tem_especial = False
    caracteres_especiais = "@#$%&*?!"

    for i in senha:
        if i.isupper():
            tem_maiuscula = True
        elif i.islower():
             tem_minuscula = True
        elif i.isdigit():
             tem_numero = True
        elif i in caracteres_especiais:
             tem_especial = True


    if tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
         return True 
    else: 
         return False
        
resultado_validador = validador(senha)
if resultado_validador == True:
    print("a senha é válida")
else:
    print("a senha é inválida")
    