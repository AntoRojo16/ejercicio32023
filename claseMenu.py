from ListaBidimancional import ClaseBid

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            0:self.salir
                          }
    def opcion(self,op,lista):
        print(op)
        func=self.__switcher.get(op,lambda: print("Opción no válida"))
        func(lista)

    def salir(self,lista):
        print('Usted salio del programa')
    def opcion1(self,lista):
        lista.mostrarMayorTemperatura()
        lista.mostarMayorPresion()
        lista.mostarMayorHumedad()
        lista.mostarMenorPresion()
        lista.mostarMenosHumedad()
        lista.mostrarMenorTemperatura()


    def opcion2(self,lista):
        lista.promedioPorHora()

    def opcion3(self,lista):
        lista.listarValores()

        
