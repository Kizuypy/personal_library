# 📚 Biblioteca Pessoal

> Sistema de gerenciamento de acervo pessoal desenvolvido em Python com foco em **Programação Orientada a Objetos**.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/POO-Orientado%20a%20Objetos-4B8BBE?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-Persistência%20de%20Dados-000000?style=for-the-badge&logo=json&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-2C3E50?style=for-the-badge)

---

## 📋 Sobre o Projeto

O **Biblioteca Pessoal** é um sistema de terminal para gerenciar seu acervo de livros. Com ele, você pode cadastrar livros, controlar empréstimos e devoluções, e buscar títulos — tudo salvo automaticamente em um arquivo JSON.

Este projeto foi desenvolvido como parte do meu aprendizado em **POO com Python**, aplicando conceitos como classes, métodos, encapsulamento, persistência de dados e modularização com packages.

---

## ✨ Funcionalidades

- 📖 **Adicionar livros** ao acervo com título, autor e ano
- 📋 **Listar todos os livros** com status de disponibilidade
- 🔍 **Buscar livro** por título
- 🤝 **Emprestar livro** — muda status para "Emprestado"
- ↩️ **Devolver livro** — muda status para "Disponível"
- 💾 **Persistência automática** em JSON — os dados são mantidos entre execuções

---

## 🧱 Conceitos de POO Aplicados

| Conceito | Onde foi usado |
|---|---|
| `class` | `Livro` e `Biblioteca` |
| `__init__` | Inicialização dos atributos |
| `__str__` | Representação legível do objeto |
| Métodos de instância | `emprestar()`, `devolver()`, `adicionar_livro()` etc. |
| Encapsulamento | Cada classe gerencia seu próprio estado |
| Separação de responsabilidades | Cada arquivo tem uma única responsabilidade |

---

## 📁 Estrutura do Projeto

```
biblioteca_pessoal/
│
├── main.py                 # Menu e execução principal
│
├── models/
│   ├── __init__.py         # Torna a pasta um package Python
│   ├── livro.py            # Classe Livro
│   └── biblioteca.py       # Classe Biblioteca
│
└── data/
    └── acervo.json         # Dados persistidos automaticamente
```

---

## 🚀 Como Usar

### Pré-requisitos

- Python 3.10 ou superior instalado

### Instalação

```bash
# Clone o repositório
git clone https://github.com/Kizuypy/personal_library.git

# Entre na pasta do projeto
cd biblioteca-pessoal

# Execute o programa
python main.py
```

### Uso

Ao executar, você verá o menu interativo:

```
=== Biblioteca Pessoal ===
1. Adicionar livro
2. Listar todos os livros
3. Emprestar livro
4. Devolver livro
5. Buscar livro
0. Sair

Escolha: 
```

---

## 💡 Exemplo de Uso

```
Escolha: 1
Título: Clean Code
Autor: Robert C. Martin
Ano: 2008
Livro adicionado!

Escolha: 2
Clean Code - Robert C. Martin (2008) [Disponível]

Escolha: 3
Título do livro: Clean Code
Livro emprestado com sucesso.

Escolha: 2
Clean Code - Robert C. Martin (2008) [Emprestado]
```

---

## 🗺️ Próximos Passos (Roadmap)

- [ ] Adicionar data de empréstimo com `datetime`
- [ ] Listar apenas livros disponíveis ou emprestados
- [ ] Adicionar nome do responsável pelo empréstimo
- [ ] Interface gráfica com Tkinter ou PySide6

---

## 👨‍💻 Autor

Feito com 💙 por **Vinicius Henrique**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vinicius-henrique-dev/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Kizuypy)