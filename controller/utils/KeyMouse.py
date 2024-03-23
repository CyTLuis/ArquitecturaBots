import time, keyboard, pyautogui

class KeyMouse:

    """
        KeyMouse
        ======== 
        Es la clase encargada de entregar metodos de utilidad
        para interactuar con el teclado y el mouse, de manera que se puedan
        inclusive dar click en imagenes a través de la combinación de funciones.
        ## Usos
        - Interacción del proyecto con la interfaz gráfica.
        - Interacción entre elementos y pestañas del navegador.
        - Acciones básicas de Windows o Win Explorer.
    """
    def __init__(self) -> None:
        pass

    def maximizarVentana(self):
        """
            Metodo para: maximizar ventana actualmente activa
            - `KEYS:` atajo de teclado (win + fecla arriba)
        """
        keyboard.press('win')
        time.sleep(0.2)
        keyboard.press_and_release('up')
        keyboard.release('win')
        time.sleep(1)
    
    def tab(self):
        """
            Metodo para: presionar una sola vez la tecla tab.
            - `USAGE:` Posicionarse dentro de elemento de interfaz usando tabulador
        """
        keyboard.press_and_release('tab')
        time.sleep(0.2)

    
    def pressBarraUrl(self):
        """
            Metodo para: activar la barra del navegador en el que se esta activo.
            - `KEYS:`  atajo de teclado (CRTL + L)
        """
        keyboard.press('ctrl')
        time.sleep(0.2)
        keyboard.press_and_release('l')
        keyboard.release('ctrl')
        time.sleep(1)
    
    def seleccionarArchivos(self):
        """
            Metodo para: seleccionar todos los elementos de la ventana activa.
            - `KEYS:`  atajo de teclado (CRTL + E)
        """
        keyboard.press('ctrl')
        keyboard.press_and_release('e')
        keyboard.release('ctrl')

    def copiarTeclado(self):
        """
            Metodo para: copiar todo lo que se este seleccionado.
            - `KEYS:`  atajo de teclado (CRTL + C)
        """
        keyboard.press('ctrl')
        keyboard.press_and_release('c')
        keyboard.release('ctrl')
        time.sleep(3)
    
    def pegarTeclado(self):
        """
            Metodo para: pegar el elementos (o elementos) dentro del clipboard
            - `KEYS:`  atajo de teclado (CRTL + V)
        """
        keyboard.press('ctrl')
        keyboard.press_and_release('v')
        keyboard.release('ctrl')
        time.sleep(10)

    def abrirEjecutar(self):
        """
            Metodo para: Abrir ventana de "Ejecutar" de Windows.
            - `KEYS:`  atajo de teclado (WIN + R)
        """
        keyboard.press('win')
        keyboard.press_and_release('r')
        keyboard.release('win')
        time.sleep(0.25)
    
    def abrirDescargasNavegador(self):
        """
            Metodo para: Abrir apartado de descargas del navegador activo.
            - `KEYS:`  atajo de teclado (CTRL + J)
        """
        keyboard.press('ctrl')
        keyboard.press_and_release('j')
        keyboard.release('ctrl')
        time.sleep(0.25)
    
    def abrirMenuTareas(self):
        """
            Metodo para: Abrir menú de opciones de programa.
            - `KEYS:`  atajo de teclado (Shift + F10)
        """
        keyboard.press('shift')
        keyboard.press_and_release('f10')
        keyboard.release('shift')
        time.sleep(0.5)

    def cambiarVentana(self):
        """
            Metodo para: Cambiar entre ventanas (Una vez)
            - `KEYS:`  atajo de teclado (Alt + Tab)
        """
        keyboard.press('alt')
        keyboard.press_and_release('tab')
        keyboard.release('alt')
        time.sleep(1.5)
    
    def cerrarVentanaForzado(self):
        """
            Metodo para: Cerrar una ventana de manera forzosa.
            - `KEYS:`  atajo de teclado (Alt + F4)
        """
        keyboard.press('alt')
        keyboard.press_and_release('f4')
        keyboard.release('alt')
        time.sleep(3)
    
    def cerrarVentanaSimple(self):
        """
            Metodo para: Cerrar ventana de manera simple (Puedo no cerrar la ventana en si).
            - `KEYS:`  atajo de teclado (Ctrl + W)
        """
        keyboard.press('ctrl')
        keyboard.press_and_release('w')
        keyboard.release('ctrl')
        time.sleep(3)

    def presionarHotKey(self, tecla):
        """
            Metodo para: Presionar una single hotkey.
            - `Params:` tecla -> La tecla que se desea presionar una sola vez
            - `USAGE:` Útil para cerrar ventanas o submit formularios
        """
        pyautogui.hotkey(tecla)

    def escribir(self, texto: str):
        """
            Metodo para: Escribir una cadena de texto en el lugar activo.
            - `Params:` texto -> Cadena de texto a escribir
            - `USAGE:` Interacción con cajas de texto
        """
        keyboard.write(str(texto))
        time.sleep(1)
    
    def moverMouse(self, pos: tuple):
        """
            Metodo para: Posicionar el mouse en una posición exacta.
            - `Params:` pos -> Tupla de coordenadas
            - `Opcional:` En la tupla de datos, se pueden pasar 3 parametros, (X, Y, y tiempo de duración entre el movimiento)
            - `USAGE:` Posicionar el mouse sobre un elemento de la interfaz gráfica.
        """
        pyautogui.moveTo(pos)
    
    def moverPestanas(self):
        """
            Metodo para: Cambiar entre pestañas del navegador de Windows.
            - `USAGE:` Cambiar entre el navegador y el explorador de windows
            - `KEYS:`  atajo de teclado (Ctrl + Shift + Tab)
        """
        keyboard.press('ctrl')
        keyboard.press('shift')
        keyboard.press_and_release('tab')
        keyboard.release('shift')
        keyboard.release('ctrl')
        time.sleep(3)
    
    def singleClick(self):
        """
            Metodo para: Dar click en la posición que se encuentra el Mouse
            - `USAGE:` Combinado con la función (moverMouse) podrá dar click sobre un elemento especifico
        """
        pyautogui.click()

    def dobleClick(self):
        """
            Metodo para: Dar doble click en la posición que se encuentra el Mouse
            - `USAGE:` Combinado con la función (moverMouse) podrá dar doble click sobre una posición especifica
        """
        pyautogui.doubleClick()
    
    def encontrarImagen(self, img, intentos):
        """
            Metodo para: Encontrar la posición de una imagen especifica, y retornar sus coordenadas centradas
            - `Args:`
                - img: (str or pathType): Ruta de la imagen que se desea ubicar
                - intentos: (int): Número de veces en las que pyautogui buscará la imagen
            - `Returns:`
                coordenadas (tuple): Coordenadas en X y Y del centro de la imagen en la pantalla compelta
            - `USAGE:` Combinado con funciones de click, podrá interactuar con elementos de la interfaz gráfica
        """
        coordenadas = None
        count = 0
        while (coordenadas is None and count < intentos) :      
            coordenadas = pyautogui.locateCenterOnScreen(img)
            time.sleep(0.5)
            count += 1
        return coordenadas

    def dobleClickCoordenadas(self, coordenadas):
        """
            Metodo para: Dar doble click en las coordenadas recibidas
            - `Args:`
                - coordenadas: (tuple): Coordenadas en (X, Y) donde dar doble click
            - `USAGE:` Combinado con la función (encontrarImagen) se podrá dar click en una posición encontrada.
        """
        if(not (coordenadas is  None)):
            pyautogui.doubleClick(coordenadas)

    def clickCoordenada(self, coordenada):
        """
            Metodo para: Dar single click en las coordenadas recibidas
            - `Args:`
                - coordenadas: (tuple): Coordenadas en (X, Y) donde dar el click
            - `USAGE:` Combinado con la función (encontrarImagen) se podrá dar single click en una posición encontrada.
        """
        if(not (coordenada is  None)):
            pyautogui.click(coordenada)

    