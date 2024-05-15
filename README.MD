# Proyecto Hipoteca Inversa en Python con practicas de Clean Code


## ¿Quién hizo esto?

Alejandro Gutierrez Vallejo
Andrea Márquez Sánchez

## ¿Qué es y para qué es?

Este proyecto tiene como objetivo calcular una Hipoteca Inversa desarrollada en Python.

## ¿Cómo lo hago funcionar?

Prerrequisitos:
- Editor de texto: Se recomienda utilizar un editor de texto adecuado para el desarrollo en Python. Se recomienda utilizar Visual Studio Code.

- Asegúrate de tener instalada la última versión de Python en tu sistema.

- Asegúrate de tener instalado pip, para poder instalar kivy.

- Instalar kivy para ejecutar la interfaz gráfica.

Instalación de Python:
- Descargar Python: Visita el sitio web oficial de Python (https://www.python.org/) y descarga la última versión estable disponible para tu sistema operativo.

- Instalar Python: Una vez descargado el instalador, sigue las instrucciones proporcionadas por el instalador para completar el proceso de instalación. Durante la instalación, asegúrate de marcar la opción que permite agregar Python al PATH del sistema, lo que facilitará la ejecución de comandos desde la línea de comandos.

- Comprobar la instalación: Para verificar que Python se ha instalado correctamente, abre una terminal o ventana de comandos y ejecuta el siguiente comando:
`
python --version
`

Instalación de pip:
- Instalar pip: Ejecuta el script de instalación utilizando Python:
`
python get-pip.py
`

- Comprobar la instalación: Una vez completada la instalación, verifica que pip se haya instalado correctamente ejecutando el siguiente comando:
`
pip --version
`

Instalación de Kivy
Kivy es una biblioteca Python de código abierto para el desarrollo de aplicaciones multiplataforma que incluye interfaces de usuario (UI). Puedes instalar Kivy utilizando pip, el gestor de paquetes de Python.

- Instalación de Kivy: Ejecuta el siguiente comando en tu terminal o ventana de comandos:
`
pip install kivy"[base]"
`
Este comando instalará la versión más reciente de Kivy y todas sus dependencias necesarias.


Al cumplir con estos prerrequisitos, estarás listo para utilizar el proyecto y comenzar a trabajar en él.


## Estructura sugerida

La estructura del proyecto sigue las prácticas recomendadas para mantener un código organizado y modular. A continuación, se describe la estructura sugerida:

- src: Esta carpeta contiene el código fuente de la aplicación. Está organizada en capas para facilitar el mantenimiento y la escalabilidad del proyecto. La estructura de carpetas dentro de src es la siguiente:

* Console: Contiene el codigo fuente de la interfaz de usuario por consola

* Interface: Contiene el codigo fuente de la interfaz grafica de la aplicación.

* Logic: Contiene el codigo fuente para realizar el calculo de la Hipoteca Inversa

- tests: Esta carpeta contiene las pruebas unitarias para validar el correcto funcionamiento del código.

Recuerde que cada carpeta de código fuente debe contener un archivo __init__.py que permite que python
reconozca la carpeta como un Módulo.

* Ejecución de la GUI
Para ejecutar la interfaz gráfica de usuario, sigue estos pasos:

Navega hasta la carpeta src/Interface del proyecto.
Ejecuta el siguiente comando en la terminal o ventana de comandos: python Hipoteca_Inversa_Interface.py.

## Uso

Para ejecutar las pruebas unitarias desde la carpeta test, utiliza los siguientes comandos:

`
  Hipoteca-Inversa> cd tests
  Hipoteca-Inversa\test> python Hipoteca_Inversa_Tests.py
`

Si deseas ejecutarlas desde la carpeta raíz, asegúrate de incluir la ruta de búsqueda de los módulos al inicio del módulo de pruebas:

`
  import sys
  sys.path.append("src")
`

Si se desea devolver, ejecuta el siguiente comando cuantas veces sea necesario:
`
  cd ..
`

Para ejecutar la interfaz de usuario mediante por consola, utiliza los siguientes comandos:

`
  Hipoteca-Inversa> cd src
  Hipoteca-Inversa\src> cd Console
  Hipoteca-Inversa\src\Console> python Hipoteca_Inversa_Console.py
`

Si se desea devolver, ejecuta el siguiente comando cuantas veces sea necesario:
`
  cd ..
`

Para ejecutar la interfaz gráfica de usuario, utiliza los siguientes comandos:

`
  Hipoteca-Inversa> cd src
  Hipoteca-Inversa\src> cd Interface
  Hipoteca-Inversa\src\Interface> python Hipoteca_Inversa_Interface.py
`