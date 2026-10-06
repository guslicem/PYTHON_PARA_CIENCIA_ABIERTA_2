# mylib.py - Módulo auxiliar para el curso CSIC

import os

from time import time,sleep

def limpiar_pantalla():
    """
    Limpia la pantalla según el sistema operativo.
    Args:
        - Esta funcion no recibe argumentos. Detecta automaticamente el sistema operativo y ejecuta el comando correspondiente.
    Returns:
        - None
    """
    if(os.name=='nt'):
        os.system('cls')
    else:
        os.system('clear')
    
def linea(caracter='*', longitud=100):
    """
    Imprime una línea de separación personalizada.
    Args:
        caracter (str): Carácter a utilizar para dibujar la línea.
        longitud (int): Longitud de la línea.
    Returns: 
        - None
    """
    
    print(caracter * longitud)


if __name__ == "__main__":
    print("Probamos la funcion de limpiar pantalla, y la de imprimir linea")
    limpiar_pantalla()
  
    
    linea()
    sleep(5)
    linea('--',25)
    print('Hola')

    linea('#', 30)

    help(limpiar_pantalla)
    print(limpiar_pantalla.__doc__)