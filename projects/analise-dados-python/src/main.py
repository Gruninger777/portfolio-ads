from pathlib import Path

import pandas as pd


def carregar_dados(caminho_arquivo: Path) -> pd.DataFrame:
    """Carrega o arquivo CSV de exemplo para análise."""
    return pd.read_csv(caminho_arquivo)


def exibir_estatisticas(dados: pd.DataFrame) -> None:
    total_registros = len(dados)
    media_valor = dados["valor"].mean()
    # O agrupamento ajuda a comparar rapidamente os resultados entre áreas diferentes.
    quantidade_por_categoria = dados.groupby("categoria")["id"].count()
    media_por_categoria = dados.groupby("categoria")["valor"].mean()

    print("=== Visão geral dos dados ===")
    print(f"Total de registros: {total_registros}")
    print(f"Média de valor por venda: R$ {media_valor:.2f}")
    print()
    print("=== Quantidade de vendas por categoria ===")
    print(quantidade_por_categoria)
    print()
    print("=== Média de valor por categoria ===")
    print(media_por_categoria.round(2))


def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent
    caminho_csv = base_dir / "data" / "vendas.csv"
    dados = carregar_dados(caminho_csv)
    exibir_estatisticas(dados)


if __name__ == "__main__":
    main()
