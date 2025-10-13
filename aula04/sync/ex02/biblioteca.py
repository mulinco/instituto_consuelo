from livro import Livro


class Biblioteca:
    def __init__(self, livros):
        self.livros = livros

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def buscar_por_autor(self, autor):
        livros_autor = []
        for livro in self.livros:
            if livro.autor == autor:
                livros_autor.append(livro)
        return livros_autor

    def listar_todos(self):
        for livro in self.livros:
            livro.exibir_infos()

livro = Livro('As Crônicas de Gelo e Fogo', 'George R. R. Martin', '1998', '10' )