# Sistema IGUana

  El sistema IGUana consiste en una interfaz para la utilización de cajeros automaticos sin la necesidad de tocar botones con la mano,
  esto debido a la necesidad de contener la transimisión de virus y bacterias que existen en la superficie de un cajero automatico.

# Explicación

  El sistema se inicia con una pantalla que muestra 9 cuadros verdes, eston son usados para la calibracion creando un histograma con los colores detectados,
  posteriormente el codigo encuentra el centroide del histograma creado y se procede a realizar un seguimiento de este centroide, todo esto utilizando OpenCV.
  Ademas del seguimiento del centroide se obtienen las coordenadas de este en todo momento y con estas se procede a generar eventos de mouse, especificamente 
  mover el cursor, detras de todo esto se encuentra una interfaz simple a modo de ejemplo para que la demostración del sistema sea más ilustrativa.
  
# Modo de uso
  1) Coloque el dedo en los cuadros verdes que se encuentran en la pantalla
  2) Presione el pedal para iniciar el control del cursor
  3) Desplace el cursor por la pantalla al boton de interes, y presione el pedal para ingresar la selección
