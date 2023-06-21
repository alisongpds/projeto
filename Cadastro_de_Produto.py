class Cadastro_de_Produto():
    def __init__(self):
        self.produtos_cadastrados = []
        
    def cadastrar_produto (self, Produto):
        self.produtos_cadastrados.append(Produto)
        return "Produto cadastrado com sucesso!"