# El arte del lúpulo: datos, estilos y valoraciones de las cervezas

El arte del lúpulo: datos, estilos y valoraciones de las cervezas

Proyecto de análisis de datos con Python para explorar las valoraciones de distintas cervezas, estudiar sus características y descubrir qué factores pueden estar relacionados con las puntuaciones que reciben.

## La pregunta

1. ¿Qué características están relacionadas con la valoración general de una cerveza? 
2. ¿Qué estilos reciben mejores puntuaciones?
3. ¿Existe una relación entre la graduación alcohólica y la valoración?

El objetivo es utilizar Python y el análisis exploratorio de datos (EDA) para investigar estas preguntas y, más adelante, desarrollar una aplicación que permita explorar cervezas según sus características.

## Los datos

- De dónde salen: (https://www.kaggle.com/datasets/rdoume/beerreviews)
- Cuántos son: 1.586.614 filas y 13 columnas en el conjunto original. Después de la limpieza, el conjunto contiene 1.518.829 filas y 10 columnas.
- Qué es cada fila: una reseña de una cerveza. 

## Qué he limpiado y por qué

- He eliminado las columnas brewery_id, review_profilename y review_time, porque no eran necesarias para el análisis planteado.

- He traducido al español los nombres de las diez columnas restantes para que sean más fáciles de interpretar.

- He detectado 67.785 filas sin información sobre la graduación alcohólica y las he eliminado para poder analizar la relación entre esta variable y las valoraciones.

- He conservado las valoraciones iguales a cero porque, aunque pueden ser valores atípicos, no hay información suficiente para afirmar que sean errores.

- He revisado las distribuciones de las variables numéricas, los valores atípicos y la frecuencia de los distintos estilos de cerveza.

## Lo que he encontrado

1. Distribución de las valoraciones: la valoración general tiene una media de 3,82 y una mediana de 4 sobre 5. Esto indica que las puntuaciones se concentran, en general, en valores relativamente altos.

2. Relación entre variables numéricas: la correlación de Pearson entre la graduación alcohólica y la valoración general es de aproximadamente 0,14. Se trata de una relación positiva débil, por lo que la graduación por sí sola no explica las diferencias entre las puntuaciones.

3. Diferencias entre grupos: la valoración media varía según el estilo de cerveza. American Wild Ale obtiene una media de 4,10, mientras que Low Alcohol Beer alcanza una media de 2,55. También se observa que las cervezas con una graduación superior al 9 % tienen una valoración media de 3,94, frente a 3,58 en las cervezas de hasta el 5 %.

4. Limpieza de los datos: he eliminado tres columnas, he traducido los nombres de las diez columnas restantes y he eliminado las filas que no tenían información sobre la graduación alcohólica. El conjunto ha pasado de 1.586.614 a 1.518.829 filas.

## La app

![La app](capturas/app.png)

(Qué se puede hacer en la app, en dos o tres frases.)

Enlace: (si la has publicado en Streamlit Community Cloud)

## Cómo ejecutarlo

1. Crear un entorno e instalar las librerías: `pip install -r requirements.txt`
2. El EDA está en `eda.ipynb`.
3. La app se abre con `streamlit run app.py`.

## Autor

## Autor

Erika Pinel Ortega

- GitHub: [@eripinor](https://github.com/eripinor)
- LinkedIn: [erika-pinel](https://www.linkedin.com/in/erika-pinel/)
