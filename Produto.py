class Produto():
    def __init__(self) -> None:
        self.produtos_cadastrados = []
        
    def cadastrar_produto (self, produto):
        self.produtos_cadastrados.append(produto)
        return "Produto cadastrado com sucesso"
        