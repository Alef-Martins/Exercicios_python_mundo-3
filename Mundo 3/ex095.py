#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de vizualização de detalhes do aproveitamento de cada jogador.
grupo = []
relatorio = {}
partidas = []
while True:
    relatorio.clear()
    partidas.clear()
    relatorio['Nome'] = input('Nome do jogador: ').capitalize()
    jogos = int(input(f'Quantas partidas {relatorio["Nome"]} jogou? '))
    total = 0
    for c in range (0, jogos):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
        total += partidas[c]
    relatorio['gols'] = partidas[:]
    relatorio['total'] = total
    grupo.append(relatorio.copy())
    while True:
        flag = input('Quer continuar? [S/N]: ').upper()
        if flag in 'SN':
            break
        print('ERRO! digite apena S ou N.')
    if flag == 'N':
        break

print(grupo)
print('-='*20)
print('cod ', end='')
for i in relatorio.keys():
    print(f'{i:<15}', end='')
print()
print('-='*30)
for k, v in enumerate(grupo):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)
while True:
    flag = int(input('Mostrar dados de qual jogador? [999 para sair] '))
    if flag == 999:
        break
    if flag -1 >= len(grupo):
        print('ERRO! O código não existe na lista')
    print('-='*30)
    for c in range(0, len(grupo)):
        if c == flag-1:
            print(f'O jogador {grupo[c]["Nome"]} jogou {len(grupo[c]["gols"])} partidas')
            print(f' --- LEVANTAMENTO DO JOGADOR \033[32m{grupo[c]["Nome"]}\033[m')
            for c in range (0, len(grupo[flag-1]['gols'])):
                print(f'    No jogo {c+1} fez {grupo[flag-1]["gols"][c]} gols')
            print('-='*30)
        
