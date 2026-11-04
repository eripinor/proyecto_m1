# La app de mi proyecto
# Para verla, en la terminal: streamlit run app.py
# Son los mismos pasos que en app_pisos.py y app_titanic.py.


# Paso 1. La página
# 1.1 Importa streamlit y pandas.
# 1.2 Pon el nombre de la pestaña del navegador, la página a todo lo ancho y un título que diga de qué va tu proyecto.
# 1.3 Debajo, una o dos frases con st.write: qué pregunta responde la app y de dónde salen los datos.

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="El arte del lúpulo: datos, estilos y valoraciones de las cervezas",
    page_icon="🍻",
    layout="wide")

st.title("🍻El arte del lúpulo: datos, estilos y valoraciones de las cervezas")

st.write("Explora qué estilos reciben mejores valoraciones, qué cervecerías concentran más reseñas y si existe relación entre la graduación alcohólica y la valoración.")


# Paso 2. Los datos
# 2.1 La función cargar_datos, con @st.cache_data encima, que lea "datos/datos_limpios.csv" y lo devuelva.
#     Agrupamos las reseñas para tener una fila por cerveza, con su valoración media y número de reseñas.
# 2.2 Llama a la función y guarda las tablas en variables.

@st.cache_data
def cargar_datos():
    cervezas = pd.read_csv("datos/datos_limpios.csv.gz")  # leemos el CSV limpio

# Calculamos la valoración media de cada cerveza
    valoraciones = cervezas.groupby(["cerveceria", "cerveza", "estilo_cerveza", "graduacion"])["rating"].mean().reset_index()

# Contamos el número de reseñas de cada cerveza
    resenas = cervezas.groupby(["cerveceria", "cerveza", "estilo_cerveza", "graduacion"])["rating"].count().reset_index()

    resenas = resenas.rename(columns={"rating": "numero_resenas"})  # cambiamos el nombre de la columna

# Unimos las valoraciones y las reseñas
    cervezas_unicas = valoraciones.merge(resenas, on=["cerveceria", "cerveza", "estilo_cerveza", "graduacion"])

    cervezas_unicas = cervezas_unicas.rename(columns={"rating": "valoracion_media"})  # cambiamos el nombre de la columna

    return cervezas, cervezas_unicas  # devolvemos las dos tablas

cervezas, cervezas_unicas = cargar_datos()  # llamamos a la función y guardamos las tablas

# Paso 3. Los filtros
# 3.1 En la barra de la izquierda, permite seleccionar uno o varios estilos.
# 3.2 Añade una barra con dos puntas para elegir el intervalo de graduación.
# 3.3 Añade una barra para elegir la valoración mínima.
# 3.4 Añade una caja de texto para buscar por el nombre de la cerveza.

# Paso 3. Los filtros

with st.sidebar:

    st.header("Filtros")

    estilos = sorted(cervezas_unicas["estilo_cerveza"].dropna().unique())
    estilo = st.multiselect("Estilo de cerveza", estilos)

    graduacion_minima = float(cervezas_unicas["graduacion"].min())
    graduacion_maxima = float(cervezas_unicas["graduacion"].max())

    graduacion_min, graduacion_max = st.slider("Graduación alcohólica", graduacion_minima, graduacion_maxima, (graduacion_minima, graduacion_maxima))

    valoracion = st.slider("Valoración mínima", 0.0, 5.0, 0.0, step=0.1)

    nombre = st.text_input("Buscar cerveza")


# Paso 4. Filtrar
# 4.1 Empieza con filtrados = tu tabla, y después aplica un filtro por cada widget, como en los pisos.

filtrados = cervezas_unicas.copy()  # hacemos una copia de la tabla

# Aplicamos el filtro de estilos si se ha seleccionado alguno
if estilo:
    filtrados = filtrados[filtrados["estilo_cerveza"].isin(estilo)]

# Aplicamos el filtro de graduación mínima y máxima
filtrados = filtrados[filtrados["graduacion"] >= graduacion_min]
filtrados = filtrados[filtrados["graduacion"] <= graduacion_max]

# Aplicamos el filtro de valoración mínima
filtrados = filtrados[filtrados["valoracion_media"] >= valoracion]

# Buscamos el nombre de la cerveza si se ha escrito algo
if nombre != "":
    filtrados = filtrados[filtrados["cerveza"].str.contains(nombre, case=False, na=False)]

st.write("Cervezas encontradas:", len(filtrados))  # comprobamos que los filtros funcionan


# Paso 5. Si no queda nada
# 5.1 Si filtrados está vacía, saca un aviso con st.warning y para el programa con st.stop().

if len(filtrados) == 0:
    st.warning("No hay cervezas que cumplan los filtros seleccionados.")
    st.stop()

