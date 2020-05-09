import re

file = open('Problema3.c', mode='r');

archivo = file.read();

#IDENTIFICADORES
patron_id = '([a-zA-Z]+[a-zA-Z|0-9]|[a-zA-z])';
idlist =  re.findall(patron_id,archivo);
print("Hay: ",str(len(idlist))," Identificadores y son:");
print(idlist);

#NUMEROS ENTEROS
etnlist =  re.findall( "\d+",archivo);
print("Hay: ",str(len(etnlist)),"Numeros Enteros y son: ")
print(etnlist);

#NUMEROS DECIMALES
patrondeci = '(\d+[.]\d+)'
dcilist = re.findall(patrondeci,archivo);
print("Hay: ",len(dcilist),"Numeros Reales y son: ")
print(dcilist);

#OPERADORES
patron_op = '([\sa-z][\>][^\r][^\#][\s0-9]|[|>][0-9]|[0-9\s][\<][^a-z]|&|=|[*]|[+]|%)'
opelist = re.findall(patron_op,archivo);
print("Hay: ",str(len(opelist)),"Operadores y son: ")
print(opelist);