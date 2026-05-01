import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 175)   # speed
engine.setProperty("volume", 1.0) # volume


def speak(text):
    print(f"Timothy: {text}")
    engine.say(text)
    engine.runAndWait()