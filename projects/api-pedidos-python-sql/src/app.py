from flask import Flask, jsonify, request

from database import add_order, delete_order, get_order_by_id, initialize_database, list_orders


app = Flask(__name__)


# Garante que a tabela exista e que o banco tenha dados iniciais para demonstracao.
initialize_database()


@app.get("/pedidos")
def listar_pedidos():
    """Lista todos os pedidos cadastrados no banco."""
    pedidos = list_orders()
    return jsonify(pedidos), 200


@app.get("/pedidos/<int:pedido_id>")
def buscar_pedido(pedido_id):
    """Busca um pedido especifico pelo id informado na rota."""
    pedido = get_order_by_id(pedido_id)

    if pedido is None:
        return jsonify({"erro": "Pedido nao encontrado."}), 404

    return jsonify(pedido), 200


@app.post("/pedidos")
def adicionar_pedido():
    """
    Recebe um JSON simples, valida os campos esperados e salva o pedido.
    Esse fluxo foi mantido propositalmente didatico para facilitar estudo.
    """
    data = request.get_json(silent=True) or {}

    campos_obrigatorios = ["cliente", "produto", "quantidade", "valor"]
    campos_ausentes = [campo for campo in campos_obrigatorios if campo not in data]

    if campos_ausentes:
        return jsonify(
            {"erro": f"Campos obrigatorios ausentes: {', '.join(campos_ausentes)}"}
        ), 400

    try:
        quantidade = int(data["quantidade"])
        valor = float(data["valor"])
    except (TypeError, ValueError):
        return jsonify({"erro": "Quantidade deve ser inteira e valor deve ser numerico."}), 400

    if quantidade <= 0 or valor <= 0:
        return jsonify({"erro": "Quantidade e valor devem ser maiores que zero."}), 400

    novo_pedido = add_order(
        cliente=data["cliente"],
        produto=data["produto"],
        quantidade=quantidade,
        valor=valor,
    )

    return jsonify(novo_pedido), 201


@app.delete("/pedidos/<int:pedido_id>")
def remover_pedido(pedido_id):
    """Remove um pedido pelo id e informa se a operacao foi concluida."""
    deleted = delete_order(pedido_id)

    if not deleted:
        return jsonify({"erro": "Pedido nao encontrado."}), 404

    return jsonify({"mensagem": "Pedido removido com sucesso."}), 200


if __name__ == "__main__":
    app.run(debug=True)
