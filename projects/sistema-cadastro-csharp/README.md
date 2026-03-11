# Sistema de Cadastro em C#

Aplicação de console para cadastro, listagem e remoção de usuários, com armazenamento em memória.

## Objetivo

Praticar estruturação de uma aplicação de console em C#, uso de listas, menu interativo e separação básica de responsabilidades.

## Tecnologias

- C#
- .NET

## Funcionalidades

- cadastrar usuários
- listar usuários cadastrados
- remover usuários
- interagir por menu no terminal

## Estrutura do projeto

```text
sistema-cadastro-csharp/
├── README.md
├── sistema-cadastro-csharp.csproj
└── src/
    ├── Program.cs
    ├── User.cs
    └── UserService.cs
```

## Como executar

```bash
dotnet run
```

## Exemplo de uso

```text
1 - Adicionar usuário
2 - Listar usuários
3 - Remover usuário
0 - Sair
Escolha uma opção: 1
Digite o nome do usuário: Ana
Usuário adicionado com sucesso.
```

## O que este projeto demonstra

- uso de `List<T>` para dados em memória
- fluxo de aplicações de console
- separação simples entre modelo, serviço e execução
- tratamento básico de entrada do usuário

## Próximos passos

- adicionar persistência em arquivo ou banco de dados
- incluir busca por nome
- validar duplicidade de usuários
- criar testes automatizados

[Voltar ao README principal](../../README.md)
