import re
import Cal

def priori(exp_principal):
  exp_div     = '(\d*.\d*[/]\d*.\d*)'
  exp_mult    = '\d+[*]+\d+'
  cadenaTotal = ' '#aqui se guarda toda la operacion

  #1 en prioridad la Division          
  lista = verificaOperador(exp_div,exp_principal)
  if( lista != 0):
    print('Division valida')
    cadena      =  converToString(lista)
    if(validaDivision(cadena) == 1):
      cad_libre     = liberaSeparaExpresion(cadena,'/')
      cadena_result = realizaDivision(cad_libre)
      cadenaTotal   = modificaExpresion(lista,cadena_result,exp_principal)
      #print(cadenaTotal)
    else:
      print("Division entre cero invalida")
  else:
    print('Divsion Invalida')
  #2 en priorirdad la Multiplicacion
  """lista = verificaOperador(exp_mult,cadenaTotal)
  if(lista != 0):
     print('Multiplicacion valida')
     print(lista)
  else:
    print('Multiplicacion Invalida') 
    """



def verificaOperador(ope,exp):
  opelist = re.findall(ope,exp)
  if(len(opelist) > 0 ):
      print("Hay almenos un operador" )
      return opelist
  else: 
      print("No Hay  un operador")
      return 0



def converToString(opelist):
  cadena = ' '
  for i in range(0,len(opelist)):
    cadena = cadena+' '+opelist[i]
  return cadena  

def validaDivision(cadena):
 exp1 = '/(0$|0\s|0\-|0\*|0\+|0.0)'
 lista = re.findall(exp1,cadena)
 
 if(len(lista)>0):
   return 0
 else:
   return 1  
 


def liberaSeparaExpresion(exp,operador):
  #Separo la expresion cada vez que haya una division
  lista = re.split(operador,exp)
  #La lista la paso a string y separo la cadena cada vez que hay espacios
  cadena = converToString(lista)
  nombreLista = re.split(" ",cadena)
  #Quito los Espacios de la lista que salio, para que no haya espacios
  nombreLista = [i for i in nombreLista if i ]
  #tenemos la lista separada
  return nombreLista

def realizaDivision(lista):

  #Este for es para hacer la operacion de la division
  cad = " "
  for i in range(0,len(lista)):
    if(i%2==0):
      num = Cal.division(float(lista[i]),float(lista[i+1]))
      cad = cad +" "+ format(num)
  
  return cad


        

def modificaExpresion(lt_patron,cad_result,exp_principal):

  nueva_cad = exp_principal
  lista_cad_result = cad_result.split() 

  for i in range(0,len(lt_patron)):
    nueva_cad = re.sub(lt_patron[i],lista_cad_result[i],nueva_cad)

  nueva_cad = sentence = re.sub(r"\s+", "", nueva_cad, flags=re.UNICODE)
  return nueva_cad 
 
 




     

   