# API de Clientes em Go

API REST simples para cadastro e listagem de clientes, com armazenamento em memória e comunicação em JSON.

## Objetivo

Praticar fundamentos de backend com Go, criação de rotas HTTP, manipulação de requisições e respostas JSON e estrutura inicial de uma API.

## Tecnologias

- Go
- `net/http`
- `encoding/json`

## Funcionalidades

- listar clientes
- cadastrar novos clientes
- responder dados em formato JSON
- manter dados temporariamente em memória

## Estrutura do projeto

```text
api-clientes-golang/
├── README.md
├── go.mod
└── src/
    └── main.go
```

## Como executar

```bash
go run src/main.go
```

API disponível em `http://localhost:8080`.

## Exemplo de uso

Listar clientes:

```bash
curl http://localhost:8080/clientes
```

Cadastrar cliente:

```bash
curl -X POST http://localhost:8080/clientes ^
  -H "Content-Type: application/json" ^
  -d "{\"nome\":\"Maria\",\"email\":\"maria@email.com\"}"
```

## O que este projeto demonstra

- construção de rotas com `net/http`
- serialização e leitura de JSON
- organização básica de uma API REST
- desenvolvimento backend sem frameworks

## Próximos passos

- adicionar busca por ID
- implementar atualização e remoção
- validar melhor os dados de entrada
- separar responsabilidades em mais arquivos

[Voltar ao README principal](../../README.md)
