def validador(senha):
    if len(senha) >= 8:
        print('Tamanho válido')
    else:
        print('Tamanho inválido')


tamanho_valido = validador()
print(tamanho_valido)