import random
from palavras import palavras
import string


def jogo_forca():
    palavra = random.choice(palavras).upper()
    letras_palavra = set(palavra) #letras na palavra
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set()
    vidas = 6

    while len(letras_palavra) > 0 and vidas > 0:

        #informa letras utilizadas
        print('Você tem ', vidas, ' vidas restantes. Letras já utilizadas: ', ' '.join(letras_usadas))

        #informa o estado da palavra
        lista_palavras = [letra if letra in letras_usadas else '-' for letra in palavra] 
        print(' '.join(lista_palavras))

        letra_digitada = input('\nAdivinhe uma letra: ').upper()
        if letra_digitada in alfabeto - letras_usadas:
            letras_usadas.add(letra_digitada)
            if letra_digitada in letras_palavra:
                letras_palavra.remove(letra_digitada)
            else:
                vidas = vidas - 1
                print('Esta letra não está na palavra.')

        elif letra_digitada in letras_usadas:
            print('Você já digitou essa letra antes. Tente novamente.')

        else:
            print('Caractere inválido. Tente novamente.')
    
    if vidas == 0:
        print('Você morreu. \nA palavra era', palavra)
    else:
        print('Você adivinhou corretamente a palavra', palavra, '!!!')

if __name__ == '__main__':
    jogo_forca()

print('\nFIM DE JOGO.')