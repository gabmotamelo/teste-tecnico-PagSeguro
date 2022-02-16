from frete import Produtos
from frete import Frete
from frete import CustoEntregas


# Produtos que irão ser calculados
produtos = [{'Produto': 'Fone de Ouvido', 'Distancia': 1, 'Peso': 1},
            {'Produto': 'Controle Xbox', 'Distancia': 1, 'Peso': 3},
            {'Produto': 'Pc Gamer', 'Distancia': 1, 'Peso': 35},
            {'Produto': 'Fone de Ouvido', 'Distancia': 430, 'Peso': 1},
            {'Produto': 'Fone de Ouvido', 'Distancia': 33, 'Peso': 1},
            {'Produto': 'Fone de Ouvido', 'Distancia': 50, 'Peso': 1},
            {'Produto': 'Controle Xbox', 'Distancia': 100, 'Peso': 3},
            {'Produto': 'Kit Gamer', 'Distancia': 1000, 'Peso': 5},
            {'Produto': 'Teclado+Fone', 'Distancia': 5, 'Peso': 6},
            {'Produto': 'Pc Gamer', 'Distancia': 1000, 'Peso': 35}]

# Empresas transportadoras
empresas = [{'Nome': 'BoaDex', 'ValorFixo': 10, 'ValorKmKg': 0.05},
            {'Nome': 'BoaLog', 'ValorFixo': 4.30, 'ValorKmKg': 0.12},
            {'Nome': 'Transboa-5kg', 'ValorFixo': 2.10, 'ValorKmKg': 1.10},
            {'Nome': 'Transboa+5kg', 'ValorFixo': 10, 'ValorKmKg': 0.01}]

# Classe a ser chamada com os determinados parâmetros
resultadoCotacao = Frete(produtos, empresas)  

# Classe e função a ser chamada para impressão da cotação
CustoEntregas.custoFrete(resultadoCotacao)  