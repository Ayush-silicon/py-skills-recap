import os
import datetime
import requests

def speak(text, voice="Microsoft Zira Desktop", rate=0, volume=100):
    """Speak text using PowerShell with adjustable voice, rate, and volume."""
    command = (
        f'powershell -Command "Add-Type -AssemblyName System.Speech; '
        f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
        f'$speak.SelectVoice(\'{voice}\'); '
        f'$speak.Rate = {rate}; '
        f'$speak.Volume = {volume}; '
        f'$speak.Speak(\'{text}\')"'
    )
    os.system(command)


if __name__ == "__main__":
    print("🤖 Welcome to RoboSpeaker 2.0 🚀")
    print("Type something and I'll speak it!")
    print("Commands: quit | time | date | hello | joke | read <filename> | save <text>")

    while True:
        x = input("\nEnter what you want me to speak: ")

        # Quit command
        if x.lower() == "quit":
            speak("Bye bye friend, talk to you later")
            break

        # Say current time
        elif x.lower() == "time":
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"⏰ Current time: {now}")
            speak(f"The current time is {now}")

        # Say current date
        elif x.lower() == "date":
            today = datetime.date.today().strftime("%B %d, %Y")
            print(f"📅 Today's date: {today}")
            speak(f"Today's date is {today}")

        # Greeting
        elif x.lower() == "hello":
            speak("Hello! How are you doing today?")

        # Joke using icanhazdadjoke API
        elif x.lower() == "joke":
            try:
                headers = {"Accept": "application/json"}
                res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
                joke = res["joke"]
                print(f"😂 Joke: {joke}")
                speak(joke)
            except Exception:
                speak("Sorry, I could not fetch a joke right now.")

        # Read a text file aloud
        elif x.lower().startswith("read "):
            filename = x[5:].strip()
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    content = f.read()
                print(f"📖 Reading file: {filename}")
                speak(content)
            else:
                speak("Sorry, file not found.")

        # Save speech to WAV file
        elif x.lower().startswith("save "):
            text_to_save = x[5:].strip()
            output_file = "output.wav"
            command = (
                f'powershell -Command "Add-Type -AssemblyName System.Speech; '
                f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
                f'$speak.SetOutputToWaveFile(\'{output_file}\'); '
                f'$speak.Speak(\'{text_to_save}\'); '
                f'$speak.Dispose()"'
            )
            os.system(command)
            print(f"💾 Saved speech to {output_file}")
            speak("Your speech has been saved to a file.")

        # Speak normal input
        else:
            speak(x)
