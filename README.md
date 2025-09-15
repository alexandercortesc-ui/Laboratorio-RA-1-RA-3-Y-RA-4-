<h1 align="center">
 # Lab1: tipos de datos avanzados y archivos en python (-RA-1-RA-3-Y-RA-4-)
 </h1>
 <p align="center">
Alexander cortes cordoba <br />
Miguel Angel Morales Ortiz <br />
Manuel David Lucero Casanova <br />
  <p align="center">
Programació<pn, II-2025 <br />
GDSPROC <br />
Uniquindío <br />
</p>
 
Este repositorio alberga una colección de scripts desarrollados en Python, enfocados en el manejo de estructuras de datos avanzadas y operaciones con archivos. A lo largo del contenido, se presentan diversas implementaciones que ilustran cómo se aplican estos tipos de datos complejos en función del nivel de dificultad y los requerimientos específicos de cada problema. El objetivo es ofrecer ejemplos prácticos y progresivos que faciliten la comprensión y el uso eficiente de herramientas como listas anidadas, diccionarios, conjuntos, tuplas, manejo de archivos CSV, JSON, entre otros.

## Reto 1: Representacion de informacion del ususario. Codigo 1: [´reto1.py´](reto1.py)
En el primer reto, se instruyó a los estudiantes a desarrollar un programa que permitiera registrar y estructurar la información de usuarios utilizando diccionarios en Python. Esta actividad tuvo como propósito introducirlos en el manejo de estructuras de datos complejas, brindando una primera aproximación al uso de tipos de datos avanzados para representar información de manera organizada y eficiente.

## Reto 2: Almacenamiento en archivo de texto de la información del usuario. Codigo: [´reto2.py´](reto2.py)
En el reto número 2, se solicitó a los estudiantes que, en concordancia con el ejercicio anterior, realizaran modificaciones al código de manera que los datos almacenados en un diccionario fueran guardados en un archivo de texto. Para ello, debían utilizar la función dumps del módulo json de Python (from json import dumps), previamente abordada en clase.
El objetivo principal de esta actividad fue familiarizar a los estudiantes con el manejo de archivos en formato JSON, así como con la realizacion de estructuras de datos complejas, promoviendo una comprensión más profunda de los conceptos relacionados con el almacenamiento estructurado y el tratamiento de información avanzada.

## Reto 3: Registro de multiples usuarios. Codigo: [´reto3.py´](reto3.py)
En este reto se incrementó el nivel de exigencia, solicitando a los estudiantes que modificaran el código del ejercicio anterior para que no solo convierta los datos de un diccionario en texto plano, sino que además permita registrar múltiples usuarios en un archivo .
La nueva versión del programa debe cumplir con los siguientes requisitos:
- 	Registrar varios usuarios de forma consecutiva, almacenando cada uno como un objeto JSON en el archivo de texto.
- 	Verificar si el usuario ya está registrado, comparando su número de identificación con los registros existentes.
- 	En caso de que el usuario ya exista, la función debe retornar una cadena que indique el error correspondiente.
-	Si el usuario no está previamente registrado, debe guardar sus datos correctamente y retornar una cadena que confirme el registro exitoso.

Este ejercicio tuvo como objetivo consolidar los conocimientos adquiridos en los retos anteriores, promoviendo una implementación eficiente de estructuras de datos, validación de entradas y persistencia de información en formato estructurado.
## Reto 4: Inicio de sesión del usuario. codigo:
En el reto número 4, se incrementó el nivel de complejidad del ejercicio, solicitando a los estudiantes que, con base en el código previamente desarrollado, lo adaptaran para incorporar una funcionalidad de inicio de sesión para usuarios registrados.
El programa debe ser capaz de:
- Validar la existencia del usuario en el sistema mediante su número de identificación.
- Verificar la autenticidad de la contraseña proporcionada, asegurando que coincida con la registrada previamente.
- En caso de autenticación exitosa, añadir un nuevo campo al diccionario del usuario que indique que la sesión se encuentra activa.
Este desafío exige a los estudiantes integrar y aplicar de forma efectiva los conocimientos adquiridos en etapas anteriores, promoviendo así el desarrollo de habilidades avanzadas en el manejo y persistencia de datos estructurados.
## Reto 5: Gestión de consultas médicas. Codigo:
Este ya es el reto final y el que mas exigencia tiene puesto que sera el codigo usado en el proyecto y representa el desafío de mayor complejidad, ya que el código desarrollado será implementado como parte integral del sistema. En esta etapa, se ha solicitado a los estudiantes integrar componentes de ejercicios previos con el objetivo de construir un módulo en Python para la gestión de consultas médicas.
El módulo debe incorporar funciones que permitan:
- Agendar una consulta médica en una fecha y hora determinada, validando previamente que el médico esté registrado como usuario en el sistema.
- Verificar la autenticación del paciente, quien debe haber iniciado sesión para poder programar una cita.
- Persistir las consultas en un archivo de texto, almacenándolas como objetos JSON generados a partir de diccionarios en Python, siguiendo el mismo esquema utilizado para el registro de usuarios.
 ## Referencias
 [1] Geeks for Geeks, "What is an IP Address?",url=https://www.geeksforgeeks.org/computer-science-fundamentals/what-is-an-ip-address/ .
 
[2] W3schools, "Javascript JSON",url=https://www.w3schools.com/js/js_json.asp.
