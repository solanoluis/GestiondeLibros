import os
import csv
import operator
import sys
import time

salida = False

#********************************************************************************************************************
#FUNCION QUE DIBUJA EL MENU Y LLAMA A LA FUNCION QUE VALIDA QUE LA OPCION DEL MENU SEA CORRECTA
def dibujaMenu():
    os.system('cls')
    print("***************************************")
    print("Gestión y Control de Préstamo de Libros")
    print("***************************************")
    print("")
    print("a - Ver lista de personas")
    print("b - Ordenar lista de personas")
    print("c - Imprimir registro de lista de persona")
    print("d - Ver lista de libros")
    print("e - Buscar libro")
    print("f - Prestar libro")
    print("g - Devolver libro")
    print("h - Ver libros prestados")
    print("i - Salir")
    print("")

#********************************************************************************************************************
#MUESTRA LISTA DE PERSONAS
#OPCION A DEL MENU
def muestraPersonas():
    with open ("personas.csv", "r") as csv_personas:
        csv_reader = csv.DictReader(csv_personas)

        for line in csv_reader:
            print("Indice: ",line["Indice"])
            print("Cedula: ",line["Identificación"])
            print("Nombre: ", line["Nombre"], " ",  end="")
            print(line["Primer Apellido"], " ", end="")
            print(line["Segundo Apellido"],)
            print("E-mail: ", line["Correo Electrónico"])
            print("")
    input("Presione un ENTER para continuar...")

#********************************************************************************************************************
#ORDENA LA LISTA DE PERSONAS POR PRIMER APELLIDO
#OPCION B DEL MENU
def ordenLista():
    print("1. Ordenar la lista por Cedula")
    print("2. Ordenar la lista por Nombre")
    print("3. Ordenar la lista por Primer Apellido")
    print("4. Ordenar la lista por segundo Apellido")
    print("5. Ordenar la lista por correo electronico")

    op = int(input())
    print("")

    sample = open("personas.csv", "r")
    csv1 = csv.reader(sample)
    next(csv1, None)
    sort = sorted(csv1,key=operator.itemgetter(op)) 
    for eachline in sort:
        print(eachline[1], " ", eachline[2], " ", eachline[3], " ",eachline[4], " ", eachline[5])

    input("Presione un ENTER para continuar...")

#********************************************************************************************************************
#IMPRIME REGISTRO DE LISTA DE PERSONAS
#OPCION C DEL MENU
def imprimePersona():
    csv_file = csv.reader(open('personas.csv', "r"))

    row_count = sum(1 for row in csv_file)
    print("Exiten ", row_count-1, "registros guardados.")

    op = input("Digite el numero de registro que desea ver: ")

    csv_file = csv.reader(open('personas.csv', "r"))

    for row in csv_file:
        if op == row[0]:
            print("")
            print("**********************************")
            print ("Cedula: ", row[1])
            print ("Nombre: ", row[2])
            print ("Primer Apellido: ", row[3])
            print ("Segundo Apellido: ", row[4])
            print("**********************************")

    input("Presione un ENTER para continuar...")

#********************************************************************************************************************
#IMPRIME REGISTRO DE LISTA DE LIBROS
#OPCION D DEL MENU
def imprimeLibros():
    with open ("libros.csv", "r") as csv_personas:
        csv_reader = csv.DictReader(csv_personas)

        for line in csv_reader:
            #print(line["idLibro"], " - ", "Genero: ", line["Genero"])
            print(line["idLibro"], "|","Titulo: ", line["nombre"], "| ",  end="")
            print("Autor: ", line["Autor"],)
            print("")

    input("Presione un ENTER para continuar...")

