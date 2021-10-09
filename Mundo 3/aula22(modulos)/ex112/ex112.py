from utilidades import moeda
from utilidades import dados

valor = dados.LeiaDinheiro('Digite o preço: R$')
moeda.resumo(valor, 32, 22)