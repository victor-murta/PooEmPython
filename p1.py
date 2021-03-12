#import datetime

'''class Conta:
    def __init__(self, numero, nome_cliente, saldo , limite):
        self.numero = numero
        self.nome_cliente = nome_cliente
        self.saldo = saldo
        self.limite = limite
    
    def getNumero(self):
        print(f'Número: {self.numero}')

    def getNome_Cliente(self):
        print(f'Nome: {self.nome_cliente}')
    
    def depositar(self,valor):
        self.saldo += valor
        print('Depositado com sucesso ')
        return self.saldo

    def setNumero(self,setNumero):
        self.numero = setNumero
        return f'Número alterado para {setNumero}'

    def setNome_cliente(self, novoNome):
        self.nome_cliente = novoNome
        return 'Nome alterado para ', novoNome

    def __str__(self):
        return f''      --Dados conta {self.nome_cliente}--

        Número: {self.numero}
        Nome do cliente: {self.nome_cliente}
        Saldo: {self.saldo}
        Limite: {self.limite}
        ''
    def Saque(self, valorSaque):
        if self.saldo < valorSaque:
            print('Saldo insuficiente')
        else:
            self.saldo -= valorSaque
            return f'Saldo: {self.saldo}'
            

    def transferencia(self, paraQuem, valor):
        if self.Saque(valor):

            paraQuem.depositar(valor)
            

            print(self)
            print(paraQuem)
        else: 
            print('Tranferência não realizada')


    
if __name__ == '__main__':
    p1 = Conta(12234,'Victor', 90000,8)
    #print(p1)
    p2 = Conta(54321, 'Simone', 90000, 8)
    #p2.transferencia(p1, 300)
    #print(p1.__class__.__name__)
    #print(p1.__class__.__dict__)
'''    


# import datetime

# class Cliente(object):    
#     def __init__(self, nome, objeto, cpf ):
#         self.nome =nome
#         self.objeto = objeto
#         self.cpf = cpf
    
#     def nomeCompleto(self):
#         print(f'Nome:  {self.nome}')

    
#     def getObject(self):
#         print(f'All data object: {self.objeto}')

    
#     def getStrato(self):
#         print(f'Saldo: {self.objeto.saldo}')

#     def __str__(self):
#         return f'''     
#         --Dados conta {self.nome}--

#         Número: {self.objeto.numero}
#         Nome do cliente: {self.nome}
#         Saldo: {self.objeto.saldo}
#         Limite: {self.objeto.limite}
#         '''
#     def setNome(self, setnome):
#         self.nome = setnome
#         return f'Nome alterado com SUCESSO!! para {self.nome}'
        

# #AGREGAÇÃO : CLIENTE ESTÁ AGREGADO À CONTA

# class Conta():
#     def __init__(self, numero, saldo , limite):
#         self.numero = numero
#         self.saldo = saldo
#         self.limite = limite
#         self.historico = Historico().historico


#     def getNumero(self):
#         print(f'Número: {self.numero}')
#         self.historico.append('Vendo número da conta')

    
#     def depositar(self,valor):
#         self.saldo += valor
#         self.historico.append('Depositar')
#         print('Depositado com sucesso ')
#         return self.saldo

#     def setNumero(self,setNumero):
#         self.numero = setNumero
#         return f'Número alterado para {setNumero}'

#     def setNome_cliente(self, novoNome):
#         self.nome_cliente = novoNome
#         return 'Nome alterado para ', novoNome
#         self.historico.append('Mundança de nome')


    
#     def Saque(self, valorSaque):
#         if self.saldo < valorSaque:
#             print('Saldo insuficiente')
#         else:
#             self.saldo -= valorSaque
#             return f'Saldo: {self.saldo}'
        
#         self.historico.append('Saque')
            

#     def transferencia(self, paraQuem, valor):
#         if self.Saque(valor):

#             paraQuem.depositar(valor)
            

#             print(self)
#             print(paraQuem)
#         else: 
#             print('Tranferência não realizada')
        
#         self.historico.append('Transferência')


# #COMPOSIÇÃO: HISTORICO DEPENDE DE OUTRA CLASSE

# class Historico():
#     def __init__(self):
#         self.data = datetime.date.today()
#         self.hora = datetime.time
#         self.historico = []

#     def getDataDeAbertura(self):
#         return f'A conta foi aberta no dia {self.data}, na hora {self.hora} '

#     def getTransacoes(self):
#         self.historico.append()

#     def mostraHistorico(self):
#         self.historico.append(f'Histórico do dia {self.data}')

#         for n in self.historico:
#             print(f'- {n}')
    

    



# if __name__ == '__main__':
#     conta = Conta('1234',  99999999, 8)
#     cliente  = Cliente('Victor Murta Garcia',conta, 1223455)
    

    

#     #print(f'C1: {conta1.getNome_Cliente}')
#     cliente.nomeCompleto()
#     cliente.getObject()
#     print(cliente)
#     print(cliente.setNome('Murta'))
#     h = Historico()
#     h.mostraHistorico()

    

class Cliente():
    
    def __init__(self,nome , idade , endereços):
        self.nome = nome
        self.idade = idade
        self.endereços = []
    
    def getNome(self):
        print(f'Nome do cliente: {self.nome}')
    def inserEndereco(self, cid, est):
        End = Endereco('Bsb', 'Ag')
    
class Endereco():
    def __init__(self, cidade, estado):
        self.ciade = cidade
        self.estado = estado
    def getCidade(self):
        print(f'Cidade do cliente {Cliente().nome}: {self.ciade}')


if __name__ == '__main__':
    cliente = Cliente('Victor', 19, 'endereco')










