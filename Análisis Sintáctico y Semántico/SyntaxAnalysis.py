# -*- coding: utf-8 _*_

"""
    ! Syntax Analysis (Analizador Sintáctico Demostrativo)
    ! Non-CFG
    * Permite el reconocimiento de ristintos tokens en el orden correcto de instrucciones.
    ? Comprende la lógica general de la demostración.
    ? Comprende identificadores de usuario.
    ? Comprende operador de asignación.
    ? Comprende valores númericos enteros y flotantes.
    ? Requiere fin de instrucción.
    ? Se comunica mediante pipeline
    @author swd
    @date 2020/07/13
    @version 0.1
"""

import re

class SyntaxAnalysis:
    pass

    def __init__(self):
        pass

    def help(self):

        print("")
        print("*"*80)
        print("*"*80)
        print("\tSyntax Analysis (Analizador Sintáctico Demostrativo) ")
        print("""
\ŧPermite el reconocimiento de distintos tokens en el orden correcto de instrucciones

\ŧ@author swd
\ŧ@date 2020/07/13
\ŧ@version 0.1""")
        print("*"*80)
        print("*"*80)
        print("")

    def read(self):
        self.text = input()
        return self

    def parse(self):
        text = self.text
        lines = re.split(r";",text)

        for i in range(len(lines)):
            
            line = ("%s".strip() % lines[i]).strip()
            if len(lines)>0:

                #regex.com
                if(
                    re.match(r"^[a-zA-Z][a-zA-Z\d_]*\s*=\s*\d+(\.\d+)?$",line) or
                    re.match(r"^[a-zA-Z][a-zA-Z\d_]*\s*=\s*[a-zA-Z][a-zA-Z\d_]*$", line)
                ):
                    pass
                else:
                    quit("Error sintáctico: se ha encontrado un error en la línea %d" % i)

        return True


parser = (SyntaxAnalysis()).read()

if parser.parse():
    print("%s" % parser.text)