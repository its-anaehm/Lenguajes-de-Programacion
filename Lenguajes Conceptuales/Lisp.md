PAC II 2020 - LLP 1100
@author swd
@date 2020/07/22
@version 0.1

LISP
======

* Es un lenguaje de proposito general.
* Integers, Ratios, Complex Numbers, Strings, Arrays, Vectors, Hash Tables, Functions, Streams.
* Expresiones -S se definen, recursivamente, como:
  * Un tipo de dato simple, el cual se llama "átomo".
    * Un átomo corresponde con: número, listas, cadenas de caracteres y símbolos.
  *  Una lista de expresiones -S donde una expresión -S podría ser una lista de expresiones -S, que a su ves podria ser listas, y se pueden obtener expresiones anidadas de cualquier nivel de profundidad.

Expresión -S (S-expression)
------

* Expresión simbólica: es una notación de forma de texto usada en la representación de estructuras de arbol, está basada en listas anidadas, en donde cada sublista es un subárbol las expresiondes-S se usan en la familia de lenguajes de programación LISP. Su representación es mediante secuencias de cadenas de caracteres, delimitadas por parentesis, y separadas por espacios: (= 4 (+ 2 2)). En C este ejemplo seria: 4 == 2 + 2.
  
Common LISP
------

* https://lisp-lang.org/
* Requiere el uso de notificación pre-fija.
* En consola lo ejecutaremos usando un programa SBCL (sudo aptitude).
  * http://www.sbcl.org
  * http://www.sbcl.org/manual

    #
        $ sbcl
        This is SBCL 1.3.1.debian, an implementation of ANSI Common Lisp.
        More information about SBCL is available at <http://www.sbcl.org/>.

        SBCL is free software, provided as is, with absolutely no warranty.
        It is mostly in the public domain; some portions are provided under
        BSD-style licenses.  See the CREDITS and COPYING files in the
        distribution for more information.
        * (+ 1 1)

        2
        * (exit)
    #

* Ejemplos:
    #
        (+ 1 2)
        (+1 1 (+ 1 1))
        (* (+ 1 2) (- 3 4)) ;Observe que existen espacios que separan cada elementode la instrucción
        (+ (+ 3 4) (+ (+ 4 5) 6))
        (+ 3 4 6 6) ;La función de adición puede tomar más de un parámetro
        (defun function (x,y) (+ x y 5)) ;La definición de una función.
        (let ((x 10)) x)
        (let ((y 10)) (- y 10))
        (list 4 5 6)
    #

* Para ejecutar un script:
    #
        $ sbcl --script programa.lisp
    #

* Tome en cuenta que:
    * SET que puede establecer el valor de símbolos.
    * SETQ puede establecer el valor de variables.
    * SETF es un macro, posee la capacidad de definir elementos: símbolos, variables, elementos de un arreglo, instancias, etc.

* Ejemplo de perición de datos:
    #
        (write (+ 1 (read)))
    #

* Ejemplo (sin importar resultados):
    #
        (defvar *unaVariableCualquiera*)
        (setf *unaVariableCualquiera* 42.1)
        (* 2.1 *unaVariableCualquiera*)
    #

* Ejemplo de función y ejecución de función:
    #
        ; Se define una función
        (defun square (x) (* x x))

        ; Se usa la función
        (write (square 3))
    #

* Ejercicio de un programa que imprime mensajes en pantalla y recibe datos de usuario

* Ejercicio de factorial que imprime el resultado en pantalla de un número fijo.
    #
* Por lo tanto el estudiante debe:
    * Orientar su pensamiento a la creación de programas basados en otros paradigmas conceptuales, donde existe la posibilidad de aplicar múltiples formas gramaticales para resolver operaciones, usando el generador de analizadores léxicos Plex y el generador de analizadores sintácticos Lark.
  