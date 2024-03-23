# region - Importaciones de clases y librerias
from os import getcwd
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from controller.utils.Configurations import Configurations

from controller.Log import Log
# endregion - Importaciones de clases y librerias

# region - Inicialización de clases o variables globales
log = Log()
configurations = Configurations()
# endregion - Inicialización de clases o variables globales

class Selenium:
    """
        Selenium
        ========
        Esta clase se encargará unicamente de crear el 
        llamado del GeckoDriver, encargado de la gestión
        del bot en las automatizaciones web.
        ### Aspectos a considerar:
        - Esta clase solo retorna el `driver`, no los metodos de Selenium.
        - Para usar metodos de Selenium, se instancia en la clase que lo llame.
        ### Nota:
        - En desarrollos completamente nuevos, se deberá descomprimir el GeckoDriver
        que se encuentra en la ruta `plugins\gecko`
    """
    def __init__(self):
        """
            Se inicializa los atributos de la clase Robot
            para la plantilla, se deja inicializado el driver en el metodo init
            pero se puede inicializar y modificar a medida del requerimiento
            - Usaremos selenium con `Firefox` usando el GeckoDriver
                para la automatización web
            - Usaremos el argumento `"--disable-blink-features=AutomationControlled"`
                para prevenir la detección del bot como automatización
        """ 
        self.opcionesDriver = Options() # Se inicializan las opciones del driver para Firefox
        self.opcionesDriver.add_argument('--disable-blink-features = AutomationControlled')
        self.servicePath = Service(getcwd() + configurations.getConfigValue("drivers", "GeckoDriver")) # Se inicializa el servicio en la ruta del GeckoDriver        

    # Region - Metodos usados para la automatización con Selenium
    
    def retornarDriver(self):
        """
            Metodo encargado de inicializar el GeckoDriver para 
            el uso de selenium en la automatización web
            ## `Uso`
            - Retornará la instancia del driver, para que al ser llamado
            desde otro archivo, pueda usarse la interacción web a través
            de Firefox.
            ## `Nota`
            - En caso de necesitar otro metodo de la clase Selenium, se deberá
            importar dentro del archivo que llamo el Driver, y no en este archivo.
        """
        try:
            driver = webdriver.Firefox(service = self.servicePath, options = self.opcionesDriver)                       
            return driver
        except Exception as e:
            log.registrarLogEror(f"Inicialización del GeckoDriver, error: {e}", "retornarDriver")
            return None
        
    # Endregion - Metodos usados para la automatización con Selenium
    