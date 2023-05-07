from claseRegistro import Registro
from claseMenu import Menu
from ListaBidimancional import ClaseBid

if __name__ == '__main__':

    unalista=ClaseBid()
    unalista.inicializar()
    bandera = False
    while not bandera:
        print("\nMENU DE OPCIONES")
        print("0 Salir")
        print("1 ITEM 3.1: Mostrar por cada variable el diay la hora de menor y mayor valor")
        print("2 ITEM 3.2: Indicar la temperatura promedio mensula para cada hora")
        print("3 ITEM 3.3: Dado un numero de dia listar los valores para cada hora del dia dado. ")

        opcion = int(input('Ingrese una opcion:'))
        unmenu=Menu()
        unmenu.opcion(opcion,unalista)
        bandera = int(opcion)== 0









    


