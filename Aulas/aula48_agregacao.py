class Carrinho:
    def __init__(self) -> None:
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])

    def insert_produtos(self, *produtos):
        # for produto in produtos:
        #     self._produtos.append(produto)
        # self._produtos.extend(produtos)
        self._produtos += produtos

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()



class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1, p2 = Produto('Arroz', 2.75), Produto('Frango', 16.00)
carrinho.insert_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())