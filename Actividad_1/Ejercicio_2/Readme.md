## 1. Solucion del Problema.

## 2. ¿Cómo cambia el comportamiento del algoritmo si cambiamos la función de costo?
No, si se cambian los diferentes costos que tienen las diferentes casillas, el algoritmo seguira funcionando correctamente, cambiara la salida pero no en si su comportamiento. Si por costo nos referimos a la funcion manhatan_distance, si, al cambiar la forma en la que se calcula la heuristica puede cambiar el comportamiento.

## 3. ¿Qué sucede si hay múltiples salidas en el laberinto? ¿Cómo podrías modificar el algoritmo para manejar esto? Plantea una  propuesta.
Si el laberinto cuenta con multiples salidas, se tendria que modificar el algoritmo para que basandonos en el punto de entrada o de inicio, al calcular la heuristica de los nodos cercanos, dirigirnos hacia la salida mas cercana.

## 4. Modifica el laberinto por uno más grande y con otro tipo de obstáculo además de paredes. ¿Qué limitación encuentras en el algoritmo? 
Le cuesta mas recursos (tiempo y memoria) alcanzar la salida, en caso tal de agregar un obstaculo, afectaria dependiendo de en donde se encuentre el obstaculo, es decir, que no este bloqueando un camino esencial o necesario para alcanzar la salida.
