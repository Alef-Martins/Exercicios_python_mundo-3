#Fça um programa que tenha uma função chamada área(), que receba as dimenssões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(l, c):
    area = l * c
    print(f'A área de um terreno {l} x {c} é de {area}m²')


print('Controle de terrenos')
print('='*30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
