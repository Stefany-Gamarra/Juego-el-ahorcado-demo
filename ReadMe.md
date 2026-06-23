**Juego del Ahorcado**

**Objetivo**

Desarrollar una aplicación de escritorio interactiva del clásico juego "El Ahorcado" utilizando Python, el entorno de desarrollo Spyder y la biblioteca gráfica Tkinter.
Utilizando lo aprendido en el módulo 1, materia de lógica de programación.

**Descripción de funcionalidades**

1. Gestión Dinámica del Vocabulario
    - Banco de Palabras en JSON: El juego no utiliza palabras fijas en el código, sino que lee el repertorio directamente desde un archivo externo en formato .json.
    - Escalabilidad: Permite actualizar, añadir o categorizar nuevas palabras de manera sencilla sin necesidad de modificar el código fuente de la lógica ni de la interfaz.

2. Interfaz Gráfica de Usuario 
    - Ventana de Juego Principal (Adivinar): Espacio central donde se desarrolla la partida, diseñado cuidando la estrucutra y ubicación de los elementos.
    - Botonera Virtual de Letras: Un teclado en pantalla optimizado visualmente con botones de gran tamaño para facilitar la interacción táctil o con el ratón, mejorando la usabilidad.
    - Desactivación de Teclas: Las letras ya seleccionadas por el usuario se deshabilitan automáticamente para evitar intentos duplicados y guiar visualmente los pasos restantes.
    - Visualización del Progreso de la Palabra: Espacios dinámicos que se van completando en tiempo real a medida que el jugador acierta las letras correctas.

3. Motor Lógico del Juego (Separación de Conceptos)
    - Arquitectura Desacoplada: Estricta separación entre los módulos de datos, lógica de control e interfaz gráfica. El núcleo lógico procesa los aciertos, errores y estados de la partida sin afectar la interfaz.
    - Control de Intentos y Estado: Contador interno que registra los fallos del jugador y desencadena de forma precisa los eventos de finalización de la partida.
    - Condiciones de Victoria y Derrota: Pantallas o notificaciones emergentes que gestionan de manera clara el flujo cuando el jugador adivina la palabra completa o agota sus oportunidades.

**Librerías utilizadas**

- tkinter (incluida en Python)
- random (incluida en Python)

**Cómo ejecutar**

1. Tener Python instalado
2. Abrir el archivo ahorcado.py en Spyder
3. Ejecutar con F5

**Fecha**

Junio del 2026

**Autoría**

Stefany Gamarra Vistin
- Gmail: stefanygamarrav2005@gmal.com