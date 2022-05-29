# Simulacion de matriz

Simulación para calcular la presión con el método implícito usando la ecuación de difusividad con ciertas suposiciones.

En esta simulación calculamos la presión para estudiar el caudal de petróleo de un pozo, viendo la evolucion de la presion en diferentes posiciones y el tiempo.

## Variables
Al ejecutar el programa, primero nos pide que pongamos las filas y las columnas, pero al ser una matriz tridiagonal, se necesita que sea una matriz cuadrada (igual filas que columnas).

Luego te pide diferentes variables tal como:
 - phi : porosidad en fracción
 - mu : viscosidad en cP
 - ct : compresibilidad total (fluido + formación)
 - perm : permeabilidad de la roca
 - dx : diferencial de posicion en el eje x
 - dt : diferencial de tiempo
 - a : constante que aparece en la ecuacion de difusividad
 - 
Ecuación de difusividad (con varias suposiciones):

![ecuasion de difusividad](https://user-images.githubusercontent.com/69403501/170887661-ef7a2b73-55c5-49a5-8b92-43621907e9bb.png)

Para sacar el numerador de la constante que aparece en la ecuacion de difusividad se necesita la siguiente ecuacion:

La porosidad en fraccion multipiclado por la viscosidad en cP multiplicado por 10 elevado a la-3 multiplicado por la cmpresibilidad total por la diferencial de posicion en el eje x elevado al cuadrado, es decir:

phi * mu*10^-3 * ct * dx^2

Luego para sacar el denominador de la constante que aparece en la ecuacion de difusividad se necesita: 
la permeabilidad de la roca multiplicado por 9.87 por 10 elevado a la -16 multiplicado por la diferenciad de tiempo por 6894.75729, es decir:

perm * 9.87*10^-16 * dt * 6894.75729

a = phi * mu*10^-3 * ct * dx^2 / perm * 9.87*10^-16 * dt * 6894.75729


Utilizando la ecuación vista, y aplicando los operadores para el método implícito:

![ecuasion de difusividad2](https://user-images.githubusercontent.com/69403501/170887662-a4f42b79-e3b4-43bc-a158-2a539901bae3.png)

Despejando ![Captura de pantalla 2022-05-29 161025](https://user-images.githubusercontent.com/69403501/170887684-b28d806c-3fd7-4f77-a185-f976ee9bdb74.png)

![Captura3](https://user-images.githubusercontent.com/69403501/170887691-dcbcd7a2-0598-465b-9970-92502099322f.png)

Tomando como condición de contorno un lado de presión constante y uno de caudal nulo:

-Presión constante: ![Captura4](https://user-images.githubusercontent.com/69403501/170887725-be2f1d17-02ad-4cc5-ab47-006553493720.png)

-Caudal nulo: ![Captura5](https://user-images.githubusercontent.com/69403501/170887737-272cd9b6-1655-4eec-80b7-f95b636bcd19.png)

Aplicando las condiciones en la discretización:

![Captura6](https://user-images.githubusercontent.com/69403501/170887744-33668ffd-581b-4fb9-9b73-4f426ee07496.png)

Escribiéndolo matricialmente:

![Captura8](https://user-images.githubusercontent.com/69403501/170887774-baf7f767-3b39-4151-b4ba-29fe0c3c0dfd.png)

Esto se puede ver como: 

![Captura7](https://user-images.githubusercontent.com/69403501/170887787-05eccb9e-c84e-48d7-960d-662f7de29124.png)

## Matriz tridiagonal

Una vez que las variables ya estan colocadas, se llama a la funcion creaMatriz con los parametros n y m (filas y columnas, respectivamente) que ya hemos colocado anteriormente y se crea una matriz tridiagonal automaticamente.
Una Matriz tridiagonal en álgebra lineal es una matriz cuyos elementos son solo distintos de cero en la diagonal principal y las diagonales adyacentes por encima y por debajo de esta.

Por ejemplo

![353a4862130008599653ed68ed0e2ae49cc2c455](https://user-images.githubusercontent.com/69403501/169623124-d63a5f7e-ccef-4579-b61c-e867ba035c9f.svg)

El resultado de la matriz se muestra por consola. Y se llama a otra funcion en la cual se invierte esta matriz tridiagonal.

## Matriz A

La matriz A es creada por la funcion matrizA con los parametros m, n y a (columnas, filas y la constante que aparece en la ecuacion de difusividad, respectivamente), la cual se crea automaticamente y aparece en consola una vez hecha.

## Matriz B 

Esta matriz es creada por la funcion matrizB la cual tiene los parametros BHP, PI y n (n de filas), estas variables son:
 - BHP: Bottom hole pressure o la presión del fondo del pozo.
 - PI: Presión inicial en la formación

Para calcular el BHP primero se tiene que introducir el MBHP (Mega bottom hole pressure, la presion original divida a 10 elevado a la 6), y ahi se multipica el MBHP por 10 elevado a la 6 o MBHP * 10^6 y se obtiene el BHP.

Y para calcular la presión inicial se precisa el MPI (Mega presión inicial) que se introduce por comando, y multiplicando esta variable por 10 elevado a la 6 se obtiene PI.
Luego se crea automaticamente y aparece en consola una vez hecha.

## Multiplicaciones de matrices

Aca es donde se llama a la funcion invertirMatriz con el parametro crearMatriz (funcion que crea la matriz tridiagonal) y despues se multiplica con la matrizA (funcion que crea la matriz A) con sus respectivos parametros.

Por último se multiplica el resultado de lo anterior por la funcion matrizB (que devuelve la matriz B).
