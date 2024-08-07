#imports
from tabulate import tabulate

#funciones
def mostarmenu():
    print('''
    1. Registrar pedido
    2. Listar todos los pedidos
    3. Imprimir hoja de ruta
    4. Salir del programa
    ''')

def opcion1():
    #Por ahora me aseguro solo si ingresó algo para validar, si no ingresó nada, hago que ingrese todo de nuevo. Finalmente guardo los datos en una lista
    while True:
        nombre = input("Nombre y apellido: ")
        if len(nombre) == 0:
            print("No ingresaste nada")
            continue
        direccion = input("Dirección: ")
        if len(direccion) == 0:
            print("No ingresaste nada")
            continue
        comuna = input("Comuna: ")
        if len(comuna) == 0:
            print("No ingresaste nada")
            continue
        try :
            cil5 = int(input("Cantidad cilindros de 5 kg: "))
        except ValueError:
            print("No ingresaste un número")
            continue
        try:
            cil15 = int(input("Cantidad cilindros de 15 kg: "))
        except ValueError:
            print("No ingresaste un número")
            continue
        try:
            cil45 = int(input("Cantidad cilindros de 45 kg: "))
        except ValueError:
            print("No ingresaste un número")
            continue
        linea = [nombre, direccion, comuna, cil5, cil15, cil45]
        datos.append(linea)
        print("Pedido ingresado con exito!")
        print()
        break

def opcion2():
    print(tabulate(datos, headers=['Nombre', 'Dirección', 'Sector', 'Cil. 5kg', 'Cil. 15kg', 'Cil. 45kg']))

def opcion3(txt):
    #Valido que la variable txt, que será el sector, sea igual al sector de algun pedido y lo guardo en imprimir
    imprimir = []
    for i in datos:
        if i[2].upper() == txt.upper():
            imprimir.append(i)
    #si no tiene nada imprimir, no se creará ningun archivo
    if len(imprimir) == 0:
        print("No se han ingresado pedidos con el sector correspondiente")
    else:
        with open('ruta' + sector + '.txt', 'w', encoding='utf-8') as file:
            file.write(tabulate(imprimir, headers=['Nombre', 'Dirección', 'Sector', 'Cil. 5kg', 'Cil. 15kg', 'Cil. 45kg']))
            print("Hoja de ruta imprimida")
            imprimir = []

#codigo principal
datos = []
sectores = ['Concón', 'Reñaca', 'Forestal', 'Caleta Higuerillas', 'Manzanar']
while True:
    mostarmenu()
    op = input("Eliga una opción: ")
    print()
    if op == "4":
        print("Hasta luego")
        print()
        break
    elif op == "1":
        opcion1()
    elif op == "2":
        if len(datos) == 0:
            print("No se han ingresado pedidos")
        else:
            opcion2()
    elif op == '3':
        for i in sectores:
            print(i)
        print()
        sector = input('Indique el sector para imprimir: ')
        opcion3(sector)
    else:
        print("Ingrese una opción válida(1/2/3/4)")