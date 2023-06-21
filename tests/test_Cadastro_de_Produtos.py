from Produto import Produto
from Cadastro_de_Produto import Cadastro_de_Produto

def test_para_cadastro_de_produtos():
    produto = Produto()
    cadastro_produto = cadastroProduto()
    resposta = cadastro_produto.cadastrar_produto(produto)
    assert "Produto cadastrado com sucesso!" == resposta