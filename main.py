import Cal
import Letras
import Operadores
import Operacion
import re
#ingresa la expresion
print("Ingresa tu expresion: ")
exp = input()

patrondeci = '(\d*.\d*[/])'# numeros del numerador
dcilist = re.findall(patrondeci,exp);
print(dcilist);

cadena = Operacion.converToString(dcilist)
lista = re.findall(patrondeci,cadena)
print(lista)
nuevaCad = Operacion.converToString(lista)
cadenaNumeradores = re.sub('/','',nuevaCad)
print(cadenaNumeradores)
listaNueva = cadenaNumeradores.split(sep=' ')
print(listaNueva)
for i in range(0,len(listaNueva)):
  if(listaNueva[i]!=''):
    print(listaNueva[i])

#validamos las letras en la expresion
#if Letras.validaLetras(exp) == 0 :  #QUIERE DECIR QUE LA EXPRESION NO TIENE LETRAS O CARACTERES QUE NO SEAN NUMERO
   # cadena = Operadores.primerOperador(exp) 
    #Operadores.Opera(cadena)
  #Operacion.priori(exp)
  











#OPERADORES
#patron_op = '([\sa-z][\>][^\r][^\#][\s0-9]|[|>][0-9]|[0-9\s][\<][^a-z]|&|=|[*]|[+]|%|[-])'
#patron2 = '[a-zA-Z]'##Esto dice que encontro almenos una letra
#patron3 = '[^\s\da-zA-Z]'
#opelist = re.findall(patron2,exp);
#print(opelist)

#print("Hay: ",str(len(opelist)),"Operadores y son: ")
#print(opelist);


