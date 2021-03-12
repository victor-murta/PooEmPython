#composição: relação mais forte entre classes. Uma classe vai ser dona dos objetos da outra classe

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
    
    # o Endereço(classe) pertence a classe Cliente, quando a Cliente é removido , a classe Endereço também é
    def inserirEndereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))
    
    def listaEnderecos(self):
        for e in self.enderecos:
            print(f' - {e.cidade} {e.estado}')
    
    def __del__(self):
        print(f' ---- {self.nome} FOI APAGADO ----')


#Um cliente pode ter vários endereços, então terá uma classe só para endereços  

class Endereco:
    def __init__(self, cidade , estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f' ---- {self.cidade}/{self.estado} FORAM APAGADOS ----')





if __name__ == '__main__':
    cliente1 = Cliente('Victor Murta garcia', 19)
    cliente1.inserirEndereco('Bsb', 'DF')
    cliente1.listaEnderecos()
    del cliente1
    print()


    cliente2 = Cliente('Lucas', 19)
    cliente2.inserirEndereco('DownTown', 'Whashington')
    cliente2.listaEnderecos()





