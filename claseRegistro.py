class Registro:
    __temperatura= ""
    __humedad= ""
    __presionAdmosferica= ""

    def __init__(self,tem,hum,presion):
        self.__temperatura=tem
        self.__humedad=hum
        self.__presionAdmosferica=presion

    def getTemperatura(self):
        return self.__temperatura

    def getHumedad(self):
        return self.__humedad

    def getPresion(self):
        return self.__presionAdmosferica

    def __str__(self):
        return "%s %s %s"% (self.__temperatura,self.__humedad,self.__presionAdmosferica)
