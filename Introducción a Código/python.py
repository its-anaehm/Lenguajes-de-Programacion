# -*- coding: utf-8 -*-

"""
    Conforman la Gramática: Léxico, Sintaxis y Semántica.

        E.g.:
          Cuidado, ¡Ladrón!.
            Cuidado ladrón.

    Manejo de errores en todo lenguaje de programación.
    Existen errores léxicos, sintácticos, gramaticales y semánticos en la generación de código.
    El manejo de errores identifica:
        El número de líneas donde ocurre el error.
        El tipo de error
        El caracter donde ocurre el error.
"""

"""
    ! Meétodo Factorial.
    * Permite calcular la multiplicación de n*(n-1)*(n-2)*...*(n-k), donde n-k >=1
    @author jose.inestroza@unah.edu.hn
    @version 0.1
"""

def factorial(n):
    if n<2: return 1
    return n*factorial(n-1)

m = 5
n = m
print("El factorial en Python para '%d' es: '%d'" % (n, factorial(n)))