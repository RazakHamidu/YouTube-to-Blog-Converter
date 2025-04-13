# Importa il modulo 're' per lavorare con le espressioni regolari
import re

# Definisce una funzione chiamata 'extract_video_id' che accetta un URL come argomento
def extract_video_id(url):
    # Cerca nell'URL un pattern che corrisponda a un ID video di YouTube
    # Il pattern cerca "v=" o "youtu.be/" seguito da una serie di caratteri che non sono "&" (l'ID del video)
    match = re.search(r"(?:v=|youtu\.be/)([^&]+)", url)
    # Se viene trovata una corrispondenza (match non è None), restituisce il primo gruppo catturato (l'ID del video)
    # Altrimenti, se non viene trovata nessuna corrispondenza, restituisce None
    return match.group(1) if match else None
