# Análise de Dados em Python

Projeto introdutório de análise de dados com leitura de CSV, estatísticas simples e agrupamentos utilizando `pandas`.

## Objetivo

Praticar manipulação de dados tabulares, leitura de arquivos, agrupamento por categorias e interpretação inicial de métricas.

## Tecnologias

- Python
- pandas

## Funcionalidades

- leitura de arquivo CSV
- cálculo de estatísticas básicas
- agrupamento de informações por categoria
- exibição de resultados no terminal

## Estrutura do projeto

```text
analise-dados-python/
├── README.md
├── data/
│   └── vendas.csv
└── src/
    └── main.py
```

## Como executar

1. Instale a dependência:

```bash
pip install pandas
```

2. Execute o script:

```bash
python src/main.py
```

## Exemplo de saída

```text
=== Visão geral dos dados ===
Total de registros: 8
Média de valor por venda: R$ 643.75

=== Quantidade de vendas por categoria ===
categoria
Backend    3
Dados      3
Frontend   2
```

## O que este projeto demonstra

- leitura e tratamento inicial de dados com `pandas`
- cálculo de média e contagem
- agrupamento por categoria
- organização de um projeto analítico simples

## Próximos passos

- criar gráficos com bibliotecas de visualização
- adicionar filtros por período
- exportar relatórios
- incluir novos datasets para comparação

[Voltar ao README principal](../../README.md)
