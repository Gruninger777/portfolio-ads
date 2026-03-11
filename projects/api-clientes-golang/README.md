# API de Clientes em Go

## Descrição

API REST simples para cadastro e listagem de clientes, com dados mantidos em memória e comunicação em JSON.

## Objetivo do projeto

Praticar fundamentos de backend com Go, criação de rotas HTTP, serialização de JSON e organização inicial de uma API.

## Tecnologias utilizadas

- Go
- net/http
- encoding/json

## Estrutura de arquivos

```text
api-clientes-golang/
├── README.md
├── go.mod
└── src/
    └── main.go
```

## Como executar

1. Acesse a pasta do projeto.
2. Execute a aplicação:

```bash
go run src/main.go
```

3. A API ficará disponível em:

```text
http://localhost:8080
```

## Exemplo de uso

Listar clientes:

```bash
curl http://localhost:8080/clientes
```

Adicionar cliente:

```bash
curl -X POST http://localhost:8080/clientes ^
  -H "Content-Type: application/json" ^
  -d "{\"nome\":\"Maria\",\"email\":\"maria@email.com\"}"
```

## Aprendizados desenvolvidos

- Criação de rotas com `net/http`
- Leitura e escrita de JSON
- Estruturação básica de API REST
- Armazenamento temporário em memória

## Melhorias futuras

- Adicionar busca por ID
- Implementar atualização e remoção
- Validar formato de e-mail
- Separar rotas e serviços em arquivos diferentes