# Paso 6. Las métricas
# 6.1 Tres métricas en columnas, con los números más importantes para tu pregunta.

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Cervecerías", filtrados["cerveceria"].nunique())

with col2:
    st.metric("Valoración media", round(filtrados["valoracion_media"].mean(), 2))

with col3:
    st.metric("Número de reseñas", int(filtrados["numero_resenas"].sum()))


# Paso 7. Las pestañas
# 7.1 Tres pestañas: "Listado de cervezas", "Gráficos" y "¿Cuál sería tu cerveza perfecta?".

# En la primera, mostramos la tabla de cervezas filtradas.

tab1, tab2, tab3 = st.tabs(["Listado de cervezas", "Gráficos", "¿Cuál sería tu cerveza perfecta?"])

with tab1:
    st.header("Listado de cervezas")

    # Ordenamos las cervezas por valoración media
    listado = filtrados.sort_values("valoracion_media", ascending=False)

    st.dataframe(listado)


# 7.2 En la pestaña "Gráficos", mostramos dos gráficos.

with tab2:

    colx, coly = st.columns(2)

    with colx:
        st.subheader("Número de cervezas por estilo")

# Contamos las cervezas de cada estilo
        cervezas_estilo = filtrados["estilo_cerveza"].value_counts()

        st.bar_chart(cervezas_estilo)

    with coly:
        st.subheader("Valoración media por estilo")

# Calculamos la valoración media ponderada de cada estilo

        valoracion_estilos = filtrados.groupby("estilo_cerveza").apply(
            lambda grupo: (grupo["valoracion_media"] * grupo["numero_resenas"]).sum() / grupo["numero_resenas"].sum())

# Ordenamos los estilos por valoración y seleccionamos los 15 mejores
        valoracion_estilos = valoracion_estilos.sort_values(ascending=False).head(15)

# Ordenamos de menor a mayor para mostrar el gráfico
        valoracion_estilos = valoracion_estilos.sort_values()

# Mostramos el gráfico de barras horizontal
        st.bar_chart(valoracion_estilos, horizontal=True)


# Paso 8. Una pregunta para el usuario
# 8.1 El usuario elige sus preferencias y la app le recomienda cervezas según los datos.

with tab3:
    st.header("¿Cuál sería tu cerveza perfecta?")

    st.write("Selecciona tus preferencias y descubre qué cervezas se ajustan a ellas.")

# Permitimos seleccionar uno o varios estilos
    estilos_preferidos = sorted(cervezas_unicas["estilo_cerveza"].dropna().unique())
    estilo_preferido = st.multiselect("¿Qué estilos de cerveza te gustan?", estilos_preferidos)

# Permitimos elegir un intervalo de graduación alcohólica
    graduacion_preferida_min, graduacion_preferida_max = st.slider("¿Qué graduación alcohólica prefieres?", 0.0, float(cervezas_unicas["graduacion"].max()), (4.0, 7.0), step=0.1)

# Permitimos elegir una valoración mínima
    valoracion_preferida = st.slider("¿Qué valoración mínima buscas?", 0.0, 5.0, 4.0, step=0.1)

# Creamos una copia de todas las cervezas para buscar recomendaciones
    cerveza_perfecta = cervezas_unicas.copy()

# Aplicamos el filtro de estilos si se ha seleccionado alguno
    if estilo_preferido:
        cerveza_perfecta = cerveza_perfecta[cerveza_perfecta["estilo_cerveza"].isin(estilo_preferido)]

# Aplicamos el intervalo de graduación
    cerveza_perfecta = cerveza_perfecta[cerveza_perfecta["graduacion"] >= graduacion_preferida_min]
    cerveza_perfecta = cerveza_perfecta[cerveza_perfecta["graduacion"] <= graduacion_preferida_max]

# Aplicamos la valoración mínima
    cerveza_perfecta = cerveza_perfecta[cerveza_perfecta["valoracion_media"] >= valoracion_preferida]

# Exigimos un mínimo de 10 reseñas para recomendar una cerveza
    cerveza_perfecta = cerveza_perfecta[cerveza_perfecta["numero_resenas"] >= 10]

# Ordenamos las cervezas por valoración media
    cerveza_perfecta = cerveza_perfecta.sort_values("valoracion_media", ascending=False)

    st.subheader("Tus cervezas recomendadas")

# Mostramos cuántas cervezas cumplen las preferencias
    st.write("Hemos encontrado", len(cerveza_perfecta), "cervezas que pueden encajar contigo.")

# Comprobamos si hay resultados
    if len(cerveza_perfecta) == 0:
        st.warning("No hemos encontrado cervezas con esas preferencias.")

    else:
# Mostramos la tabla de cervezas recomendadas
        st.dataframe(cerveza_perfecta)