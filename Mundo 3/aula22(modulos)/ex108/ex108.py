#Adapte o código do exercício 107, ciando uma função adicional chamada moeda() que consiga mostrar números com um valor monetário formatado.
import moeda
valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(valor)} é R${moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de R${moeda.moeda(valor)} é R${moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentando 10% temos {moeda.moeda(moeda.aumentar(valor, 10))}')
print(f'Diminuindo 10% temos {moeda.moeda(moeda.diminuir(valor, 10))}')
