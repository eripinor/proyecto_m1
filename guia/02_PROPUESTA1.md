# Propuesta del proyecto

Rellenadla y enseñádmela antes de empezar el EDA. Son diez minutos que os pueden ahorrar días.

Nombre: Erika Pinel

## 1. La idea

Título del proyecto: Cata de datos: explorando el mundo del vino

¿Qué pregunta responde y a quién le interesa?
Este proyecto analiza la relación entre el precio y la puntuación de los vinos, las diferencias de valoración entre las distintas variedades de uva y los países de origen.

Puede interesar a los aficionados al vino que quieran descubrir qué vinos reciben mejores valoraciones, cómo se relaciona su precio con la puntuación y qué variedades y países destacan en las reseñas.


## 2. Los datos

De dónde salen:
- [X] Kaggle
- [ ] Hugging Face
- [ ] Datos míos (dónde los he encontrado):

Enlace a los datos: https://www.kaggle.com/zynicide/wine-reviews

Cuántas filas y columnas tienen: 150.930 filas y 10 columnas.

Qué es cada fila (un vino, un partido, una venta...): 

150.930 filas y 10 columnas.

Cada fila representa una reseña de un vino publicada por Wine Enthusiast. Contiene información sobre el vino, su procedencia, su variedad de uva, su precio y la puntuación que ha recibido

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

1. ¿Existe una relación entre el precio de un vino y la puntuación que recibe? --> gráfico de dispoersión

¿Qué variedades de uva obtienen las mejores puntuaciones? --> comparar las puntuaciones medias de distintas variedades de uva con gráfico de barras

¿Qué países tienen los vinos mejor valorados? --> comparar las puntuaciones medias por país de origen, con gráfico de barras

## 4. La app

¿Qué filtros pondrías en la barra de la izquierda?

País de origen, Variedad de uva, rango de precios, rango de puntuaciones.

¿Qué pregunta le harías al usuario al final?

¿Qué vino elegirías según tu presupuesto, la puntuación que buscas y tus preferencias?
alternativa: ¿cuál ofrece la mejor relación entre precio y valoración?

¿Tienen coordenadas para hacer un mapa?
- [ ] Sí
- [X] No (pero puedo hacer un mapa con los países de origen)

## 5. Plan B

Por si los datos principales no sirven, otros distintos:

Enlace:  https://huggingface.co/datasets/bamwor/world-cities?utm_source=chatgpt.com

from datasets import load_dataset
ds = load_dataset("bamwor/world-cities")
