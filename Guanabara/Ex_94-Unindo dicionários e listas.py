def verificar_digitos(valor):
    while not valor.isdigit():  # Loop enquanto não for um número válido
        valor = input('Caractere inválido. Digite novamente: ')
    return int(valor)

continuar = 's'
usuarios = []
soma = 0
while continuar == 's':
    cadastro = {}
    cadastro['nome'] = input('Nome: ')
    sexo = input('Sexo [F/M]: ').upper()
    while sexo != 'F' and sexo != 'M':
        sexo = input('Resposta inválida. Responda com apenas F ou M: ').upper()
    cadastro['sexo'] = sexo
    cadastro['idade'] = verificar_digitos(input('Idade: '))
    soma += cadastro['idade']
    usuarios.append(cadastro)
    continuar = input('Quer continuar? (S/N): ').lower()
    while continuar != 's' and continuar != 'n':
        continuar = input('Resposta inválida. Responda com apenas S ou N: ')

pessoas = len(usuarios)
media = soma/pessoas
mulheres = []
acima_media = []
for i in range (pessoas):
    if usuarios[i- 1]['sexo'] == 'F':
        mulheres.append(usuarios[i- 1]['nome'])
    
    if usuarios[i- 1]['idade'] > media:
        acima_media.append(usuarios[i- 1]['nome'])



print('=-' * 30)
print(f"""A) Ao todo temos {pessoas} pessoas cadastradas.
B) A média de idade é de {media:.1f} anos.
C) As mulheres cadastradas foram {', '.join(mulheres)}.
D) Lista das pessoas que estão acima da média:
{', '.join(acima_media)}

<< Encerrado >>
""")