#********************************************************************************************************************
#FUNCION QUE BUSCA UN LIBRO
#OPCION E DEL MENU
def buscaLibro():
    with open ("libros.csv", "r") as csv_personas:
        csv_reader = csv.DictReader(csv_personas)

        for line in csv_reader:
            print("Identificador del libro: ",line["idLibro"])
            print("Titulo: ", line["nombre"], " ")
            print("")

    number = input("Digite el indice del libro a mostrar: ")

    csv_file = csv.reader(open('libros.csv', "r"))

    for row in csv_file:
        if number == row[0]:
            print("")
            print("**********************************")
            print ("Titulo: ", row[1])
            print ("Genero: ", row[2])
            print ("Autor: ", row[3])
            print ("Estatus del libro: ", row[4])
            print("**********************************")

    input("Presione un ENTER para continuar...")

#********************************************************************************************************************
#FUNCION PARA MOSTRAR LIBROS DISPONIBLE Y PRESTAR UNO
#OPCION F DEL MENU
def prestaLibro():
    csv_file = csv.reader(open('libros.csv', "r"))

    print("Libros disponibles")

    for row in csv_file:

        if row[4] == "Disponible":
            print ("Identificador: ", row[0])
            print ("Titulo: ", row[1])
            print ("Genero: ", row[2])
            print ("Autor: ", row[3])
            print ("Estatus del libro: ", row[4])
            print("**********************************")
    
    opLibro = int(input("Digite el identificador del libro que desea: "))

    r = csv.reader(open('libros.csv', "r"))
    lines = list(r)

    lines[opLibro][4] = "No Disponible"

    writer = csv.writer(open('libros.csv', 'w', newline='\n'))
    writer.writerows(lines)
    
    print("Se le ha prestado este libro!")
    print("")
    input("Presione un ENTER para continuar...")

#********************************************************************************************************************
#FUNCION PARA DEVOLVER LIBROS
#OPCION G DEL MENU
def devuelveLibro():
    csv_file = csv.reader(open('libros.csv', "r"))

    print("Libros disponibles")

    for row in csv_file:

        if row[4] == "No Disponible":
            print ("Identificador: ", row[0])
            print ("Titulo: ", row[1])
            print ("Genero: ", row[2])
            print ("Autor: ", row[3])
            print("**********************************")
    
    opLibro = int(input("Digite el identificador del libro que desea: "))

    r = csv.reader(open('libros.csv', "r"))
    lines = list(r)

    lines[opLibro][4] = "Disponible"

    writer = csv.writer(open('libros.csv', 'w', newline='\n'))
    writer.writerows(lines)

    print("Su libro ha sido devuelto!")
    print("")
    input("Presione un ENTER para continuar...")

#********************************************************************************************************************
#MUESTRA LIBROS PRESTADOS
#OPCION H DEL MENU
def librosPrest():
    print("")
    print("Libros prestados")
    print("")

    csv_file = csv.reader(open('libros.csv', "r"))    
    for row in csv_file:

        if row[4] == "No Disponible":
            print ("Titulo: ", row[1])
            print ("Genero: ", row[2])
            print ("Autor: ", row[3])
            print("**********************************")

    input("Presione un ENTER para continuar...")

#********************************************************************************************************************
#VALIDA OPCION DE MENU
list_resp = ["a","b","c","d","e","f","g","h","i"]

#********************************************************************************************************************
#ELIGE FUNCION SEGUN VARIABLE OP, SI SE ELIGIO UNA OPCION INCORRECTA VUELVE A MOSTRAR EL MENU
def opMenu(op):
    if op in list_resp:
        if op == "a":
            muestraPersonas()
        if op == "b":
            ordenLista()
        if op == "c":
            imprimePersona()
        if op == "d":
            imprimeLibros()
        if op == "e":
            buscaLibro()
        if op == "f":
            prestaLibro()
        if op == "g":
            devuelveLibro()
        if op == "h":
            librosPrest()
    else:
        print("Opción invalida!")
        time.sleep(1)

#********************************************************************************************************************
#INICIO
while (salida == False):
    dibujaMenu()
    op = input("Por favor seleccione una opcion: ")
    if op == "i":
        print("Lo esperamos pronto!")
        time.sleep(1)
        salida = True
    else:
        opMenu(op)




