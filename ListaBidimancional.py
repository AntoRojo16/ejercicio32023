import csv
from claseRegistro import Registro
class ClaseBid:

    def __init__(self):
        self.__matriz=[]
        for i in range(2):
            lista=[]
            for j in range(2):
                 lista.append(0)
            self.__matriz.append(lista)


    def mostar(self):
        for i in range(2):
            for j in range(2):
                print(self.__matriz[i][j])

    def agregarRegistro(self,in1,in2,registor):
        self.__matriz[int(in1)][int(in2)-1]=registor



    def inicializar(self):
        archivo=open("Registro.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True

        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                dia=fila[0]
                hora=fila[1]
                temperatura=fila[2]
                humedad=fila[3]
                presion=fila[4]
                unRegistro=Registro(temperatura,humedad,presion)
                self.agregarRegistro(hora,dia,unRegistro)
        archivo.close()

    def mostrarMayorTemperatura(self):
        mayorT=0

        Dia=0
        Hora=0
        for i in range(2):
            for j in range(2):
                if int(self.__matriz[i][j].getTemperatura())>int(mayorT):
                    mayorT=self.__matriz[i][j].getTemperatura()
                    Dia=j
                    Hora=i
        print("La temperatura maxima es {} en el dia {} en la hora {}".format(mayorT,int(Dia+1),Hora))

    def mostrarMenorTemperatura(self):
        menorT=1000

        Dia=0
        Hora=0
        for i in range(2):
            for j in range(2):
                if int(self.__matriz[i][j].getTemperatura())<int(menorT):
                    menorT=self.__matriz[i][j].getTemperatura()
                    Dia=j
                    Hora=i
        print("La temperatura minima es {} en el dia {} en la hora {}".format(menorT,int(Dia+1),Hora))


    def mostarMayorPresion(self):
        mayorP=0
        Dia=0
        Hora=0

        for i in range(2):
            for j in range(2):
                if int(self.__matriz[i][j].getPresion())>int(mayorP):
                    mayorP=self.__matriz[i][j].getPresion()
                    Dia=j
                    Hora=i
        print("La presion maxima es {} en el dia {} en la hora {}".format(mayorP,int(Dia+1),Hora))

    def mostarMenorPresion(self):
        menorP=1000
        Dia=0
        Hora=0

        for i in range(2):
            for j in range(2):
                if int(self.__matriz[i][j].getPresion())<int(menorP):
                    menorP=self.__matriz[i][j].getPresion()
                    Dia=j
                    Hora=i
        print("La presion minima es {} en el dia {} en la hora {}".format(menorP,int(Dia+1),Hora))



    def mostarMayorHumedad(self):
        mayorH=0
        Dia=0
        Hora=0

        for i in range(2):
            for j in range(2):
                if int(self.__matriz[i][j].getHumedad())>int(mayorH):
                    mayorH=self.__matriz[i][j].getHumedad()
                    Dia=j
                    Hora=i
        print("La humedad maxima es {} en el dia {} en la hora {}".format(mayorH,int(Dia+1),Hora))

    def mostarMenosHumedad(self):
        menorH=1000
        Dia=0
        Hora=0

        for i in range(2):
            for j in range(2):
                if int(self.__matriz[i][j].getHumedad())<int(menorH):
                    menorH=self.__matriz[i][j].getHumedad()
                    Dia=j
                    Hora=i
        print("La humedad minima es {} en el dia {} en la hora {}".format(menorH,int(Dia+1),Hora))

    def promedioPorHora(self):
        for i in range(2):
            cont=0
            for j in range(2):
                cont+=int(self.__matriz[i][j].getTemperatura())
            print("La temperatura promedio mensual de la hora {} es: {}".format(i,(cont/int(2))))

    def  listarValores(self):
        dia=input("Ingrese el dia")
        t="Temperatura"
        H="Hora"
        P="Presion"
        h="Humedad"
        print("{:>0} {:>24}{:>24} {:>24}".format(H,t,P,h))
        for i in range(2):
            print("{:>0} {:>24}{:>24} {:>24}".format(i,self.__matriz[i][int(dia)-1].getTemperatura(),self.__matriz[i][int(dia)-1].getPresion(),self.__matriz[i][int(dia)-1].getHumedad()))











