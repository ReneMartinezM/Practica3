import re
def opera(exp):
  op_division = '\d+[/]+\d+'
  #patron_decimales = '\d+[*]+\d+'#ENCUENTRA OPERADOR 
  
 # patron_enteros   = '^(\d+|\d+[.]\d+)[+]^(\d+|\d+[.]\d+)'
  
  opelist = re.findall(op_division,exp)#saco los 
  print(opelist)
 # op1 = re.split(exp,'*')
  #print(op1)
  
  #print(exp.split(patron_decimales))
  
def proximoOperador(exp):
  op_division = '\d+[*]+\d+'

    opelist = re.findall(op_division,exp)#saco los 
  print(opelist)
  if()