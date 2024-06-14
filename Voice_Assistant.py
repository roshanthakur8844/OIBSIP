import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import asyncio

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine with a female voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Index 1 corresponds to a female voice

# Adjust recognition threshold
recognizer.energy_threshold = 1000  # Adjust the value based on your environment and microphone sensitivity

def speak(text):
    """Convert text to speech and play it."""
    engine.say(text)
    engine.runAndWait()

async def listen(timeout=5):
    """Capture audio from the microphone and recognize the speech."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=timeout)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.WaitTimeoutError:
            print("Listening timeout. No speech detected.")
            return None
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return None

async def respond_to_command(command):
    """Perform tasks based on the recognized command."""
    if not command:
        speak("Hello! I'm your voice assistant. How can I assist you today?")
        return
    elif 'hello' in command:
        speak("Hello! How can I assist you today?")
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif 'date' in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
    elif command.startswith('search for'):
        query = command.replace('search ', '').strip()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {query}")
        else:
            speak("Please specify what you want to search for.")
    else:
        speak("I am sorry, I don't understand that command.")

async def process_commands():
    """Process commands until the program stops."""
    while True:
        command = await listen()
        if command:
            await respond_to_command(command)

async def main():
    speak("Hello! My name is Assistant. How can I help you today?")
    await asyncio.gather(process_commands())

if __name__ == "__main__":
    asyncio.run(main())