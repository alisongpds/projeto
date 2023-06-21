from Cadastro_de_Produto import Cadastro_de_Produto
from Produto import Produto

def test_para_cadastro_de_produtos():
    produto = Produto ("nome", 100, "tipo", "departamento", 50)
    cadastro_produto = Cadastro_de_Produto()
    resposta = cadastro_produto.cadastrar_produto(produto)
    assert "Produto cadastrado com sucesso!" == resposta