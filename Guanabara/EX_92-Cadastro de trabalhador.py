from datetime import date
ano_atual= date.today().year

def verificar_digitos(valor):
    while not valor.isdigit():  # Loop enquanto não for um número válido
        valor = input('Valor inválido. Digite novamente: ')
    return int(valor)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

usuario = {
    'nome': input('Nome: '),
    'ano_nasc': verificar_digitos(input('Ano de nascimento: ')),
    'ctps': verificar_digitos(input('Carteira de trabalho (Caso não tenha, digite 0.): '))
}
usuario['idade'] = ano_atual - usuario['ano_nasc']

if usuario['ctps'] != 0:
    usuario['ano_contrato'] = verificar_digitos(input('Ano de contratação: '))
    usuario['salario'] = verificar_digitos(input('Salário: '))
    usuario['contribuicao'] = ano_atual - usuario['ano_contrato']
    usuario['aposentadoria'] = (usuario['idade'] + 35) - usuario['contribuicao'] #foram considerados 35 anos de contribuição para se aposentar.

    print(f"{usuario['nome']}, nascido em {usuario['ano_nasc']}, atualmente com {usuario['idade']} anos. Foi contratado no ano de {usuario['ano_contrato']}, com o salário no valor de R${usuario['salario']}. Atualmente tem {usuario['contribuicao']} anos de contribuição e se aposentará com {usuario['aposentadoria']} anos.")

else:
    print(f"{usuario['nome']}, nascido em {usuario['ano_nasc']}, atualmente com {usuario['idade']} anos, está desempregado.")