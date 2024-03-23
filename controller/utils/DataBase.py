# Region - Importación de librerias o archivos necesarios
from os import getcwd
from pyodbc import connect

from controller.Log import Log
from controller.utils.Helpers import Helpers
from controller.utils.Configurations import Configurations
# Endregion - Importación de librerias o archivos necesarios

# Region - Instancia de clases o elementos usados
logger = Log()
helper = Helpers()
configurations = Configurations()
keyFrt: str = "iBqlFRACiHatsCuRXJ9F-7euK73h5VLcnlTPtupd-G0="
# Obtención del path absoluta del proyecto
relativePath = getcwd()
# Endregion - Instancia de clases o elementos usados

class DataBaseRPA:
    """
    DataBaseRPA
    ===========
    Clase para manejar la base de datos que se
    involucren en el proyecto, teniendo como
    motor principal de base de datos a PgSQL.
    ### Metodos disponibles para inserción:  
        - `crearConexion()`: Apertura de conexión a Base de Datos de PgSQL
        - `cerrarConexion()`: Cierre de conexión a Base de Datos de PgSQL
    """
     
    def __init__(self):
        """ 
            Inicializamos los datos de conexión y demás variables
            utilizadas dentro de los metodos de consulta o inserción.
            ### `Variables`:
                - datosCrypto: (dict) = Datos de conexión a la base de datos, ya desencryptadas
            ## Nota:
                - Los datos vendrán encryptados desde el config, y se utilizará un metodo de la 
                clase Helper para obtener el valor, y luego desencryptar la información.
        """
        self.datosCrypto = {}
        self.datosCrypto.update({'server': helper.desEncriptarData(keyFrt, bytes(configurations.getConfigValue("datosconexion", "server"), 'utf-8'))})
        self.datosCrypto.update({'bdName': helper.desEncriptarData(keyFrt, bytes(configurations.getConfigValue("datosconexion", "bdName"), 'utf-8'))})
        self.datosCrypto.update({'username': helper.desEncriptarData(keyFrt, bytes(configurations.getConfigValue("datosconexion", "username"), 'utf-8'))})
        self.datosCrypto.update({'password': helper.desEncriptarData(keyFrt, bytes(configurations.getConfigValue("datosconexion", "password"), 'utf-8'))})
        self.__conn = ""
    
    def crearConexion(self):
        """
        Este metodo se encargará de gestionar la
        conexión a la base de datos de PgSQL, retornando
        la instancia de conexión para ser usada en otros lugares.
        """
        try:
            self.__conn = connect(
                    database = self.datosCrypto["bdName"], 
                    user = self.datosCrypto["username"], 
                    host= self.datosCrypto["server"],
                    password = self.datosCrypto["password"],
                    port = 5432
                )
        except Exception as e:
            logger.registrarLogEror(f"Ha ocurrido un error generando la conexión a base de datos, error: {e}", "crearConexion")
            self.__conn = ""
    
    def cerrarConexion(self):
        """
        Cada que se use la conexión a base de datos nueva,
        se deberá cerrar la misma para evitar procesos abiertos.
        """
        try:
            if(self.__conn != ""):
                self.__conn.close()
        except Exception as e:
            logger.registrarLogEror(f"Ha ocurrido un error cerrando la conexión a base de datos, error: {e}", "cerrarConexion")
            self.__conn = ""
        