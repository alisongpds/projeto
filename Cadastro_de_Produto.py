class Cadastro_de_Produto:
    def __init__(self):
        self.produtos_cadastrados = []

    def cadastrar_produto(self, Produto):
        self.produtos_cadastrados.append(Produto)

        if len(self.produtos_cadastrados) > 0:
            return "Produto cadastrado com sucesso!"
