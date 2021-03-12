#associação: uma classe não depende da outra


class Escritor:
    def __init__(self, nome):
        #atributo privado 
        self.__nome = nome
        self.__ferramenta = None

    @property
    def getNome(self):
        return self.__nome

    @property
    def getFerramenta(self):
        return self.__ferramenta

    @getFerramenta.setter
    def getFerramenta(self, setFerramenta):
        self.__ferramenta = setFerramenta

class Caneta:
    def __init__(self, marca):
        #setter
        self.__marca = marca

    #getter
    @property
    def getMarca(self):
        return self.__marca
    
    def escrever(self):
        print('Caneta escrevendo ...')

class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina escrevendo ...')


if __name__ == "__main__":
    escritor = Escritor('Victor Murta')
    print(escritor.getNome)

    caneta = Caneta('Bic')
    print(caneta.getMarca)

    maquina = MaquinaDeEscrever()
    maquina.escrever()

    #associação

    escritor.meioDeEscrita = caneta
    #escritor.meioDeEscrita = maquina
    escritor.meioDeEscrita.escrever()

