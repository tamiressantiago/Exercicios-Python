def verificar_digitos(valor):
    while not valor.isdigit():  # Loop enquanto não for um número válido
        valor = input('Caractere inválido. Digite novamente: ')
    return int(valor)

continuar = 's'
jogadores = []

while continuar == 's':
    print('-' * 50)
    cadastro = { 'nome': input('Nome do jogador: '),
    }
    cadastro['partidas'] = verificar_digitos((input('Quantas partidas ' + cadastro['nome'] + ' jogou?: ')))
    gols = []
    for partida in range (1, cadastro['partidas'] + 1):
        gol = input(f"Quantos gols na partida {partida}?: ")
        gols.append(verificar_digitos(gol))
        cadastro['gols'] = gols
        cadastro['total'] = sum(gols)
    jogadores.append(cadastro)
    continuar = input('Deseja continuar? [S/N]: ').lower()
    while continuar != 's' and continuar != 'n':
        continuar = input('Resposta inválida. Responda com apenas S ou N: ')


print('=-' * 30)

print(f"{'cod':<4} {'nome':<15} {'gols':<25} total\n {'-' * 60}")

for i in range (len(jogadores)):
    gols_str = ', '.join(str(gol) for gol in jogadores[i]['gols'])
    print(f"{i:<4} {jogadores[i]['nome']:<15} {gols_str:<26} {jogadores[i]['total']}")

cod = 0

while cod != 999:
    print('=-' * 30)
    cod = verificar_digitos(input('Mostrar dados de qual jogador? (Digite 999 para encerrar): '))

    if cod < len(jogadores) and cod != 999:
        print(f"\nLevantamento do jogador {jogadores[cod]['nome']}:")
        for i in range(len((jogadores[cod])['gols'])):
            print(f"No jogo {i + 1} fez {jogadores[cod]['gols'][i]} gols")

    elif cod >= len(jogadores) and cod != 999:
        print('ERRO! Não existe jogador com este código. Tente novamente.\n')
    
    else:
        print('\n<<Programa encerrado>>')
