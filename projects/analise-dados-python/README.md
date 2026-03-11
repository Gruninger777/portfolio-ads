# Análise de Dados em Python

## Descrição

Projeto introdutório de análise de dados com leitura de CSV, agrupamento de informações e cálculo de estatísticas simples utilizando `pandas`.

## Objetivo do projeto

Praticar manipulação de dados tabulares, leitura de arquivos, agrupamento por categorias e interpretação inicial de métricas.

## Tecnologias utilizadas

- Python
- pandas

## Estrutura de arquivos

```text
analise-dados-python/
├── README.md
├── data/
│   └── vendas.csv
└── src/
    └── main.py
```

## Como executar

1. Acesse a pasta do projeto.
2. Instale a dependência:

```bash
pip install pandas
```

3. Execute o script principal:

```bash
python src/main.py
```

## Exemplo de uso

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

## Aprendizados desenvolvidos

- Leitura de arquivos CSV com `pandas`
- Cálculo de média e contagem
- Agrupamento de dados por categoria
- Organização de um pequeno projeto analítico

## Melhorias futuras

- Criar gráficos com `matplotlib` ou `seaborn`
- Adicionar filtros por período
- Exportar relatórios
- Incluir novos datasets para comparação
