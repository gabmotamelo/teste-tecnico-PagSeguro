class Produtos(object):

    # Construtor da classe "Produtos"
    def __init__(self, dadosProduto):
        self.dadosProduto = dadosProduto

    # Função para obter as infos de "Produtos"
    def getProdutosInfo(self):
        return self.dadosProduto


# Classe que herda de "Produtos"
class Frete(Produtos):

    # Construtores da classe "Frete"
    def __init__(self, dadosProduto, dadosEmpresa):
        Produtos.__init__(self, dadosProduto) # Está invocando os construtores da classe "Produtos"
        self.dadosEmpresa = dadosEmpresa

    # Função para obter as infos das transportadoras
    def getTransportInfo(self):
        return self.dadosEmpresa


# Classe que herda de "Frete", e transitivamente, de "Produtos"
class CustoEntregas(Frete):

    # Construtor da classe "CustoEntregas"
    def __init__(self, dadosProduto, dadosEmpresa):
        Frete.__init__(self, dadosProduto, dadosEmpresa) # Está invocando os construtores da classe "Frete"

    # Função do cálculo do custo para cada transportadora
    def custoFrete(self):
        for objeto in self.dadosProduto:
            self.listaCustos = dict()
            print('\n')
            for empresa in self.dadosEmpresa:
                if objeto['Peso'] <= 5:
                    if empresa['Nome'] == 'Transboa+5kg':
                        pass
                    else:
                        self.custo = empresa['ValorFixo'] + (objeto['Peso'] * objeto['Distancia'] * empresa['ValorKmKg'])
                        self.listaCustos.update({empresa['Nome']: self.custo})
                elif objeto['Peso'] > 5:
                    if empresa['Nome'] == 'Transboa-5kg':
                        pass
                    else:
                        self.custo = empresa['ValorFixo'] + (objeto['Peso'] * objeto['Distancia'] * empresa['ValorKmKg'])
                        self.listaCustos.update({empresa['Nome']: self.custo})

            # Função para estilizar o código na hora que for executado
            def escreva(msg):
                tam =  60
                print(f'    {msg}')
                print('-' * tam)

            # Imprimindo os dados do produto e o preço que será cobrado por cada transportadora
            escreva(f"{objeto['Produto']} -  Distância:  {objeto['Distancia']} km -  Peso:  {objeto['Peso']} kg")
            for transportadora in sorted(self.listaCustos, key=self.listaCustos.get):
                escreva(f'{transportadora} = R$ {self.listaCustos[transportadora]:.2f}')



