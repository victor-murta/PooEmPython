'''
dentro da associação =>
    agregação: uma classe usa a outra e dependem entre si
    compisição: uma classe usa outra a e dependem entre si
'''

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
    
    def inserirProduto(self, produto):
        self.produtos.append(produto)
    
    def listaProdutos(self):
        for p in self.produtos:
            print(f' - {p.nome} , {p.valor}')
        
    def somaTotal(self):
        total = 0
        for prod in self.produtos:
            total += prod.valor
            
        print()
        return f'Total: {total}'

class Produtos:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


if __name__ == '__main__':
    carrinho = CarrinhoDeCompras()
    
    p1 = Produtos('Notebook', 4000)
    p2 = Produtos('Teclado', 200)
    p3 = Produtos('Mouse', 150)

    #p1 é um objeto
    carrinho.inserirProduto(p1)
    carrinho.inserirProduto(p2)
    carrinho.inserirProduto(p3)

    carrinho.listaProdutos()
    print(carrinho.somaTotal())

