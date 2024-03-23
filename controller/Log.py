# ===========================================================================
# Importaciones de clases y librerias necesarias
# ===========================================================================

# Region - Importaciones de librerias y archivos
from datetime import datetime, timedelta
from os import makedirs, path, getcwd, system
from controller.utils.Configurations import Configurations
# Endregion - Importaciones de librerias y archivos

# ===========================================================================
# VARIABLES GLOBALES - LOCAL - INSTANCIA DE OBJETOS O CLASES
# ===========================================================================

# Region - Instancia de clases o declaración de variables
relativePath = getcwd()
config = Configurations()
# Nombre de los archivos de logs de ejecución
nombreArchivoError = f"LogErrores_{(datetime.today() - timedelta(hours = 0)).strftime('%Y-%m-%d')}.txt"
nombreArchivoProceso = f"LogProcesos_{(datetime.today() - timedelta(hours = 0)).strftime('%Y-%m-%d')}.txt"
# Endregion - Instancia de clases o declaración de variables

class Log:
    """
        Log
        ===
            Clase encargada de generar los logs del proceso,
            se entiende por log aquellos archivos de registros
            que se van generando en la ejecución del proceso.
        `Usos:`
            - Escritura de inicio de proceso
            - Escritura de finalización de proceso
            - Escritura de variables dadas en el proceso
            - Escritura de errores dados en el proceso
    """
    def __init__(self):
        """
            Metodo para inicializar la clase, siendo este
            el constructor de la misma, ayuda a validar
            que se tengan las carpetas correspondientes a los logs
        """
        self.__nombreArchivoEror = nombreArchivoError
        self.__nombreArchivoProceso = nombreArchivoProceso
        self.__tiempoActual = ""
        
        rutaCarpetaProcesos = config.getConfigValue("routes", "UbicacionLogProceso")
        rutaCarpetaErrores = config.getConfigValue("routes", "UbicacionLogError")
        
        if not(path.isdir(rutaCarpetaProcesos)):
            # Creación de la carpeta de logs de procesos, en caso de que no existe
            makedirs(rutaCarpetaProcesos)
        if not(path.isdir(rutaCarpetaErrores)):
            # Creación de la carpeta de logs de errores, en caso de que no existe
            makedirs(rutaCarpetaErrores)

        # Asinación de rutas completas para los Logs del bot.
        self.__pathLogProcesos = path.join(relativePath, rutaCarpetaProcesos, self.__nombreArchivoProceso)
        self.__pathLogErrores = path.join(relativePath, rutaCarpetaErrores, self.__nombreArchivoEror)
            
    def gettiempoActual(self):
        return self.__tiempoActual
    
    def settiempoActual(self, tiempoActual):
        self.__tiempoActual = tiempoActual

    # Region - Metodos de escritura de logs
    def registroInicioProcesos(self):
        """
            Metodo que escribirá dentro del log de procesos, el 
            registro de la hora de inicio de ejecución del proceso.
        """
        self.settiempoActual((datetime.today() - timedelta(hours = 0)).strftime('%Y-%m-%d %H:%M:%S'))
        message = "============================================================================================================================\n"
        message+= f"| INICIO DE EJECUCIÓN - {config.getConfigValue("enviroment", "nombreAutomatizacion")} - {str(self.gettiempoActual())} |\n"
        message+= "============================================================================================================================\n"
        file = open(self.__pathLogProcesos, "a")
        file.write(message + "\n") 
        file.close()
    
    def registroFinalProcesos(self):
        """
            Metodo que escribirá dentro del log de procesos, el 
            registro de la hora en que se finalizo el proceso
            y su estado final: Exitoso o Fallido.
        """
        self.settiempoActual((datetime.today() - timedelta(hours = 0)).strftime('%Y-%m-%d %H:%M:%S'))
        log = "============================================================================================================================\n"
        log+= f"| FINAL DE EJECUCIÓN - {config.getConfigValue("enviroment", "nombreAutomatizacion")} - {str(self.gettiempoActual())} |\n"
        log+= "============================================================================================================================\n"
        file = open(self.__pathLogProcesos, "a")
        file.write(log + "\n") 
        file.close()
        
    def registrarLogProceso(self, nameProcess):
        """
            Metodo que escribirá dentro del log de procesos, el 
            nombre del proceso que se esta ejecutando.
            - `Args:`
                - nameProcess (str): Nombre del proceso en ejecución
        """
        self.settiempoActual((datetime.today() - timedelta(hours = 0)).strftime('%Y-%m-%d %H:%M:%S'))
        Messagelog = f"| Ejecutando la tarea == ['{nameProcess}'] <--> Hora de ejecución: {str(self.gettiempoActual())}"
        file = open(self.__pathLogProcesos,"a")
        file.write(Messagelog + "\n") 
        file.close()
    
    def registroSubtitulo(self, messageTitle):
        """
            Metodo que escribirá dentro del log de procesos, 
            un titulo referente a la ejecución del proceso, puede
            servir como flag o checkpoint del proceso. 
            - `Args:`
                - messageTitle (str): Titulo a registrar dentro del log
        """
        self.settiempoActual((datetime.today() - timedelta(hours = 0)).strftime('%Y-%m-%d %H:%M:%S'))
        log = "============================================================================================================================\n"
        log+= f"| {messageTitle}  - {str(self.gettiempoActual())} |\n"
        log+= "============================================================================================================================\n"
        file = open(self.__pathLogProcesos, "a")
        file.write(log + "\n") 
        file.close()
    
    def registrarComentario(self, titulo: str, comentario: str):
        """
            Metodo que escribirá dentro del log de procesos, 
            escribe el comentario relacionado al proceso, toma
            un titulo como nivel de información, y el comentario
            como mensaje descriptivo.
            - `Args:`
                - titulo: str (str): Nivel de información (Info, Error, etc)
                - comentario (str): Mensaje a escribir dentro del log
        """
        self.settiempoActual((datetime.today() - timedelta(hours = 0)).strftime('%Y-%m-%d %H:%M:%S'))
        log = "============================================================================================================================\n"
        log+= f"| {titulo} |: {comentario} - {str(self.gettiempoActual())} \n"
        log+= "============================================================================================================================\n"
        file = open(self.__pathLogProcesos, "a")
        file.write(log + "\n") 
        file.close()
        
    # Metodo para hacer una division en un log
    def registroSeparador(self):
        log = "============================================================================================================================"
        file = open(self.__pathLogProcesos, "a")
        file.write(log + "\n") 
        file.close()
    
    def registrarLogEror(self, error, procesoActual):
        """
            Metodo que escribirá dentro del log de errores, 
            el error que se genero y se dio manejo en el proceso,
            a la par que el nombre del proceso o metodo que genero
            el error
            - `Args:`
                - error (str): Error generado
                - procesoActual (str): Proceso o metodo del error
        """
        self.settiempoActual((datetime.today() - timedelta(hours = 0)).strftime('%Y-%m-%d %H:%M:%S'))
        log = "============================================================================================================================\n"
        log+= f"| Se ha encontrado un error || Hora detectada: {str(self.gettiempoActual())} |\n"
        log+= f"| Ultimo estado (Tarea) --> {procesoActual} |\n"
        log+= f"| ERROR: --> {str(error)} |\n"
        log+= "============================================================================================================================\n"
        file = open(self.__pathLogErrores, "a")
        file.write(log + "\n") 
        file.close()
        
    # Endregion - Metodos de escritura de logs
    