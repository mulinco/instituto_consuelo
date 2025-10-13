class Livro:
    def __init__(self, titulo, autor, ano, isbn):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = isbn

    def exibir_infos(self):
        return f"Título: {self.titulo}\n Autor: {self.autor}\n Ano: {self.ano}\n IBSN: {self.isbn}\n"
    

livro = Livro('As Crônicas de Gelo e Fogo', 'George R. R. Martin', '1998', '10' )
print(livro.exibir_infos())