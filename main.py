import Cal
import Letras
import Operadores


print("Ingresa tu expresion: ")
exp = input()



if Letras.validaLetras(exp) == 0 :  #QUIERE DECIR QUE LA EXPRESION NO TIENE LETRAS O CARACTERES QUE NO SEAN NUMERO
    cadena = Operadores.primerOperador(exp) 
    if(cadena != ' '):
      print("Divison valida")
      for i in range(0,len(cadena)):
        print(cadena[i])
        if(cadena[i] == '/'):
         # numA = cadena[i-1]
         # numB = cadena[i+1]
         # print(numA)
          #num = Cal.division(int(numA),int(numB))
          #cadena[i] = num
          #cadena[i-1] = ''
          #cadena[i+1] = ''
          num = Cal.division(int(cadena[i-1]),int(cadena[i+1]) )
          print(num)
          cadena[i] = chr(num)
      #print(cadena)
    else: 
      print("Division invalida")  

else:
  print("Operacion no valida")    




#OPERADORES
#patron_op = '([\sa-z][\>][^\r][^\#][\s0-9]|[|>][0-9]|[0-9\s][\<][^a-z]|&|=|[*]|[+]|%|[-])'
#patron2 = '[a-zA-Z]'##Esto dice que encontro almenos una letra
#patron3 = '[^\s\da-zA-Z]'
#opelist = re.findall(patron2,exp);
#print(opelist)

#print("Hay: ",str(len(opelist)),"Operadores y son: ")
#print(opelist);






