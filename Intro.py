import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Conversión de texto a voz")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace usaremos una de las aplicaciones de Inteligencia Artificial") 
 url = "https://textavoz.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Reconocimiento de Objetos")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
 url = "https://yolov5-qxmdztvfvyeej9s99jm39l.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Entrenando Modelos")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://u3qwqec5yxdlyer8zjqkrd.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Conversión de voz a texto")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://traductorvozatexto.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Análisis de Datos")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://drawrecog-kck6qwtvo5bkg2bgzsvm63.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Trasnscriptor Audio y Video")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://histinf-qocdvh9tqmjnzth82bem6j.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Generación en Contexto")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://chatpdf-me3mzua7c8hrsacajlpxdb.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Análisis de Imagen")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://visionapp-jpush7s2yugarzartqhcuw.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Sistema Ciberfísico")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://jacobo-kkncwvoz7dajrivddrffpx.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")


