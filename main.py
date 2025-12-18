from transformers import pipeline
from pydub import AudioSegment, silence
import numpy as np
import ollama
# ======================================================
# 1. AUDIO → WAV
# ======================================================
def convert_to_wav(input_audio, output_wav, target_sr=16000):
    audio = AudioSegment.from_file(input_audio)
    audio = audio.set_frame_rate(target_sr).set_channels(1)
    audio.export(output_wav, format="wav")
    return output_wav


# ======================================================
# 2. WAV → TRANSCRIPTION (WHISPER)
# ======================================================

def transcribe_whisper(
    wav_file,
    model_name="openai/whisper-small",
    silence_len=500,
    silence_thresh=-35
):
    print("Chargement de Whisper...")
    asr = pipeline(
        "automatic-speech-recognition",
        model=model_name,
        device=-1,              # CPU
        chunk_length_s=30
    )

    audio = AudioSegment.from_wav(wav_file)

    chunks = silence.split_on_silence(
        audio,
        min_silence_len=silence_len,
        silence_thresh=silence_thresh,
        keep_silence=250
    )

    print(f"{len(chunks)} segments détectés.")

    transcription = ""

    for i, chunk in enumerate(chunks):
        samples = np.array(chunk.get_array_of_samples()).astype(np.float32)
        samples /= np.iinfo(chunk.array_type).max

        if chunk.channels == 2:
            samples = samples.reshape((-1, 2)).mean(axis=1)

        result = asr(
            {"array": samples, "sampling_rate": chunk.frame_rate},
            language="fr",
            generate_kwargs={"temperature": 0.0}
        )

        transcription += result["text"].strip() + " "
        print(f"Segment {i+1}/{len(chunks)} transcrit.")

    return transcription.strip()


# ======================================================
# 3. TRANSCRIPTION → COMPTE RENDU (OLLAMA LOCAL)
# ======================================================

def generate_compte_rendu(
    transcription,
    model="mistral",
    output_file="compte_rendu.txt"
):
    print("Génération du compte rendu...")

    prompt = f"""
Tu es un assistant professionnel spécialisé dans la rédaction de comptes rendus de réunion.

À partir de la transcription ci-dessous :
- corrige le langage oral
- reformule en français professionnel
- structure clairement
- identifie les décisions
- liste les actions à mener

FORMAT STRICT :

TITRE
CONTEXTE
POINTS DISCUTÉS
DÉCISIONS PRISES
ACTIONS À MENER

TRANSCRIPTION :
{transcription}
"""

    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": "Assistant expert en comptes rendus de réunion."},
            {"role": "user", "content": prompt}
        ],
    )

    compte_rendu = response["message"]["content"]

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(compte_rendu)

    return compte_rendu





# ======================================================
# 4. MAIN PIPELINE
# ======================================================
if __name__ == "__main__":
    input_audio = "compte_rendu2.m4a"
    wav_file = "compte_rendu2.wav"
    transcription_file = "transcription2.txt"
    compte_rendu_file = "compte_rendu2.txt"

    convert_to_wav(input_audio, wav_file)

    transcription = transcribe_whisper(wav_file)

    with open(transcription_file, "w", encoding="utf-8") as f:
        f.write(transcription)

    
    
    
    generate_compte_rendu(
        transcription,
        model="mistral",
        output_file=compte_rendu_file
    )

    print("Pipeline terminé ✅")

