### Objetivos da aula

> Modularizar código profissionalmente  
> Dados com segurança  
>  Boas práticas em Python  
>  Criar testes unitários   

### Por que modularizar??

#### Problema
- Código difícil de manter   
- Duplicação constante   
- Testes impossíveis   
- Bugs recorrentes   

#### Solução
- Colaboração Eficiente   
- Código reutilizável  
- Manutenção fácil  
- Testes isolados

**Design System, bootstrap
 ### Refatoração == Normalização

"""Enunciado: Crie um arquivo validador_senha.py com uma função que valida senhas seguindo estas regras:

Mínimo de 8 caracteres
Pelo menos uma letra maiúscula
Pelo menos uma letra minúscula
Pelo menos um número
Pelo menos um caractere especial (@, #, $, %, etc.)"""

# Testes devem verificar:
# 1. Senha válida
# 2. Senha muito curta
# 3. Sem maiúsculas
# 4. Sem números
# 5. Sem caracteres especiais



def validador(senha):
    if len(senha) >= 8:
        print('Tamanho válido')
    else:
        print('Tamanho inválido')

    if isupper(senha):
        print('Contém letra maiúscula')
    else: 
        print('Não contém letra maiúscula')

    if senha.islower():
        print('Contém letra minúscula')
    else:
        print('Não contém letra minúscula')


tamanho_valido = validador()
print(tamanho_valido)

### PEP 8 - Regras de ouro


