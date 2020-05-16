import re
import Cal
def opera(exp):
  op_division = '(\d*.\d*[/]\d*.\d*)'
  #patron_decimales = '\d+[*]+\d+'#ENCUENTRA OPERADOR 
  
 # patron_enteros   = '^(\d+|\d+[.]\d+)[+]^(\d+|\d+[.]\d+)'
  
  opelist = re.findall(op_division,exp)#saco los 
  #print(opelist)
 # op1 = re.split(exp,'*')
  #print(op1)
  
  #print(exp.split(patron_decimales))
  

def converToString(opelist):
  cadena = ''
  for i in range(0,len(opelist)):
    cadena = cadena+' '+opelist[i]
  return cadena


#Esta funcion valida que en la cadena de solo divisiones, se pueda divir
def validaDivision(exp_cadena): 
  valido = 1;
   #RECORREMOS LA CADENA
  for i in range(len(exp_cadena)):
      #SI ALGUN CARACTER DE LA CADENA ES DIVISION, TOMAREMOS EL SIGUIENTE Y EL ANTERIOR A LA DIVISION.
      if(exp_cadena[i] == '/'): 
          if(int(exp_cadena[i+1]) == 0 ): #0 = no es valido,
            valido = 0        
  return valido       
            
            
  





def primerOperador(exp):
  op_division = '\d+[/]+\d+'
  opelist = re.findall(op_division,exp)#saco los 
#  print(opelist)

  #CONVIERTE LA LISTA EN CADENA
  cadena = converToString(opelist)
  
  #Enviamos la cadena de 1er operador(DIVISION), para validar si es posible.
  if(validaDivision(cadena) == 0): #regresa 1  si es posible y 0 si no es posible
    return ' '
  else:
    return cadena

  
 



  #Obtenemos la lista en cadena, lista para operar.
  #print(cadena)   

    
  
def Opera(cadena):
  #Si entra a este if, la division se puede hacer y esta validada
  if(cadena != ' '):
    print("Divison valida")
  for i in range(0,len(cadena)):
      if(cadena[i] == '/'):
        num = Cal.division(int(cadena[i-1]),int(cadena[i+1]) )
       
        print(num)
       

      else:
        print("")  
         
  else:#la cadena no es valida
    print("Operacion no valida")  
         