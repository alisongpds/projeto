class Produto:
    def __init__(self, nome, tipo, preco):
        self.nome = nome
        self.tipo = tipo
        self.preco = preco

class CadastroProdutos:
    def __init__(self):
        self.produtos = []

    def cadastrar_produto(self, nome, tipo, preco):
        produto = Produto(nome, tipo, preco)
        self.produtos.append(produto)

    def listar_produtos(self):
        if len(self.produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            print("Lista de produtos:")
            for produto in self.produtos:
                print(f"Nome: {produto.nome}\nTipo: {produto.tipo}\nPreço: R${produto.preco}\n")
