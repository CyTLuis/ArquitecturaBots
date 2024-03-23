# Region -  Importando librerias o clases necesarias
from configparser import ConfigParser
from controller.Impresor import Impresor
# Endregion -  Importando librerias o clases necesarias

console = Impresor()

class Configurations:
    """
        Configurations
        ==============
        Clase encargada de interactuar con el archivo
        de configuración del proyecto, de manera que
        se puedan obtener valores o rutas relacionadas 
        para el funcionamiento del mismo.
        - `Usos:`
            - Obtener la ruta de los archivos de config
            - Obtener los valores de las cadenas de datos
    """
    
    # Constructor de la clase
    def __init__(self):
        self.__config = ConfigParser()
        self.__file = "config.ini"
    
    # Region - Metodos usados en la clase
    
    def getConfigValue(self, section, key):
        """
            Metodo encargado de obtener el valor de un
            elemento de las secciones del `config.ini`
            en caso de ser necesario para complementar la ruta
            se deberá concatenar en las clases o metodos donde
            se hace el llamado de este, no directamente sobre 
            este metodo.
            - `Args:`
                - section (str): Sección del config
                - key (str): Valor a obtener dentro de la sección
            - `Returns:`
                - str: valor obtenido dentro del config
        """
        valor = ""
        try:
            self.__config.read(self.__file)
            valor = self.__config.get(section, key)
        except Exception as e:
            console.imprimirError(f"Error en la obtención de la data para: [{section} - {key}], error: {e}")
        finally:
            return valor

    # Endegion - Metodos usados en la clase
