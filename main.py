import Cal
import Letras
import Operadores
import Operacion
import re






#ingresa la expresion
print("Ingresa tu expresion: ")
exp = input()





if(Letras.validaLetras(exp) == 0):
 Operacion.priori(exp)

