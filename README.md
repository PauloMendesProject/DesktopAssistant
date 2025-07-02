# DesktopAssistant

A simple Python voice-controlled desktop assistant that listens to your commands, searches Wikipedia, and responds using text-to-speech.

---

## Features

- **Voice recognition** using Google's speech recognition API via the `speech_recognition` library.
- **Text-to-speech** responses powered by `pyttsx3`.
- **Wikipedia integration**: Searches and summarizes Wikipedia articles.
- Handles common voice commands such as searching Wikipedia and exiting the program.
- Compatible with Python 3.10 and 3.11.

---

## Installation

1. Install Python 3.10 or 3.11 if you haven't already.

2. Install the required Python packages:

   ```bash
   pip install speechrecognition pyttsx3 wikipedia

Important Note About Microphone Input:
The assistant uses a specific microphone device index set in the code

with sr.Microphone(device_index=2) as source:

You may need to adjust the device_index in your listen() function to match your system’s microphone. To find your device index, you can run this snippet:

import speech_recognition as sr

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Microphone with index {index}: {name}")

    Troubleshooting
The assistant requires an active internet connection for Google’s speech recognition.

Adjust microphone sensitivity parameters in listen() if speech recognition is inconsistent.
