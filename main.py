from voice import speak, listen

def main():
    speak("Hello Ansel. I am Timothy.")

    while True:
        user_input = listen()

        if user_input == "exit":
            speak("Goodbye.")
            break

        speak(f"You said {user_input}")

if __name__ == "__main__":
    main()