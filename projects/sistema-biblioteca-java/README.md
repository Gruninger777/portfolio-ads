# Sistema de Biblioteca em Java

Aplicação de console para cadastro, listagem e remoção de livros, utilizando armazenamento em memória.

## Objetivo

Praticar fundamentos de Java com classes simples, organização básica do projeto e criação de menus de interação no terminal.

## Tecnologias

- Java

## Funcionalidades

- cadastrar livros
- listar livros cadastrados
- remover livros
- interagir por menu no terminal

## Estrutura do projeto

```text
sistema-biblioteca-java/
├── README.md
├── out/
└── src/
    └── biblioteca/
        ├── Livro.java
        ├── BibliotecaService.java
        └── Main.java
```

## Como executar

Compile os arquivos Java:

```bash
javac -d out src/biblioteca/*.java
```

Execute a aplicação:

```bash
java -cp out biblioteca.Main
```

## Exemplo de uso

```text
1 - Cadastrar livro
2 - Listar livros
3 - Remover livro
0 - Sair
Escolha uma opção: 1
Digite o título do livro: Clean Code
Livro cadastrado com sucesso.
```

## O que este projeto demonstra

- uso de `ArrayList` em uma aplicação simples
- separação entre classes de modelo e serviço
- leitura de dados pelo console
- estrutura inicial de um projeto Java

## Próximos passos

- adicionar autor e ano de publicação
- implementar busca por título
- persistir dados em arquivo
- incluir testes unitários

[Voltar ao README principal](../../README.md)
