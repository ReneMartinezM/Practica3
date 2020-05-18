import re
import Cal


def priori(exp_principal):
    exp_div = '(\d*.\d*[/]\d*.\d*)'
    exp_mult = '(\d*.\d*[\*]d*.\d*)'
    exp_suma = '(\d*.\d*\+\d*.\d*)'
    exp_resta = '(\d*.\d*\-\d*.\d*)'
    cadenaTotal = ' '  #aqui se guarda toda la operacion
    cadenaTotal1 = ' '  #aqui se guarda toda la operacion
    cadenaTotal2 = ' '  #aqui se guarda toda la operacion
    cadenaTotal3 = ' '  #aqui se guarda toda la operacion

    #1 en prioridad la Division
    lista = verificaOperador(exp_div, exp_principal)
    if (lista != 0):
        print('Division valida')
        cadena = converToString(lista)
        if (validaDivision(cadena) == 1):
            cad_libre = liberaSeparaExpresion(cadena, '\/')
            cadena_result = realizaDivision(cad_libre)
            cadenaTotal = modificaExpresion(exp_div, cadena_result,
                                            exp_principal)
            print("Despues de resolver las divisiones, la expresion es asi")
            print(cadenaTotal)
        else:
            print("Division entre cero invalida")
    else:
        print('No hay divisiones')
#2 en priorirdad la Multiplicacion
    aux = cadenaTotal
    lista = verificaOperador(exp_mult, aux)
    if (lista != 0):
        print('Multiplicacion valida')
        cadena = converToString(lista)
        cad_libre = liberaSeparaExpresion(cadena, '\*')
        cadena_result = realizaMultiplicacion(cad_libre)
        cadenaTotal = modificaExpresion(exp_mult, cadena_result, aux)

    else:
        print('No hay Multiplicaciones')
#3 en priorirdad la Suma

    aux = cadenaTotal
    lista = verificaOperador(exp_suma, aux)
    if (lista != 0):
        print('Suma valida')
        cadena = converToString(lista)
        cad_libre = liberaSeparaExpresion(cadena, '\+')
        cadena_result = realizaSuma(cad_libre)
        cadenaTotal = modificaExpresion(exp_mult, cadena_result, aux)
        print(cadenaTotal2)
    else:
        print('No hay sumas')


#4 en priorirdad la Resta

    aux = cadenaTotal
    lista = verificaOperador(exp_resta, aux)
    print("Lista", lista)
    if (lista != 0):
        print('Resta valida')
        cadena = converToString(lista)
        cad_libre = liberaSeparaExpresion(cadena, '\-')
        print("Cadena Separada dentro del Resta", cadena)
        #cadena_result    = realizaResta(cad_libre)
        #cadenaTotal     =  modificaExpresion(exp_mult,cadena_result,aux)
        #print(cadenaTotal)
    else:
        print('No hay restas')


def verificaOperador(ope, exp):
    opelist = re.findall(ope, exp)
    if (len(opelist) > 0):
        print("Hay almenos un operador")
        return opelist
    else:
        print("No Hay  un operador")
        return 0


def converToString(opelist):
    cadena = ' '
    for i in range(0, len(opelist)):
        cadena = cadena + ' ' + opelist[i]
    return cadena


def validaDivision(cadena):
    exp1 = '/(0$|0\s|0\-|0\*|0\+|0.0)'
    lista = re.findall(exp1, cadena)

    if (len(lista) > 0):
        return 0
    else:
        return 1


def liberaSeparaExpresion(exp, operador):
    #Separo la expresion cada vez que haya una division
    lista = re.split(operador, exp)
    print("Lista Separada", lista)
    #La lista la paso a string y separo la cadena cada vez que hay espacios

    cadena = converToString(lista)
    nombreLista = re.split(" ", cadena)

    #Quito los Espacios de la lista que salio, para que no haya espacios
    nombreLista = [i for i in nombreLista if i]
    #tenemos la lista separada

    return nombreLista


def realizaDivision(lista):

    #Este for es para hacer la operacion de la division
    cad = " "
    for i in range(0, len(lista)):
        if (i % 2 == 0):
            if (i < len(lista)):
                num = Cal.division(float(lista[i]), float(lista[i + 1]))
                cad = cad + " " + format(num)

    return cad


def realizaMultiplicacion(lista):

    #Este for es para hacer la operacion de la multiplicacion
    cad = " "
    for i in range(0, len(lista)):
        if (i % 2 == 0):
            if (i < len(lista)):
                num = Cal.multiplicacion(float(lista[i]), float(lista[i + 1]))
                cad = cad + " " + str(num)
    return cad


def realizaSuma(lista):
    #Este for es para hacer la operacion de la multiplicacion
    cad = " "
    for i in range(0, len(lista)):
        if (i % 2 == 0):
            if (i < len(lista)):
                num = Cal.suma(float(lista[i]), float(lista[i + 1]))
                cad = cad + " " + str(num)
    return cad


def realizaResta(lista):
    #Este for es para hacer la operacion de la multiplicacion
    cad = " "
    print(list)
    for i in range(0, len(lista)):
        if (i % 2 == 0):
            if (i < len(lista)):
                num = Cal.resta(float(lista[i]), float(lista[i + 1]))
                cad = cad + " " + str(num)
    return cad


def modificaExpresion(exp_mult, cad_result, exp_principal):
    nueva_cad = exp_principal
    lista_cad_result = cad_result.split()
    for i in range(0, len(lista_cad_result)):
        if (i < len(lista_cad_result)):
            nueva_cad = re.sub(exp_mult, lista_cad_result[i], nueva_cad)
    nueva_cad = sentence = re.sub(r"\s+", "", nueva_cad, flags=re.UNICODE)
    return nueva_cad
