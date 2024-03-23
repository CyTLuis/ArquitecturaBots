# ===========================================================================
# Importaciones de clases y librerias necesarias en este archivo main
# ===========================================================================

# Region -  Importaciones de archivos o librerias
from controller.Log import Log
from controller.Impresor import Impresor
# Endregion - Importaciones de archivos o librerias

# ===========================================================================
# VARIABLES GLOBALES - LOCALES - INICIALIZACION DE OBJETOS
# ===========================================================================

# Region - Instancia de clases de archivos importado
logger = Log()
consola = Impresor()
# Endregion - Instancia de clases de archivos importado

# Region - Body Metodo Principal
def main():
    try: 
        consola.imprimirInicio("Nombre de la Automatización")
        logger.registroInicioProcesos()
        
        logger.registrarLogProceso("Inicio de ejecución del proceso")
        
        # Region - Cuerpo de la automatización
        
        # Endregion - Cuerpo de la automatización
        
        consola.imprimirFinal()
        logger.registroFinalProcesos()
    except Exception as e:
        logger.registrarLogEror(f"Error no controlado en la ejecución del proyecto: {e}", "Ejecución de Main")
        consola.imprimirError(f"Error no controlado en la ejecución del proyecto: {e}")
# Endregion

# Metodo para ejecución del Script, invocando la función main()    
if __name__ == '__main__':
    main()