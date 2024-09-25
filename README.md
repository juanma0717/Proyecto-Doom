# Proyecto-Doom

Uno de los mejores juegos de la historia al alcance de tu mano

¿Estas preparado?


# Integrantes
- Juan Manuel Berdugo Torres
- Fabian Camilo Arciniegas Morales
- Santiago Camargo Molina

# Introducción
El proceso de crear tu propia consola de videojuegos puede parecer abrumador, especialmente si no cuentas con los conocimientos técnicos necesarios. A menudo, esto nos lleva a optar por comprar consolas comerciales, aunque resulten costosas. Con esto en mente, hemos desarrollado un proyecto que te permite diseñar y fabricar tu propia consola estilo Gameboy. No solo aprenderás durante el proceso, sino que también podrás disfrutar del icónico juego DOOM en una consola completamente funcional creada por ti mismo. Este proyecto DIY es altamente escalable, lo que significa que puedes agregar más funciones a la consola, limitadas únicamente por tu imaginación.

# Objetivos
Se definieron diferentes objetivos para plantear el rumbo del proyecto.
## Objetivo general
Diseñar y construir un prototipo electrónico funcional que permita a los usuarios interactuar con el dispositivo de manera fluida y divertida.
## Objetivo especificos
- Desarrollar un circuito electrónico eficiente que controle los elementos del juego.
- Programar el sistema del juego utilizando el lenguaje Micro Python para gestionar las interacciones entre el jugador y el prototipo.

# Alcance
El proyecto implica diseñar y fabricar una consola portátil estilo Gameboy que ejecute DOOM. Se utilizarán componentes como un microcontrolador (ESP32), pantalla, botones y batería, junto con librerías como ST7735 para adaptar el juego. La consola será portátil, con controles básicos y batería recargable, permitiendo la posibilidad de añadir futuras mejoras.

# Resultados
En primer lugar, en términos de ensamblaje, se logró que la pantalla SPI de 1.4 pulgadas mostrara información. Además, se conectaron los pulsadores al ESP32, permitiendo su uso como controles del juego. Con el módulo MH-CD14, se consiguió que todo el circuito funcionara a través de una batería, y finalmente, se añadió un buzzer que mejoró la experiencia al reproducir música.

Sin embargo, en el aspecto del software, no se logró que el juego DOOM funcionara con los diferentes componentes. Hubo un problema de compatibilidad entre los controladores de la pantalla y la librería del juego, ya que estaban en lenguajes de programación diferentes, y hacer que funcionaran juntos excedía el tiempo previsto. Por ello, se decidió optar por hacer funcionar el juego Snake.

# Video
[![Alt text](https://i9.ytimg.com/vi/RTt2J5ldDGo/mqdefault.jpg?sqp=CLC70bcG-oaymwEmCMACELQB8quKqQMa8AEB-AHSBoAC4AOKAgwIABABGHIgSCg6MA8=&rs=AOn4CLC1xFNVR_9DOYOby9jscaQATIAmYg)](https://youtu.be/RTt2J5ldDGo)

# Conclusiones
En primer lugar, se concluye que ejecutar el juego DOOM en una ESP32 presenta dificultades debido a la complejidad de su código. Aunque existen proyectos documentados previamente, muchos no están en MicroPython o presentan documentación inconsistente.

Por otro lado, el proceso de diseñar una consola resulta muy entretenido, y desarrollar un circuito para ejecutar un juego popular puede atraer a más personas al mundo de la electrónica.
