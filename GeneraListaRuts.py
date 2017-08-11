from random import randrange
import sys
import getopt
import os
import pyperclip


def genera_rut():
    MAX_DIGITS = 10
    NUMERO_DIGITOS = randrange(7, 9)
    DIGITOS = []
    sum_dig = 0
    multiplicador = 2
    for i in range(0, NUMERO_DIGITOS):
        dig_ran = randrange(10)
        DIGITOS.append(dig_ran)
        dig_mult = dig_ran*multiplicador
        sum_dig += dig_mult
        multiplicador = multiplicador + 1
        if multiplicador > 7:
            multiplicador = 2
    if len(DIGITOS) < MAX_DIGITS:
        ceros = MAX_DIGITS - len(DIGITOS)
        for i in range(ceros):
            DIGITOS.append(0)
    DIGITOS.reverse()

    resto = sum_dig % 11
    digito_v = 11 - resto
    if digito_v == 11:
        digito_v = 0
    elif digito_v == 10:
        digito_v = 'K'

    DIGITOS.append(digito_v)

    # Abrimos el archivo en modo "update" si el archivo existe, caso contrario se crea
    archivo = (open('ruts.txt', 'a') if os.path.isfile('ruts.txt') else open('ruts.txt', 'w+'))

    # Mientras el archivo esta abierto, ingresa el rut e imprime un salto de linea al final
    with archivo as f:
        for i in range(len(DIGITOS)):
            f.write(str(DIGITOS[i]))
        f.write('\n')


def genera_lista_ruts(cantidad):
    for i in range(cantidad):
        genera_rut()


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "n:", ["nruts="])
    except getopt.GetoptError:
        print('Uso: python GeneraListaRuts.py -n <Numero de Ruts Deseados>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-n':
            try:
                numeroruts = int(arg)
                genera_lista_ruts(numeroruts)
                print("Lista de RUTS generada, abriendo archivo...")
                os.system("start ruts.txt")
                print("Copiando al portapapeles...")
                pyperclip.copy(open('ruts.txt', 'r').read())
                print("Ctrl+v para pegar el contenido.")
            except ValueError:
                print("El argumento no es un numero entero")

if __name__ == "__main__":
    main(sys.argv[1:])


