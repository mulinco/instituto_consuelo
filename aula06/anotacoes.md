## Automatiza que cresce

- Testes unitários  
- Doc Tecnica
- Versionamento com Git/Github
- Implementação de teste unitários em APIrest

## Por que testar?
#### Custo de um código não testado resulta em retrabalho, falhas ou atrasos no desenvolvimento.  
### Com testes:  
- Bugs detectados  
- Confiança para refatorar    
- Documentação viva do código    
- Menos estresse, mais qualidade

## Pirâmides de Testes  
  #### Estrutura de testes eficiente  
  ### Regra de Ouro  
  - 70% unitários (muitos, rápidos)  
  - 20% integração (alguns, médios)   
  - 10% E2E (Testes End-To-End)

## Configurando o Ambiente
#### Setup do Pytest
`pip install pytest pytest-cov`  
`pip install flask`  (ou fastapi)  

## Primeiro Teste  
#### Teste simples - listagem vazia  
### Anatomia do Teste:  
- Nome descritivo: `test_listar_usuarios_vazio`  
- Docstring explicativa  
- Arrange: (fixture já prepara)  
- Act: `client.get('/usuarios')`  
- Assert: Verificações com `assert`  

 #### Teste de erro - validação  
 > Importante: Testar cenários de erro é tão importante quanto testar sucessos!

## Padrão AAA  
### Benefícios do padrão AAA (arrange, act, assert):  
- Estrutura clara;
- Fácil manutenção;
- Testes mais legíveis.

## Executando Testes  
### No VSCode:  
- Use a extensão Python Test Explorer;
- Veja testes visualmente;
- Execute com um clique.

  ## Boas práticas de testes
  #### Como escrever bons testes

  ### FAÇA:
  - Nomes descritivos;
  - Testes independentes;
  - Use fixtures  para reutilização;
  - Um teste = uma funcionalidade.
 
  ## NÃO FAÇA:
  - Ignorar cenários de erro;
  - Lógica complexa nos testes;
  - Testar implementação interna;
  - Testes que dependem de ordem.  
  
