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
    cadena = converToString(lista)
    print(Opera(cadena))

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

        

        
     

   