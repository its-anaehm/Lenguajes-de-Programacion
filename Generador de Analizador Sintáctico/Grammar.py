# -*- coding: utf-8 -*-

grammar = """

    //El axioma inicial
    ?start: exp+

    //Definición de una expresión
    ?esp: var "=" string ";" -> assingvar
        | var "=" arithmeticoperation ";" -> assignvar
        | "print" "("? string ")"? ";" -> print
        | "print" "("? var ")"? ";" -> printvar

    //Definición de una iperación aritmética
    ?arithmeticoperation: arithmeticoperationatom 
        | arithmeticoperation "+" arithmeticoperationatom -> sum
        | arithmeticoperation "-" arithmeticoperationatom -> sub

    //Definición de un átomo de operación aritmética
    ?arithmeticoperationatom: var -> getvar
        | number
        | "-" arithmeticoperationatom
        | "(" arithmeticoperation ")"

    //Definición de una cadena
    ?string: /"[^"]*"/
        | /'[^']*'/

    //Definición de una variable 
    ?var: /[a-zA-Z]\w*/

    //Definición de un número
    ?number: /\d+(\.\d+)?/

    //Ignorar espacios, saltos de línea y tabulados
    %ignore /\s+/
"""