# region Importando librerias o clases necesarias
from pathlib import Path
import os, glob, shutil, zipfile
from cryptography.fernet import Fernet
# endregion Importando librerias o clases necesarias

# Region - Instanciar Objetos y variables Globales
# Obtención del path absoluta del proyecto
relativePath = os.getcwd()
# Obtención del user name de la maquina de ejecución
usuarioMaquinaActual = os.getlogin()
# Endregion - Instanciar Objetos y variables Globales

class Helpers:
    """
        Helpers
        ======= 
        La clase se encargará de entregar distintos metodos,
        cada uno encargado de retornar un valor, modificar un elemento,
        obtener una ruta, o todas aquellas utilidades que puedan ser usadas
        en cualquier lugar necesario dentro de la aplicación
        ## Usos
        - Contar los registros de un DataFrame
        - Contar las carpetas de un directorio.
        - Generar interacciones con Tkinter en la GUI.
        - Entre otros, los cuales podrán ser agregados a medida del desarrollo
    """
    
    # Constructor de la clase
    def __init__(self):
        self.__initial_count = 0
    
    # Region Metodos usados en la clases
    
    def countRecordsDataframe(self, registrosContar):
        """
            Metodo para contar la cantidad de registros
            dentro de un DataFrame, devolviendo así solo
            los registros de filas con información.
        - `Args:`
            - registrosContar (Pandas DF): DataFrame con la información a contar
        - `Returns:`
            - str: Cantidad de registros del dataframe
        """
        aloneRows = registrosContar.split(",")
        total = str(aloneRows[0]).replace("(", "")
        return total
    
    # Cuenta el total de carpetas dentro de un directorio
    def countFolder(self, ruta):
        """
            Toma un directorio de un path completo, retorna la cantidad
            total de directorios encontrados dentro de la ruta dada.
            - `Args:`
                - ruta (str): Ruta del directorio raíz
            - `Returns:`
                total (int): Cantidad de subdirectorios
        """
        self.__initial_count = 0
        for path in Path(ruta).iterdir():
            if path.is_dir():
                self.__initial_count += 1
                
        return self.__initial_count
    
    def countFilesExtension(self, path, extension):
        """
            Este metodo contará los archivos dentro de una carpeta
            dada, y devolverá la cantidad de archivos que tienen 
            la extesión recibida al metodo.
        - `Args:`
            - path (str): Ruta base para los archivos
            - extension (str): Tipo de archivos por extensión a contar
        - `Returns:`
            - int: Número entero de la cantidad de archivos encontrados
        """
        cantidadArchivos = len(glob.glob1(path, f"{extension}"))
        return cantidadArchivos

    def encriptarData(self, key: str, valor: str):
        """
            Se encrypta un dato dado, en tipo str para
            hacer su encryptación a través de la llave
            recibida en el llamado del metodo
        - `Args:`
            - key (str): Llave de ecryptación del Value
            - valor (str): Valor del metodo a encryptar
        - `Returns:`
            - str: Valor encryptado
        """
        f = Fernet(key)
        token = f.encrypt(str.encode(valor))   
        return token
    
    def desEncriptarData(self, key, valor):
        """
        Toma la llave de encriptación, y el
        valor a desencriptar, y retorna el valor
        en formato str.
        - `Args:`
            - key (str): Llave de encriptación
            - valor (str): Valor a desencriptar
        - `Returns:`
            - texto (str): Valor desencriptado en UTF8
        """
        f = Fernet(key)
        texto = f.decrypt(valor)
        return texto.decode("utf-8")
    
    # Metodo para extraer un archivo zip sin duplicarse
    def extractZip(self, rutaZip):
        """
            Toma una ruta absoluta de un archivo comprimido en ".zip" para
            luego descomprimir el archivo, borrar el ".zip" original
            y retornar la ruta de la carpeta extraida
            - `Args:`
                - rutaZip (str or pathType): Ruta del archivo ".zip"
            - `Returns:`
                ruta_extraida (str or pathType): Ruta de la carpeta descomprimida
        """
        rutaConfig = rutaZip.split('\\')
        nombreCarpetaZip = rutaConfig[-1]
        nombreCarpetaOriginal = nombreCarpetaZip.replace(".zip", "")
        rutaCarpeta = rutaZip.replace(nombreCarpetaZip, "")
        rutaExtraccion = rutaCarpeta + "\\" + nombreCarpetaOriginal

        try:
            shutil.rmtree(rutaExtraccion)
        except OSError as e:
            pass
        archivo_zip = zipfile.ZipFile(rutaZip, "r")
        try:
            archivo_zip.extractall(path=rutaExtraccion)
        except Exception as e:
            pass
        archivo_zip.close()
        return rutaExtraccion
    
    # Obtención de la carpeta documents independiente del usuario que ejecuta
    def pathFolderUser(self, folder: str = 'Documents'):
        """
        Esta función se encargá de retornar la ruta de 
        la carpeta solicitda, de manera que valida el SO
        del equipo y retorna el full path de la ruta
        de la carpeta que se ha solicitado.
        - Args:
            - folder (str, optional): Carpeta a buscar. Defaults to 'Documents'.
        - Returns:
            - rutaDocuments (str): Full path de la carpeta
        """
        if os.name == 'nt':
            pathDocs = Path(os.environ['USERPROFILE']) / folder
        rutaDocuments = pathDocs.resolve()
        return rutaDocuments
        
    # Metodo para realizar la validacion del destino
    def ValidateDestiny(self, ruta):
        cont = 0
        dir = ruta
        for f in os.listdir(dir):
            cont += 1
        return cont
