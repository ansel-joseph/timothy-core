import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
recognizer = sr.Recognizer()

engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)


def speak(text):
    print(f"Timothy: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("You: ", end="", flush=True)
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(text)
        return text.lower()
    except sr.UnknownValueError:
        print("...")
        return ""
    except sr.RequestError:
        print("Speech service unavailable.")
        return ""