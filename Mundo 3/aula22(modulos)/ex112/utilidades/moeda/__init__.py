def moeda(preço=0):
    return f'{preço:.2f}'.replace('.', ',')


def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def resumo(preço=0, aumento=10, redução=5, valor='R$'):
    print('='*30)
    print('RESUMO DE VALORES'.center(30))
    print('='*30)
    if ',' in preço:
        preço = preço.replace(',', '.')
    preço = float(preço)
    print(f'Preço analisado: \t{valor}{moeda(preço)}')
    print(f'Dobro do preço: \t{valor}{dobro(preço, True)}')
    print(f'Metade do preço: \t{valor}{metade(preço, True)}')
    print(f'{aumento}% de aumento: \t{valor}{aumentar(preço, aumento, True)}')
    print(f'{redução}% de redução: \t{valor}{diminuir(preço, redução, True)}')
    print('='*30)