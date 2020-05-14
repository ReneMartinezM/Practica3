import Cal
import Letras
import Operadores
import Operacion

#ingresa la expresion
print("Ingresa tu expresion: ")
exp = input()
#validamos las letras en la expresion
if Letras.validaLetras(exp) == 0 :  #QUIERE DECIR QUE LA EXPRESION NO TIENE LETRAS O CARACTERES QUE NO SEAN NUMERO
   # cadena = Operadores.primerOperador(exp) 
    #Operadores.Opera(cadena)
  Operacion.priori(exp)











#OPERADORES
#patron_op = '([\sa-z][\>][^\r][^\#][\s0-9]|[|>][0-9]|[0-9\s][\<][^a-z]|&|=|[*]|[+]|%|[-])'
#patron2 = '[a-zA-Z]'##Esto dice que encontro almenos una letra
#patron3 = '[^\s\da-zA-Z]'
#opelist = re.findall(patron2,exp);
#print(opelist)

#print("Hay: ",str(len(opelist)),"Operadores y son: ")
#print(opelist);






