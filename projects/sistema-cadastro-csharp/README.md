# Sistema de Cadastro em C#

## Descrição

Aplicação de console para gerenciar usuários com operações de cadastro, listagem e remoção, utilizando armazenamento em memória.

## Objetivo do projeto

Praticar estruturação de uma aplicação de console em C#, uso de listas, organização de menu interativo e separação simples de responsabilidades.

## Tecnologias utilizadas

- C#
- .NET

## Estrutura de arquivos

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

1. Acesse a pasta do projeto.
2. Execute com o SDK do .NET instalado:

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

## Aprendizados desenvolvidos

- Uso de `List<T>` para armazenar dados em memória
- Construção de menus em aplicações de console
- Separação básica entre modelo, serviço e fluxo principal
- Validação simples de entrada do usuário

## Melhorias futuras

- Adicionar persistência em arquivo ou banco de dados
- Incluir busca por nome
- Validar duplicidade de usuários
- Criar testes automatizados
