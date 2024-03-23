# ArquitecturaBots-es

> ## Necesidad
>
> Definir la arquitectura inicial de los proyectos de automatización realizadas con Python, estableciendo así los driver a utilizar y distribución de carpetas definida dentro del proyecto.
>
> ## Solución
>
> Proyecto plantilla con definición y distribución de carpetas y archivos iniciales, con distintos modulos útiles para el desarrollo de la automatización que se este desarrollando.
>
> En este proyecto, se defino la herramienta [GeckoDriver](https://firefox-source-docs.mozilla.org/testing/geckodriver/index.html) como la herramienta encargada del WebDriver de Selenium para la interacción con páginas web, a través del navegador Mozilla Firefox.

### Estructura de carpetas

1. ***/content***

* Carpeta contenedora de archivos que interactuan directamente con las interfaz gráfica, simulando el comportamiento de un humano procesado a través de un robot.

2. ***/controller***

* Carpeta de gestión de archivos correspondientes a la lógica de negocio, ejercicios tales como lecturas de excel, modulos separados según el tipo de información, controladores de información entrante y de salida.
* /utils => Carpeta de archivos referentes a las utilidades usadas en cualquier lugar del proytecto, dando metodos para la reutilización de código repetido, asegurando la modularización del código.

3. ***/plugins***

* Carpeta contenedora de los plugins o .exe a utilizar como herramientas de interacción

4. ***/vendor***

* Carpeta contenedora de los archivos temp, imagenes, txt, y demás elementos usados en la ejecución del proceso, o en su defecto, generados automaticamente durante las ejecuciones.

## Comentarios útiles para los procesos de automatización

### Comando para conversión de archivo *".py"* a ejecutable *".exe"*

Comando base para conversión a ejectutable:

* ***py -m PyInstaller  --icon="ruta-absoluta-archivo-ico" ruta-abosulta-main-proyecto***

Banderas de comando para ejecutable:

* **--onefile** Crea el ejecutable en un solo archivo comprimido que lleva el nombre del archivo main pasado, con extensión .exe
* **--windowed** Dehabilita las ventanas de CMD durante la ejecución del programa.

Cabe resaltar que se debe tener instalada la libreria **Pyinstaller** antes de realizar este paso. **(pip install pyinstaller)**

### Uso de Grid dentro de las vistas de Tkinter.

Al crear automatizaciones, es posible hacer uso de la libreria de Tkinter para la creación de interfaces gráficas con las que podría interactuar el usuario final, de esa manera,

> En la respuesta de [esta publicación](https://stackoverflow.com/questions/28089942/difference-between-fill-and-expand-options-for-tkinter-pack-method) de Stack Overflow se puede encontrar de manera gráfica la explicación de como acomodar los elementos tipo frame en las distintas posiciones de la interfaz.

## Librerias usadas en el proyecto base

La siguiente es la lista completa de librerias o paquetes usados en la creación de la base del proyecto, y por ende, dependiendo de las herramientas a utilizar, necesitaremos tener instalado en la maquina a correr el desarrollo:

* [Pillow](https://pillow.readthedocs.io/en/latest/handbook/tutorial.html#create-jpeg-thumbnails) (python3 -m pip install --upgrade Pillow)
* [Selenium ](https://www.selenium.dev/selenium/docs/api/py/api.html)(pip install selenium)
* [keyboard](https://pypi.org/project/keyboard/) (pip install keyboard)
* [pyautogui ](https://pyautogui.readthedocs.io/en/latest/)(pip install pyautogui)

## Comentarios para el código

Para la reutilización del código, y basado en la nomenclatura que le querramos dar, se necesita documentar el código, de manera que se puedan entender las clases y metodos directamente desde su instancia, mostrando los parametros que se reciben, o el proposito de ese bloque de código, para ello se comentará de la siguiente manera:

Python no nos permite empaquetar bloques de código basado en su sintaxis, por ende, usaremos la extensión: Folding Region, que se encargará de empaquetar el código de la región en bloques individuales, para lograr separar por segmentos:

* Para user Folding Region, luego de instalarla, nos ubicamos en el apartado del código a empaquetar, y en la parte superior abrimos la región (# Region - Main), y al finalizar el bloque, cerramos dicha región (# Endregion - Main)
* ```
  (# Region - Main Encargada del main del código)
  if __name__ == '__main__':
      main()
  (# Endregion - Main Encargada del main del código)
  ```

Necesitamos a la par, documentar las clases, de manera que al instanciar la clase, podamos encontrar una guia visual de lo que hace la clase, para ello, en Python, usaremos la sintaxis de comentarios que nos ofrece:

* Para abrir el comentario usamos las triples comillas dobles, en la apertura y cierre (**""" Aquí va el comentario """**)
* Dentro del comentario que declaramos, podemos usar distintas formas para darle formato al comentario, por ejemplo, usaremos el signo igual (**=**) para generar titulos.
* Podemos hacer uso de las comillas invertidas (**``**) para "resaltar en negrilla un texto".
* Haremos uso de el doble numeral (**##**) para crear subtitulos dentro del bloque de comentario.
* Y podemos hacer uso del guión medio (**-**) para generar elementos de lista.

  ```
  class Ejemplo:
      """
          Aquí ira el titulo
          ==================
          Luego del titulo, generamos el comentario general del 
  	bloque, el cual será la descripción de lo que estamos 
  	comentando, en este caso, la descripción de la clase.
          ## Este es el subtitulo
          - Elemento 1 de la lista
  	- Elemento 2 de la lista
  	- Generalmente se usan las listas para dar ejemplo de los 
  	  posibles usos que se le pueden dar en este caso a la clase.
      """
  ```

Ahora, necesitamos documentar también las funciones, basados en la finalidad de la misma.

Teniendo en cuenta que una función puede o no recibir variables de entrada, a la par que puede o no dar datos de retorno, la documentación de ejemplo estará basada en aquellas funciones que tienen elementos de entrada, y de retorno.

La documentación será igual a la de la clase, con los mismos posibles elementos (Titulo, subtitulo, lista, cadena en negrilla, etc) y le adicionaremos los elementos **args**, y **returns**. Encargados de describir los argumentos recibidos por la función y el retorno de la misma.

Opcionalmente, se puede "tipar" los argumentos de la función, pasando el tipo de dato que espera recibir.

```
def funcionDePrueba(self, variableUno: str, variableDos: bool, variableTres: tuple):
        """
            En esta sección describiremos el porque, el uso, y la
	    configuración que tendrá el comportamiento de la clase.
            - `Args:`
                - variableUno (str): Variable tipada en dato tipo str 
                - variableDos(str): Variable tipada en dato tipo boolean
                - variableTres (tuple): Variable tipada en dato tipo tupla
            - `Returns:`
                data (tipoDeDatoDeRetorno): Descripción del elemento a retornar
            - `Posibles usos:`
                Descripción en lista de los usos que se le podrán dar a la función.
        """
```

### Utilizar variables de entorno

Para la realización de procesos de automatizaciones o robots, lo ideal es manejar variables de entorno, esto nos asegura el correcto funcionamiento del aplicativo independientemente de su versión, o instancias dadas en el equipo.

Otra de las ventajas de esto, es que en caso de empaquetar el aplicativo desarrollado, nos aseguraremos que solo se empaqueten las librerias necesarias dentro del proyecto, evitando así empaquetamientos de tamaño sobre dimensionados.

* python -m venv env ***(Comando para instancia de entorno virtual)***
* .\env\Scripts\activate ***(Comando para activar el entorno virtual)***
* pip list ***(Listado de librerias utilizadas)***
* pip freeze > librerias.txt ***(Obtención de librerias en archivo TXT)***
* pip install -r librerias.txt ***(Instalación de librerias desde archivo TXT)***
