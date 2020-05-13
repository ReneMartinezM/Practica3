import Cal
import Letras
import Operadores


print("Ingresa tu expresion: ")
exp = input()
print(exp)


if Letras.validaLetras(exp) == 0 :  #QUIERE DECIR QUE LA EXPRESION NO TIENE LETRAS O CARACTERES QUE NO SEAN NUMERO
    Operadores.proximoOperador(exp)
else :
  print("Operacion no valida")    




#OPERADORES
#patron_op = '([\sa-z][\>][^\r][^\#][\s0-9]|[|>][0-9]|[0-9\s][\<][^a-z]|&|=|[*]|[+]|%|[-])'
#patron2 = '[a-zA-Z]'##Esto dice que encontro almenos una letra
#patron3 = '[^\s\da-zA-Z]'
#opelist = re.findall(patron2,exp);
#print(opelist)

#print("Hay: ",str(len(opelist)),"Operadores y son: ")
#print(opelist);






