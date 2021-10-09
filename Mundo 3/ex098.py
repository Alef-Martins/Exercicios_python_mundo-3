#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens da função criada:De 1 a 10 passo 1, de 10 até 0 passo 2 e contagem personalizada.
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('='*30)
    print(f'Contagem de {i} até {f} em {p}')
    if i < f:
        for c in range(i, f+1, p):
            print(c, end=' ', flush=True)
            sleep(0.5)
    elif i > f:
        p *= -1
        for c in range(i, f+1, p):
            print(c, end=' ', flush=True)
            sleep(0.5)
    print('FIM!')
    print('='*30)


contador(1, 10, 1)
contador(10, 0, 2)
print('Contagem personalizada')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
