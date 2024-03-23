# ===========================================================================
# Importaciones de clases y librerias necesarias
# ===========================================================================

# region - Importaciones de librerias o clases
from datetime import datetime,timedelta
# endregion - Importaciones de librerias o clases

class Impresor:
    """
        Impresor
        ========
        Esta clase se encargará de imprimir mensajes en consola
        para el seguimiento del aplicativo, en la etapa de desarrollo.
        ### `Usos:`
        - Depurar a través de print el código
        - Imprimir variables necesarias para el desarrollo
    """
    def __init__(self):
        """
            Constructor de la clase `Impresor`, donde se inicializan
            las variables de la clase.
        """
        self.__tiempoActual = ""
    
    def gettiempoActual(self):
        return self.__tiempoActual
    
    def settiempoActual(self, tiempoActual):
        self.__tiempoActual = tiempoActual
        
    # Region - Metodos en la clase
    
    def imprimirInicio(self, nombreApp):
        """
            Metodo encargado de imprimir en consola el
            inicio de la ejecución del proyecto
        Args:
            nombreApp (str): Nombre del proyecto o de la aplicación
        """
        self.settiempoActual((datetime.today() - timedelta(hours = 0)).strftime('%Y-%m-%d %H:%M:%S'))
        data = "============================================================================================================================\n"
        data+= "| INICIO DE APLICACION --> ["+ str(nombreApp) +"] Hora de ejecucion: " + str(self.gettiempoActual()) + " |\n"
        data+= "============================================================================================================================\n"
        print(data)
    
    def imprimirProceso(self, proceso):
        """
            Metodo usado para imprimir la tarea o función
            que se esta ejecutando en el proceso.
        Args:
            proceso (str): Nombre de la función
        """
        self.settiempoActual((datetime.today() - timedelta(hours = 0)).strftime('%Y-%m-%d %H:%M:%S'))
        data = "============================================================================================================================\n"
        data+= "| Ejecutando la tarea --> ["+ str(proceso) +"]\n"
        data+= "| Hora de ejecucion: " + str(self.gettiempoActual()) +"\n"
        data+= "============================================================================================================================\n"
        print(data)
    
    def imprimirComentario(self, proceso: str, comentario: str):
        """
            Metodo usado para imprimir la tarea o función
            que se esta ejecutando en el proceso.
        `Args:`
            `proceso (str):` Nombre de la función del llamado
            `comentario (str):` Comentario que se desea imprimir
        """
        self.settiempoActual((datetime.today()).strftime('%Y-%m-%d %H:%M:%S'))
        data = "|==========================================================================================================================|\n"
        data+= f"| Tarea: [{proceso}] <==> {comentario}|\n"
        data+= f"| Hora de ejecución: ({self.gettiempoActual()}) |\n"
        data+= "|==========================================================================================================================|\n"
        print(data)
    
    def imprimirFinal(self):
        """
            Metodo usado para imprimir la hora
            en la que se termino de ejecutar el proceso
        """
        self.settiempoActual((datetime.today() - timedelta(hours = 0)).strftime('%Y-%m-%d %H:%M:%S'))
        data = "============================================================================================================================\n"
        data+= "| FINALIZACION DE APLICACION | Hora de ejecucion: " + str(self.gettiempoActual()) + "\n"
        data+= "============================================================================================================================\n"
        print(data)
    
    def imprimirError(self, error):
        """
            Metodo para imprimir un posible error identificado
            durante la ejecución del proceso
        Args:
            error (str): Variable contenedora del error.
        """
        self.settiempoActual((datetime.today() - timedelta(hours = 0)).strftime('%Y-%m-%d %H:%M:%S'))
        data = "============================================================================================================================\n"
        data += "| Error en ejecución| Hora del error: " + str(self.gettiempoActual()) + "\n"
        data += "| ERROR: " + error +"\n"
        data += "============================================================================================================================\n"
        print(data)
        
    # Endregion - Metodos en la clase  
             