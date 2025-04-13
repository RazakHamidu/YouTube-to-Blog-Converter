# Importa la libreria per ottenere la trascrizione dei video YouTube
from youtube_transcript_api import YouTubeTranscriptApi
# Importa la libreria Streamlit per creare l'interfaccia web
import streamlit as st

# Importa la funzione per interagire con il modello LLM dal file model.py
from model import LlmModel
# Importa la funzione per estrarre l'ID del video dall'URL dal file extract_video_id.py
from extract_video_id import extract_video_id


# Imposta il titolo dell'applicazione Streamlit, con "YouTube" in rosso
st.title(":red[YouTube] to Blog Converter 🔴📝")

# Crea un campo di input testuale per l'utente dove inserire il link del video YouTube
LinkVideo = st.text_input("Inserisci il video youtube")

# Controlla se l'utente ha inserito un link nel campo di input
if LinkVideo:
    # Mostra il video YouTube nell'interfaccia Streamlit usando il link fornito
    st.video(LinkVideo)
    # Estrae l'ID univoco del video YouTube dall'URL inserito
    video_id = extract_video_id(LinkVideo)
    # Ottiene la trascrizione del video specificato dall'ID, provando prima in inglese ('en') e poi in italiano ('it')
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'it'])
    # Unisce tutte le parti testuali della trascrizione in una singola stringa, separate da uno spazio
    full_text = " ".join([entry['text'] for entry in transcript])
    # Invia il testo completo della trascrizione al modello LLM per generare il post del blog
    response = LlmModel(full_text)
    # Mostra la risposta (il post del blog generato) nell'interfaccia Streamlit, interpretando il formato Markdown
    st.markdown(response)
