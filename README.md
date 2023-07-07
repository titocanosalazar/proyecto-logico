# proyecto-logico

Paso previo:

Tener instalado Python, el código funciona desde consola.

Explicación:

La función calcular() toma una cadena como entrada y realiza las operaciones especificadas en dicha cadena. La cadena debe estar en el formato "num1 operador num2 operador ...", 
donde "num1", "num2", etc. Son los números y "operador" es el operador (+, -, *, /).

La función divide la cadena utilizando el método .split() para obtener los números y los operadores por separado. 

Luego, se convierten los números en formato de tipo flotante y se realizan las operaciones correspondientes utilizando estructuras de control.

El resultado de la operación se devuelve y se muestra en la consola.

Se introdujo el diccionario operadores_prioridad que asigna una prioridad numérica a cada operador. Los operadores con mayor prioridad se evalúan primero.

En cada iteración, se encuentra el operador con la mayor prioridad. Luego, se actualiza la lista numeros reemplazando los operandos y eliminando el operador evaluado.

Cuando no quedan operadores pendientes, el resultado final se encuentra en numeros[0].

Finalmente se valida la cantidad de caracteres en la cadena, si son menores a 20 se realiza la operación de lo contrario manda un mensaje indicando, que la cantidad se excedió. 

 Ejemplo de uso: Se tienen que colocar los numero uno a ala vez y siempre dejando un espacio.
 
Observar imagen:




![image](https://github.com/titocanosalazar/proyecto-logico/assets/111630034/54c02bcc-2ad9-4b3d-a668-a64f7aa44477)

