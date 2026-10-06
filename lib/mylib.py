# mylib.py - Módulo auxiliar para el curso CSIC

import os


from time import time,sleep

def limpiar_pantalla():
    """
    Limpia la pantalla según el sistema operativo.
    """
    if(os.name=='nt'):
        os.system('cls')
    else:
        os.system('clear')
    
def linea(caracter='*', longitud=100):
    '''Imprime una línea de separación personalizada.'''
    print(caracter * longitud)


if __name__ == "__main__":
    print("Probamos la funcion de limpiar pantalla, y la de imprimir linea")
    limpiar_pantalla()
    linea()
    linea('@',25)
    
    print('Hola')

    #limpiar_pantalla()
    linea('#', 30)