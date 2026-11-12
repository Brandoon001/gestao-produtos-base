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