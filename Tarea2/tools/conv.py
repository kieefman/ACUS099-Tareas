# Importamos librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

def escalon(n: np.ndarray):
    """Función Escalon centrada en cero

    Args:
        n (np.ndarray): Vector tiempo discreto en muestras

    Returns:
        np.ndarray: Array con funcion escalón
    """
    return 1*(n >= 0)


def delta(n: np.ndarray, p: int):
    """Función Delta Escalón centrada en p

    Args:
        n (np.ndarray): Vector tiempo discreto en muestras
        p (int): Posición deseada

    Returns:
        np.ndarray: Array con 1 en posición p
    """
    return 1*(n == p)  # Ingresa 1 en posicion p

# Definimos x[k]


def signal1(n: np.ndarray, a:int):
    """Señal x[n] Ejemplo 2.13 Oppenheim & Schaffer

    Args:
        n (np.ndarray): Vector tiempo discreto en muestras
        a (int): Base función exponencial

    Returns:
        np.ndarray: Array con la función exponencial
    """
    return a**n * escalon(n)

# Definimos h[n-k]


def signal2(n: np.ndarray, N:int):
    """Señal h[n] Ejemplo 2.13 Oppenheim & Schaffer

    Args:
        n (np.ndarray): Vector tiempo discreto en muestras
        N (int): Ancho de Escalon Acotado

    Returns:
        np.ndarray: Array con Escalón Acotado
    """
    return np.roll(escalon(n) - escalon(n-N), 1)

# Definimos solucion analitica problema


def conv_calc(n: np.ndarray, a:float, N:int):
    """Solución Analitica Ejemplo 2.13 Oppenheim & Schaffer

    Args:
        n (np.ndarray): Vector tiempo discreto en muestras
        a (float): Base de Exponencial Real 
        N (int): Ancho del Escalón Acotado

    Returns:
        np.ndarray: Solución Analtica Suma de Convolución
    """    
    if n < 0:
        return 0
    elif 0 <= n <= N - 1:
        return (1 - a**(n+1)) / (1 - a)
    else:
        return a**(n - N + 1) * (1 - a**N) / (1 - a)


def convpos(n:np.ndarray, p:int, a, N):
    return conv_calc(p, a, N) * delta(n, p)