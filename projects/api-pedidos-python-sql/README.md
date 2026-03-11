# API de Pedidos em Python com SQLite

Projeto didatico de uma API simples para gerenciamento de pedidos, com persistencia em banco SQLite e rotas criadas com Flask.

## Descricao

Este projeto simula um pequeno sistema de pedidos. A aplicacao permite listar pedidos, cadastrar novos registros, buscar um pedido por id e remover itens do banco de dados.

## Tecnologias

- Python
- Flask
- SQLite

## Funcionalidades

- listar pedidos
- adicionar pedido
- remover pedido
- buscar pedido por id

## Estrutura do projeto

```text
api-pedidos-python-sql/
|-- README.md
|-- requirements.txt
|-- data/
|   `-- pedidos.db
`-- src/
    |-- app.py
    `-- database.py
```

## Como rodar

1. Acesse a pasta do projeto:

```bash
cd projects/api-pedidos-python-sql
```

2. Instale as dependencias:

```bash
pip install -r requirements.txt
```

3. Inicie a API:

```bash
python src/app.py
```

A aplicacao ficara disponivel em `http://127.0.0.1:5000`.

## Exemplos de uso

Listar pedidos:

```bash
curl http://127.0.0.1:5000/pedidos
```

Buscar pedido por id:

```bash
curl http://127.0.0.1:5000/pedidos/1
```

Adicionar pedido:

```bash
curl -X POST http://127.0.0.1:5000/pedidos \
  -H "Content-Type: application/json" \
  -d "{\"cliente\":\"Marina\",\"produto\":\"Monitor\",\"quantidade\":1,\"valor\":899.90}"
```

Remover pedido:

```bash
curl -X DELETE http://127.0.0.1:5000/pedidos/2
```

Exemplo de resposta ao listar pedidos:

```json
[
  {
    "cliente": "Ana",
    "id": 1,
    "produto": "Notebook",
    "quantidade": 1,
    "valor": 3500.0
  }
]
```

## Aprendizados

- criacao de rotas REST com Flask
- operacoes basicas com SQLite usando `sqlite3`
- validacao simples de entrada em APIs
- separacao entre camada de rotas e acesso ao banco

[Voltar ao README principal](../../README.md)
