# Importa la classe ChatOpenAI dalla libreria langchain_openai per interagire con i modelli OpenAI
from langchain_openai import ChatOpenAI
# Importa il modulo 'os' per interagire con il sistema operativo, per leggere le variabili d'ambiente
import os
# Importa la funzione load_dotenv dalla libreria python-dotenv per caricare le variabili d'ambiente da un file .env
from dotenv import load_dotenv

# Carica le variabili d'ambiente definite nel file .env nella sessione corrente
load_dotenv()

# Definisce una funzione chiamata 'LlmModel' che accetta il testo completo della trascrizione come argomento
def LlmModel(full_text):
    # Recupera la chiave API di OpenAI dalla variabile d'ambiente "OPENAI_API_KEY"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    # Inizializza il modello ChatOpenAI specificando il modello da usare ("gpt-4o-mini") e fornendo la chiave API
    model = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)
    # Definisce il prompt di sistema che istruisce il modello su come comportarsi (come un generatore di blog)
    promptSystem = "Agisci come un generatore di Blog. Ti daro la trascrizione di un video Yuotube e tu generai la versione blog di quel video. Dammelo in formato mackdown per una Migliore leggibità"

    # Crea una lista di messaggi per la conversazione con il modello:
    # Il primo messaggio è di tipo "system" e contiene le istruzioni generali (promptSystem)
    # Il secondo messaggio è di tipo "human" e contiene il testo della trascrizione (full_text)
    prompts = [
    ("system", promptSystem),
    ("human", full_text)
    ]

    # Invia i prompt al modello e ottiene la risposta. '.content' estrae il testo della risposta generata.
    response = model.invoke(prompts).content
    # Restituisce il contenuto della risposta generata dal modello (il post del blog in formato Markdown)
    return response
