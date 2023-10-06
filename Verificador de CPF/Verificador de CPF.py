def digitoverificador (qntd, contador):
    soma = 0
    for numb in range (qntd):
        mult = int(cpf[numb]) * contador
        soma += mult
        contador -=1

    digitoverificador = 11 - (soma % 11)
    if digitoverificador > 9:
        digitoverificador == 0
    else:
        return digitoverificador
    
    return digitoverificador

def remover_simbolos(cpf):
    resultado = ""
    for caractere in cpf:
        if caractere.isdigit():
            resultado += caractere
    return resultado


cpf = input('Informe o CPF:')

if not cpf.isdigit():
    cpf = remover_simbolos(cpf)

primeiro_verificador = digitoverificador(9, 10)
segundo_verificador = digitoverificador(10, 11)

if primeiro_verificador == int(cpf[9]) and segundo_verificador == int(cpf[10]):
    print('CPF válido.')
else:
    print('CPF inválido.')
