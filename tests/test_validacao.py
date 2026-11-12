# testar preço valido

def campos_validos():
    campos = {
        "nome": "Mouse sem fio",
        "preco": "49,90",
        "estoque": "23",
        "id_categoria": "2"
    }

    campos.update(alteracoes)
    return campos

@pytest.mark.parametrize("campo", "valor",
  [
    ("preco", "-50,00")
    ("preco", "-0,00")
    ("preco", "abc")
  ],
)

