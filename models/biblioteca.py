import json
from models.livro import Livro

class Biblioteca:
    def __init__(self):
        self.acervo = []
        self.arquivo = "data/acervo.json"
        self.carregar_dados()

    def carregar_dados(self):
        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)

                self.acervo = []

                for item in dados:
                    livro = Livro(
                        item["titulo"],
                        item["autor"],
                        item["ano"],
                        item["disponivel"]
                    )
                    self.acervo.append(livro)
        except FileNotFoundError:
            self.acervo = []

    def salvar_dados(self):
        dados = []

        for livro in self.acervo:
            dados.append({
                "titulo": livro.titulo,
                "autor": livro.autor,
                "ano": livro.ano,
                "disponivel": livro.disponivel
            })
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def adicionar_livro(self, livro):
        self.acervo.append(livro)
        self.salvar_dados()

    def listar_livros(self):
        if not self.acervo:
            print("Nenhum livro cadastrado.")
            return
        for livro in self.acervo:
            print(livro)
    
    def buscar_por_titulo(self, titulo):
        for livro in self.acervo:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None
    def emprestar_livro(self, titulo):
        livro = self.buscar_por_titulo(titulo)

        if livro:
            if livro.emprestar():
                print("Livro emprestado com sucesso.")
                self.salvar_dados()
            else:
                print("Livro já está emprestado.")
        else:
            print("Livro não encontrado.")
    
    def devolver_livro(self, titulo):
        livro = self.buscar_por_titulo(titulo)

        if livro:
            livro.devolver()
            print("Livro devolvido.")
            self.salvar_dados()
        else:
            print("Livro não encontrado.")
