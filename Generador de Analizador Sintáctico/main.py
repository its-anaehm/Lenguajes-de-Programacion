# -*- coding: utf-8 -*-

"""
    ! Anaizador Sintáctico para lenguajes de prueba, usando Lark
    ! Se incluyen los componentes de Reader, Semantic  y Grammar del mismo autor.
    @author swd
    @date 2020/07/21
    @version 01
"""

import sys
from Reader import Reader
from Semantic import Semantic
from lark import Lark, Transformer
from Grammar import *

reader = (Reader()).read()
parser = Lark(grammar, parser="lalr", transformer= Semantic())
language = parser.parse

sample = reader.text
try:
    language(sample)
except Exception as e:
    print ("Error: %s" % e)