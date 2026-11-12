# testar um preço
from validacao import validar_produto

categoria_ids = {1, 2, 3}

dados, erros = validar_produto(
    {
        "preco": 10.0,
        "nome": "Produto Teste",
        "estoque": 5,
        "id_categoria": 1
    },
    categoria_ids
)

assert erros == {}

assert dados == {
    "nome": "Produto Teste",
    "preco": 10.0,
    "estoque": 5,
    "id_categoria": 1
}

# testar com preço negativo
dados, erros = validar_produto(
    {
        "nome": "Produto Teste",
        "preco": "-10.0",
        "estoque": -5,
        "id_categoria": "1"
    },
    categoria_ids
)

assert "preco" in erros
assert "estoque" in erros
assert "id_categoria" not in erros
assert "nome" not in erros
assert dados is None

print("Todos os testes passaram.")