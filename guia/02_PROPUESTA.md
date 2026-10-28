# Propuesta del proyecto

Rellenadla y enseñádmela antes de empezar el EDA. Son diez minutos que os pueden ahorrar días.

Nombre: Erika

## 1. La idea

Título del proyecto: El arte del lúpulo: datos, estilos y valoraciones de las cervezas

¿Qué pregunta responde y a quién le interesa?

Este proyecto analiza qué características de una cerveza están más relacionadas con su valoración final, las diferencias entre los distintos estilos de cerveza y cómo influye la graduación alcohólica en las puntuaciones. 
Puede interesar a los aficionados a la cerveza que quieran conocer mejor sus estilos y descubrir qué aspectos valoran más las personas que las prueban.

## 2. Los datos

De dónde salen:
- [X] Kaggle
- [ ] Hugging Face
- [ ] Datos míos (dónde los he encontrado):

Enlace a los datos: https://www.kaggle.com/rdoume/beerreviews

Cuántas filas y columnas tienen: 1.586.614 filas y 13 columnas.

Qué es cada fila (un vino, un partido, una venta...): Cada fila representa una reseña, es decir, una persona que puntúa una cerveza. Por tanto, una misma cerveza puede aparecer en varias filas, ya que puede haber sido valorada por diferentes personas. Esto significa que el número de filas no equivale al número de cervezas únicas.

Comprobado (los requisitos están en 03_DATOS.md):
- [X] Son tabulares, en una sola tabla
- [X] No los hemos usado en clase
- [X] Tienen más de 1.000 filas
- [X] Tienen al menos 6 columnas, con números y con texto
- [X] Entiendo qué es cada columna
- [X] Hay algo que limpiar
- [X] Sé de dónde salen y se pueden usar
- [ ] El CSV limpio pesará menos de 100 MB

## 3. Tres preguntas que quiero responder

1. ¿Qué características de una cerveza están más relacionadas con su valoración general?
2. ¿Qué estilos de cerveza obtienen las mejores valoraciones?
3. ¿Las cervezas con mayor graduación alcohólica reciben mejores puntuaciones?

## 4. La app

¿Qué filtros pondrías en la barra de la izquierda?

Estilo de cerveza: para seleccionar uno o varios estilos.
Graduación alcohólica: para limitar el análisis a un intervalo de alcohol.
Valoración general: para seleccionar las puntuaciones que nos interesan.
Nombre de la cerveza: para buscar una cerveza concreta

¿Qué pregunta le harías al usuario al final?:

¿Cuál sería tu cerveza perfecta? y seleccionar  preferencias, por ejemplo:
    - Estilo de cerveza: podrá seleccionar uno o varios estilos.
    - Graduación alcohólica: podrá indicar sus preferencias respecto al contenido de alcohol.
    - Nota mínima: podrá establecer la puntuación mínima que debe tener una cerveza.

¿Tienen coordenadas para hacer un mapa?
- [ ] Sí
- [X] No

## 5. Plan B

Por si los datos principales no sirven, otros distintos: 

Cata de datos: explorando el mundo del vino
Enlace: https://www.kaggle.com/datasets/zynicide/wine-reviews?utm_source=chatgpt.com