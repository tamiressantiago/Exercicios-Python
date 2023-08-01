from random import randint
from time import sleep
from rich import print
jogadores = {}


print("""[blue] =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
          SORTEANDO OS VALORES. . .[/blue]
""")
sleep(1)


for i in range(1, 5):
    dado = randint(1, 6)
    jogadores["Jogador " + str(i)] = dado
print('Valores sorteados:')


for chave in jogadores:
    valor = jogadores[chave]
    print(f"{chave}: {valor}")
    sleep(1)

print('[blue]\nRanking dos jogadores:[/blue]')
sleep(1.4)

dicionario_ordenado = dict(sorted(jogadores.items(), key=lambda item: item[1],reverse=True)) #O key=lambda item: item[1]' faz com o sort seja feito a partir dos valores que os jogadores obtiveram. Se quiser fazer com as chaves ao invés dos valores, use item[0].

posicao = 0
for chave in dicionario_ordenado:
    posicao += 1
    valor = dicionario_ordenado[chave]
    if posicao == 1:
        print(f"[green]{posicao}º lugar:[/green] {chave} com {valor}")
    else:
        print(f"[yellow]{posicao}º lugar:[/yellow] {chave} com {valor}")
    sleep(0.5)