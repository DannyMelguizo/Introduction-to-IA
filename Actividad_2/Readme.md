# Actividad 2

## 1. Descripcion del dataset (fuente, numero de registros, variables, objetivo del problema).

### Fuente: https://www.kaggle.com/datasets/vikasjigupta786/customer-analytics-practice-dataset

El dataset contiene los datos de 196 clientes en un Mall, permitiendonos realizar varias tareas sobre la informacion contenida, como clasificar los datos, realizar regresiones, agrupamiento, etc. Permitiendo poner un poco en practica el aprendizaje de maquina.

Descripcion de las columnas del dataset:

**1. CustomerID** identificador del cliente.

**2. Gender** genero.

**3. Age** edad del cliente.

**4. Annual Income (k$)** ingreso anual en miles de dolares.

**5. Spending Score (1-100)** comportamiento de gasto asignado por el Mall.

**6. Age Group** grupo de edades.

**7. Estimated Savings (k$)** ahorros estimados aproximados entre el ingreso y el gasto.

**8. Credit Score** puntuacion sintetica influenciada por los ingresos y los gastos.

**9. Loyalty Years** medida aproximada de la duracion de la relacion con el cliente.

**10. Preferred Category** preferencia de compras (Lujo, Moda, Electronicos, Economico).


### Objetivo del problema

Se plantea la idea de que somos un negocio y tenemos cierta informacion recolectada sobre algunos clientes, queremos saber que tipo de publicidad podemos ofrecerle a una persona, basandonos en su edad, genero, ingresos mensuales, cuanto suele gastar dicha persona y/o cuanto suele ahorrar. Se busca principalmente aprovechar cualquier tipo de informacion que se pueda recolectar o tener en cualquier negocio o empresa y generar un beneficio para la misma con esta.

Es un problema muy comun y ayuda a entender un poco el procesamiento que ocurre detras de cualquier aplicacion cuando aceptamos politicas sobre el tratamiento de datos y demas.

## 2. Preprocesamiento realizado.
El dataset fue un poco modificado eliminando algunos campos para generar un poco mas de trabajo a la hora de preprocesar los datos.

**1. Limpieza de Datos:** Se implemento el manejo de valores nulos, en este caso, si no habia un genero especificado se tomaba una opcion aleatoria, ya que es una variable o categoria que no genera tanto impacto, ademas, se eliminaron columnas innecesarias o que aportaban muy poco para determinar que categoria preferiria el cliente.

**2. Codificacion de Variables Categoricas:** Se transformaron las variables categoricas en numeros, por ejemplo, el genero: Female = 0 y Male = 1, al igual que se establecio una codificacion para la variable de categoria preferida.

**3. Normalizacion de los Datos:** Se normalizaron las demas variables utilizando StandardScaler(), que calcula el nuevo valor tomando el valor original menos la media y se divide entre la desviacion estandar.

**4. Division entre Train/Test:** Del dataset se tomo el 70% de la muestra para entrenar los diferentes modelos y el ultimo 30% para realizar pruebas, ademas, se hacen cuatro pruebas adicionales con datos tomados del dataset original para validar la efectividad del modelo.


## 3. Evaluacion de Resultados

En cuando a metricas de rendimiento, encontramos que el modelo **Decision Trees** nos daba el resultado con una precision de 1.00 siendo bastante preciso con las respuestas a la hora de encontrar nuevas muestras. Por otro lado, con 120 generaciones el modelo **Neural Networks** nos da una precision un poco mas variable, en ocasiones de 0.8865 teniendo fallas con las pruebas de testeo realizadas.


## 4. Analisis Comparativo

Solamente se realizaron pruebas con dos modelos, **Decision Trees** y **Neural Networks**, se observo un claro aumento en el tiempo de ejecucion en el **Neural Networks**, siendo 5.92 segundos comparado con 0.018 que le tomo a **Decision Trees** entrenarse. Ademas, de que **Neural Networks** presentaba errores en la prediccion de algunos elementos, se justifica un poco por la cantidad de datos en el dataset, ya que 196 es relativamente poco para este tipo de modelo. Adicionalmente, los datos del dataset son bastante estructurados y son pocos permitiendo que **Decision Trees** tenga un mejor desempeño en esta prueba.


## 5. Conclusiones

Para el dataset presentado es sin duda mucho mejor utilizar el modelo de **Decision Trees**, por su rapidez, es bastante facil de usar y es super bueno cuando el volumen de datos a analizar es bajo. No quiere decir que **Neural Networks** sea malo, solo que para el contexto actual, presenta ciertas desventajas ante otros modelos, por otro lado, si el dataset fuera de datos no estructurados o que los datos tuvieran muy poca relacion entre si y ante un volumen de datos mayor, convendria utilizar **Neural Networks** ya que el procesamiento de este tipo de informacion seria mucho mas complejo.
