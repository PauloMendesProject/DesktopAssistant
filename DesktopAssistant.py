# Import necessary libraries
from pydoc_data import topics
from re import M
import speech_recognition as sr
import pyttsx3
import wikipedia

#Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Use pyttsx3 to convert text to speech and speak it aloud"""
    engine.say(text) #Queue the text to be spoken
    engine.runAndWait() #Process and speak the queued text

def listen():
    """Listen to microphone input and convert it to text using Google's speech recognition"""
    recognizer = sr.Recognizer() #Create a speeck recognition object
    with sr.Microphone(device_index=2) as source:
        recognizer.adjust_for_ambient_noise(source, duration=1.0)  # Adjust for ambient noise
        recognizer.pause_threshold = 1.5 # Set a pause threshold to avoid cutting off speech
        recognizer.non_speaking_duration = 0.5 # Set a non-speaking duration to avoid false positives
        recognizer.energy_threshold = 300  # bump this up if your mic is quiet

        print("Listening...") #Show feedback in the terminal
        audio = recognizer.listen(source, timeout=None, phrase_time_limit=10) # No hard timeout, max length of speech is 10 seconds

    try:
        #Try converting the speech to text using Google's online recognizer
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower() #Return the recognized text in lowercase
    except sr.UnknownValueError:
        #If speech wasn't understood
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        # If google's service is unavailable
        speak("Sorry, my speech service is down.")
        return ""

def main():
    """Main function: greets the user, then waits for voice commands in a loop"""
    speak("Hello, I am your desktop assistant. How can I help you today?")
    
    while True:
        command = listen()  # Wait for a voice command
        
        # If the user said something containing "wikipedia"
        if "wikipedia" in command:
            speak("Searching Wikipedia...")
            topic = command.replace("wikipedia", "").strip()  # Extract topic from the command

            try:
                summary = wikipedia.summary(topic, sentences=2)
                print(f"Summary: {summary}") # Print the summary to the console
                speak("According to Wikipedia...")
                speak(summary)
            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find anything on that topic.")
        
        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        elif command:
            speak("I can search Wikipedia. Just say 'Wikipedia' followed by your topic.")

# Run the assistant only if this script is the entry point
if __name__ == "__main__":
    main()
