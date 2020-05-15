import re
import Cal

def priori(exp_principal):
  exp_div = '\d+[/]+\d+'
  exp_mult = '\d+[*]+\d+'
  cadenaTotal = ' '#aqui se guarda toda la operacion

  #1 en prioridad la Division          
  lista = verificaOperador(exp_div,exp_principal)
  if( lista != 0):
    print('Division valida')
    cadena     = converToString(lista)
    cadena_div = Opera(cadena)
    print(cadena_div)
    modificaExpresion(cadena_div,exp_principal,exp_div)

  else:
    print('Divsion Invalida')
  #2 en priorirdad la Multiplicacion
  '''lista = validaOperador(exp_mult,exp_principal)
  if(lista != 0):
     print('Multiplicacion valida')
     print(lista)
  else:
    print('Multiplicacion Invalida') 
    '''



def verificaOperador(ope,exp):
  opelist = re.findall(ope,exp)
  if(len(opelist) > 0 ):
      print("Hay almenos un operador" )
      return opelist
  else: 
      print("No Hay  un operador")
      return 0




def converToString(opelist):
  cadena = ''
  for i in range(0,len(opelist)):
    cadena = cadena+' '+opelist[i]
  return cadena  



def Opera(cadena):
  cad = ' '
  #Si entra a este if, la division se puede hacer y esta validada
  if(cadena != ' '): 
    for i in range(0,len(cadena)):
      if(cadena[i] == '/'):
        num = Cal.division(int(cadena[i-1]),int(cadena[i+1]) )
        cad = cad +" "+ format(num)
  return cad      

        

def modificaExpresion(cadena_div,exp_principal,exp_div):
  #print(exp_div)
  

  for i in range(0,len(cadena_div)):
    if(cadena_div[i] =='.'):
      aux = cadena_div[i-1]+'.'+cadena_div[i+1]
      print(aux)
      nueva_cad = re.sub(exp_div,aux,exp_principal)
    else:
      aux = ' '

  print(nueva_cad)




     

   