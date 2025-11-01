## Design Tokens  
- são as variáveis que armazenam e gerenciam todos os valores visuais e de design (como cores, tipografia e espaçamento) de um produto digital, garantindo consistência em todas as plataformas.  

- Um **exemplo** seria definir `cor-do-botão-principal` com o valor hexadecimal `#00C2FF`. Se o valor da cor precisar ser atualizado (por exemplo, para #009CCE por motivos de acessibilidade), apenas o token cor-do-botão-principal precisa ser modificado, e todos os botões que o utilizam serão atualizados automaticamente.

### Espaço de respiro
- Espaço de respiro em design é o espaço vazio intencional ao redor ou entre os elementos visuais (como textos e imagens) que melhora a organização, a clareza, a legibilidade e o equilíbrio de um layout, proporcionando conforto visual ao usuário. Ele é essencial para destacar elementos importantes e evitar a sobrecarga visual, funcionando como pausas em uma apresentação.
- Em CSS, usualmente é feito esse espaço do lado esquerdo e do lado direito a fim de centralizar o conteúdo.

#### Exemplo
`style.css`  
```
main {
background: pink
}
```

```
.card {
}
```

```
#unico {
}
```
---  

### Aninhamento  
`hmtl`  
```
<main>
    <div class="card"></div>  
</main>  
```
`css`  

```
main {  
    .card {  
    }  
}
```
---

#### O que é uma classe em HTML?  
- é um atributo usado para especificar um ou mais elementos que compartilham estilos ou comportamentos comuns, permitindo que o CSS e o JavaScript os selecionem e manipulem coletivamente.
---

#### Box Model  
(escrever sobre depois)  
---

#### Container Flex  
- display-flex 🎉
---

#### Media Queries
```
@media(max-width:768px) {
  .container {
  display: flex
  flex-direction: column
  }
}
```
#### O que eu fiz duante a aula e posso aprimorar:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css"
</head>
<body>
    <h1>olar</h1>
    <section class="container">
    <div class="card">
        <p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tincidunt eu quam vitae sodales. Morbi orci libero, porttitor quis blandit eu, laoreet a sapien. Integer eu facilisis risus, non faucibus nulla. Etiam sed augue lectus. Sed sollicitudin est mauris, sed luctus libero cursus et. Fusce ut diam vitae urna ultrices eleifend ac ac leo. Cras lectus lectus, ultrices porta mi sed, tempor placerat turpis. Morbi porttitor elementum eros, eget feugiat nisl dignissim vestibulum. Proin nec sagittis sem. Aliquam ac commodo tortor. Suspendisse dictum lobortis diam, sed efficitur enim volutpat at. Curabitur porttitor urna id augue ultricies, ut pretium risus congue.
    </p>
    </div>
    <div class="card">
        <p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tincidunt eu quam vitae sodales. Morbi orci libero, porttitor quis blandit eu, laoreet a sapien. Integer eu facilisis risus, non faucibus nulla. Etiam sed augue lectus. Sed sollicitudin est mauris, sed luctus libero cursus et. Fusce ut diam vitae urna ultrices eleifend ac ac leo. Cras lectus lectus, ultrices porta mi sed, tempor placerat turpis. Morbi porttitor elementum eros, eget feugiat nisl dignissim vestibulum. Proin nec sagittis sem. Aliquam ac commodo tortor. Suspendisse dictum lobortis diam, sed efficitur enim volutpat at. Curabitur porttitor urna id augue ultricies, ut pretium risus congue.
    </p>
    </div>
    <div class="card">
        <p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tincidunt eu quam vitae sodales. Morbi orci libero, porttitor quis blandit eu, laoreet a sapien. Integer eu facilisis risus, non faucibus nulla. Etiam sed augue lectus. Sed sollicitudin est mauris, sed luctus libero cursus et. Fusce ut diam vitae urna ultrices eleifend ac ac leo. Cras lectus lectus, ultrices porta mi sed, tempor placerat turpis. Morbi porttitor elementum eros, eget feugiat nisl dignissim vestibulum. Proin nec sagittis sem. Aliquam ac commodo tortor. Suspendisse dictum lobortis diam, sed efficitur enim volutpat at. Curabitur porttitor urna id augue ultricies, ut pretium risus congue.
    </p>
    </div>
    </section>


</body>
</html>
```

```
:root {
    --cor-primaria: antiquewhite;

}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

h1 {
    font-size: 2rem;
}


.container {
    display: flex;
    gap: 8px;
    justify-content: center;
    align-items: center;
    flex-direction: row-reverse;
.card {
    width: 400px;
    height: auto;
    background-color: var(--cor-primaria);
    border: 1px solid #ccc;
    border-radius: 4px;

    p{
    padding: 0.5rem;
    font-size: 1.5rem;
    color: rgb(66, 5, 5)
    
}
}
}

```
