import re
def validaLetras(exp):
  val = 0
  patron2 = '[a-zA-Z]'##Esto dice que encontro almenos una letra
  
  opelist = re.findall(patron2,exp);
  #print(opelist)

  if(len(opelist)>0):
     val = 1
  return val
  
