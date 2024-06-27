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
