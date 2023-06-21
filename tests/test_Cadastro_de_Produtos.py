from Cadastro_de_Produto import Cadastro_de_Produto
from Produto import Produto
from Cadastro_de_Preco import Cadastro_de_preco

def test_para_cadastro_de_produtos():
    produto = Produto ("nome", 100, "tipo", "departamento", 50)
    cadastro_produto = Cadastro_de_Produto()
    resposta = cadastro_produto.cadastrar_produto(produto)
    assert "Produto cadastrado com sucesso!" == resposta
    
def test_para_preco_de_produtos():
    produto = Produto ("nome", 25, "tipo", "departamento", 70)
    cadastro_produto = Cadastro_de_Produto()
    resposta = cadastro_produto.cadastrar_produto(produto)
    assert "Preço cadastrado com sucesso!" == resposta