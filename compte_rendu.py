from transformers import pipeline
from pydub import AudioSegment, silence
import numpy as np
import ollama
from utils import load_transcription, generate_compte_rendu

# ======================================================
# 1. AUDIO → WAV
# ======================================================


# ======================================================
# 4. MAIN PIPELINE
# ======================================================
if __name__ == "__main__":
    
    transcription_file = "transcription2.txt"
    compte_rendu_file = "compte_rendu2.txt"

    
    
    # Charger transcription
    transcription = load_transcription(transcription_file)
    
    generate_compte_rendu(
        transcription,
        model="mistral",
        output_file=compte_rendu_file
    )

    print("Pipeline terminé ✅")

