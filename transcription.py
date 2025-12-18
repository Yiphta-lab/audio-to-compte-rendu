from transformers import pipeline
from transformers import pipeline
from pydub import AudioSegment, silence
import numpy as np
import ollama
from utils import convert_to_wav, transcribe_whisper


# ======================================================
# 4. MAIN PIPELINE
# ======================================================
if __name__ == "__main__":
    input_audio = "compte_rendu2.m4a"
    wav_file = "compte_rendu2.wav"
    transcription_file = "transcription2.txt"
    

    convert_to_wav(input_audio, wav_file)

    transcription = transcribe_whisper(wav_file)

    with open(transcription_file, "w", encoding="utf-8") as f:
        f.write(transcription)

    
    
    
    
