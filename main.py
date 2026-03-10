from models.livro import Livro
from models.biblioteca import Biblioteca


biblioteca = Biblioteca()


def menu():
    while True:
        print("\n=== Biblioteca Pessoal===")
        print("1. Adicionar livro")
        print("2. Listar todos os livros")
        print("3. Emprestar livro")
        print("4. Devolver livro")
        print("5. Buscar livro")
        print("0. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano: "))

            livro = Livro(titulo, autor, ano)
            biblioteca.adicionar_livro(livro)

            print("Livro adicionado!")

        elif opcao == "2":
            biblioteca.listar_livros()

        elif opcao == "3":
            titulo = input("Título do livro: ")
            biblioteca.emprestar_livro(titulo)

        elif opcao == "4":
            titulo = input("Título do livro: ")
            biblioteca.devolver_livro(titulo)

        elif opcao == "5":
            titulo = input("Título do livro: ")
            livro = biblioteca.buscar_por_titulo(titulo)

            if livro:
                print(livro)

            else:
                print("Nenhum livro encontrado.")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()