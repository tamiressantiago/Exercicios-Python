def verificar_digitos(valor):
    while not valor.isdigit():  # Loop enquanto não for um número válido
        valor = input('Caractere inválido. Digite novamente: ')
    return int(valor)

cadastro = { 'jogador': input('Nome do jogador: ')}
cadastro['partidas'] = verificar_digitos((input('Quantas partidas ' + cadastro['jogador'] + ' jogou?: ')))

gols = []
for partida in range (1, cadastro['partidas'] + 1):
    gol = input(f"Quantos gols na partida {partida}?: ")
    gols.append(verificar_digitos(gol))
cadastro['gols'] = gols
cadastro['total'] = sum(gols)

print(cadastro)

print('=-' * 30)
print(f"O jogador {cadastro['jogador']} jogou {cadastro['partidas']} partidas.")
for partida in range (1, cadastro['partidas'] + 1):
    if gols[partida - 1] > 1:
        print(f"=> Na partida {partida}, fez {gols[partida - 1]} gols.")
    elif gols[partida - 1] == 1:
        print(f"=> Na partida {partida}, fez {gols[partida - 1]} gol.")
    else:
        print(f"=> Na partida {partida}, não fez nenhum gol.")

if cadastro['total'] > 1:
    print(f"Foi um total de {cadastro['total']} gols.")
else:
    print(f"Foi um total de {cadastro['total']} gol.")
