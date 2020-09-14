# -*- coding: utf-8 -*-
from plex import *
from tabulate import tabulate
import sys

"""
    *Generador de Analizadores Léxicos: Plex (Lex para Python)
    ! Funciona en Python 2.7
    ? Programa de ejemplo para la generación de un analizador léxico que comprende:
    ? Comentarios, cadenas, operador de suma y concatenación, espacios, tabulados y saltos de linea
    @author swd
    @date 2020/07/21
    @version 0.1
"""
# sudo apt install python-pip
# #sudo -H python -m pop install tabulate

class LexicalAnalysis:

    #Str, Rep, AnyBut, Any
    def __init__(self):

        #Cadena de texto: /"[^"]*"/
        stringDouble = Str("\"") + Rep(AnyBut("\"")) + Str("\"")
        stringSimple = Str("'") + Rep(AnyBut("'")) + Str("'")

        #Espacioes en blanco y comentarios
        space = Any(" \t\n")
        comment = Str("{") + Rep(AnyBut("}")) + Str("}")

        #Operadores
        assingOp = Str("=")
        sumOp = Str("+") #/\+/

        #Palabras reservadas (e.g.)
        ifKeyword = Str("if")

        self.lexicon = Lexicon(
            [
                (stringDouble, "string"),
                (stringSimple, "string"),
                (sumOp, "sum/concat operator"),
                (assingOp, "assing operator"),
                (space | comment, IGNORE)
            ]
        )

    def parse(self):

        lexicon = self.lexicon
        lexicalTable = []

        filename = sys.argv[1:][0]
        f = open(filename, "r")
        scanner = Scanner(lexicon, f, filename)

        while True:
            try:
                token = scanner.read()

                if not token[0]: break

                desc, val = token
                lexicalTable += [[val, desc]]

            except Exception as e:
                print ("Lexical Error: %s" % (e)) 
                f.close()
                return False

        f.close()
        self.lexicalTable = lexicalTable
        return self

parser = (LexicalAnalysis())

if parser.parse():
    print "Analisis Léxico: "
    print tabulate(parser.lexicalTable)
