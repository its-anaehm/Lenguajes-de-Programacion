;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Ejemplo de programa en Common Lisp
; usando SBCL
;
; @author swd
; @date 2020/07/22
; @version 0.1
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;Mensaje de bienvenida
(write-line "")
(write-line "")
(write-line "Escriva en pantalla un dato numérico: ")
(write-line "")

;Definir una variable y se le solicita el dato al usuario
(defvar *unaVariableCualquiera*)
(setf *unaVariableCualquiera* (read))
(write-line "")

;Se imprimen los resultados de una operación cualquiera
(write-line "El resultado de su número * 5 es: ")
(write (* 5 *unaVariableCualquiera*))
(write-line "")