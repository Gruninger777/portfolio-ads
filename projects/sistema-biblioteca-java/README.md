# Sistema de Biblioteca em Java

## Descrição

Aplicação de console para cadastro, listagem e remoção de livros utilizando `ArrayList` como estrutura de armazenamento em memória.

## Objetivo do projeto

Praticar fundamentos de Java com classes simples, organização em camadas básicas e criação de menus de interação no terminal.

## Tecnologias utilizadas

- Java

## Estrutura de arquivos

```text
sistema-biblioteca-java/
├── README.md
└── src/
    └── biblioteca/
        ├── Livro.java
        ├── BibliotecaService.java
        └── Main.java
```

## Como executar

1. Acesse a pasta do projeto.
2. Compile os arquivos Java:

```bash
javac -d out src/biblioteca/*.java
```

3. Execute a aplicação:

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

## Aprendizados desenvolvidos

- Uso de `ArrayList` em aplicações simples
- Criação de classes de modelo e serviço
- Leitura de dados pelo console
- Organização inicial de um projeto Java

## Melhorias futuras

- Adicionar autor e ano de publicação
- Implementar busca por título
- Persistir os dados em arquivo
- Incluir testes unitários
