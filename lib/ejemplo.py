# script_ejemplo.py

# 1. Importaciones
import math  # Librería estándar para cálculos matemáticos

# 2.1 Definiciones (funciones)
def calcular_area_heron(a, b, c):
    """
    Calcula el área de un triángulo dados sus tres lados usando la fórmula de Herón.
    Si los lados no forman un triángulo válido (incluyendo el caso degenerado),
    devuelve None.
    - Args: 
        - a: Longitud del primer lado.
        - b: Longitud del segundo lado.
        - c: Longitud del tercer lado.
    - Returns:
        - float: Área del triángulo.
        - None: Si los lados no forman un triángulo válido.
    
    """
    # me gustaria que devolviera el area y los otros valores
    
    
    # Verificación de desigualdad triangular (estricta)
    if not ((a + b > c) and (a + c > b) and (b + c > a)):
        return None  # No es un triángulo válido

    # Cálculo con fórmula de Herón
    s = (a + b + c) / 2  # Semiperímetro
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area 

# 2.2 Aquí podrían ir las definiciones de clases

# 3. Bloque principal

if __name__ == "__main__":
    print("Cálculo del área de un triángulo con la fórmula de Herón")

    # Pedir al usuario los tres lados del triángulo
    a = 3.0  # (Reemplazado para ejecución automática desatendida)
    b = 4.0
    c = 5.0

    # Calcular el área con los valores introducidos
    area = calcular_area_heron(a, b, c)

    # Mostrar el resultado
    print(f'El área triángulo de lados {a,b,c} es {area}')

