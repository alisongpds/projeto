import pytest

def test_cadastrar_produto():
    cadastro = CadastroProdutos()
    cadastro.cadastrar_produto("Processador", "Hardware", 999.99)

    assert len(cadastro.produtos) == 1
    assert cadastro.produtos[0].nome == "Processador"
    assert cadastro.produtos[0].tipo == "Hardware"
    assert cadastro.produtos[0].preco == 999.99

def test_listar_produtos(capsys):
    cadastro = CadastroProdutos()
    cadastro.cadastrar_produto("Processador", "Hardware", 999.99)
    cadastro.cadastrar_produto("Windows 10", "Software", 199.99)

    cadastro.listar_produtos()
    captured = capsys.readouterr()

    expected_output = "Lista de produtos:\nNome: Processador\nTipo: Hardware\nPreço: R$999.99\n\n" \
                      "Nome: Windows 10\nTipo: Software\nPreço: R$199.99\n\n"
    assert captured.out == expected_output

def test_listar_produtos_sem_cadastro(capsys):
    cadastro = CadastroProdutos()

    cadastro.listar_produtos()
    captured = capsys.readouterr()

    assert captured.out == "Nenhum produto cadastrado.\n"
