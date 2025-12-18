# Audio to Compte Rendu

Ce projet permet de transformer un fichier audio (réunion, compte-rendu vocal) en texte, puis de générer un compte rendu structuré.

---

## Fonctionnement

1. **Conversion audio** : le fichier audio est converti en WAV mono à 16 kHz.
2. **Transcription Whisper** : le modèle `whisper-small` est utilisé pour transcrire l’audio en texte.
3. **(Optionnel) Compte rendu** : on peut utiliser une IA locale pour transformer la transcription en compte rendu structuré.

---

## Installation

Cloner le dépôt :

```bash
git clone https://github.com/<votre-username>/audio-to-compte-rendu.git
cd audio-to-compte-rendu

