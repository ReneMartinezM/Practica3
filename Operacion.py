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
    cadena_div  =  Opera(cadena)
    #print(cadena)
    #cadenaTotal =  modificaExpresion(cadena_div,#exp_principal,lista)
   # print(cadenaTotal)
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



def Opera(cadena):
  cad = ' '
  #Si entra a este if, la division se puede hacer y esta validada
  print(cadena)
  if(cadena != ' '): 
    for i in range(0,len(cadena)):
      if(cadena[i] == '/'):
        print(cadena[i+1], cadena[i-1])

        #num = Cal.division(int(cadena[i-1]),int(cadena[i+1]) )
        #cad = cad +" "+ format(num)
        cad = cad +" "+ format(1.0)
  return cad      

        

def modificaExpresion(cadena_div,exp_principal,cadena):
  
  i = 0
  aux = ' '
  nueva_cad = exp_principal
  for j in range(0,len(cadena_div)):
    if(cadena_div[j] =='.'):
      aux = cadena_div[j-1]+'.'+cadena_div[j+1]
      nueva_cad = re.sub(cadena[i],aux,nueva_cad)
      i = i + 1
  
  return nueva_cad



     

   