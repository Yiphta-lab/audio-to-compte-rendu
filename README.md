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

```
bash
git clone https://github.com/<votre-username>/audio-to-compte-rendu.git
cd audio-to-compte-rendu
```
---


## Installation des dépendances

Créer un environnement Python et l’activer :

```bash
# Linux / Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

##Installer les dépendances depuis le fichier requirements.txt :
```bash
pip install -r requirements.txt
```


##Pour générer le requirements.txt depuis ton environnement actuel :

```bash
pip freeze > requirements.txt
```

##Utilisation
1. Transcription audio → texte

Le script transcription.py convertit l’audio en WAV, puis le transcrit en texte avec Whisper-small.

```bash
python3 transcription.py
```

Le résultat sera enregistré dans transcription.txt.

2. Génération du compte rendu

Le script compte_rendu.py prend la transcription existante et produit un compte rendu structuré.

```bash
python3 compte_rendu.py 
```

Le compte rendu est structuré avec les sections suivantes :

- **TITRE**
- **CONTEXTE**
- **POINTS DISCUTÉS**
- **DÉCISIONS PRISES**
- **ACTIONS À MENER**

---

## Notes sur l’IA utilisée

- **Option locale** : Le script utilise un LLM Mistral en local pour produire le compte rendu. Si les performances sont limitées sur de longues transcriptions, il est possible de générer le compte rendu via NotebookLM (outil en ligne de Google) en donnant simplement la transcription.  
  - [NotebookLM](https://notebook.google.com/)  

---



