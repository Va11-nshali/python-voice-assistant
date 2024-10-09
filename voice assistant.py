import speech_recognition as sr
import pyttsx3
import webbrowser
import tkinter as tk
from tkinter import messagebox

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Function to convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Function to listen for voice commands and handle them"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            # Listen to the user's command
            print("Listening...")
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            print(f"User said: {command}")
            # Display the recognized command in the GUI
            user_command.set(command)
            handle_command(command)
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Sorry, I could not understand the command.")
            speak("Sorry, I could not understand the command.")
        except sr.RequestError:
            messagebox.showerror("Error", "Could not request results; check your internet connection.")
            speak("Could not request results; check your internet connection.")

def handle_command(command):
    """Function to handle commands based on recognized text"""
    if 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'search' in command:
        search_term = command.replace("search", "").strip()
        speak(f"Searching for {search_term}")
        webbrowser.open(f"https://www.google.com/search?q={search_term}")
    elif 'exit' in command or 'quit' in command:
        speak("Goodbye!")
        root.quit()
    else:
        speak("Sorry, I did not understand the command.")

# Function to trigger listening
def trigger_listen():
    listen()

# Initialize the GUI
root = tk.Tk()
root.title("Voice Assistant")

# Set up the GUI layout
user_command = tk.StringVar()

label = tk.Label(root, text="Press the button and give a voice command", font=("Arial", 14))
label.pack(pady=10)

command_entry = tk.Entry(root, textvariable=user_command, font=("Arial", 14), width=40)
command_entry.pack(pady=10)

listen_button = tk.Button(root, text="Listen", command=trigger_listen, font=("Arial", 14), bg="blue", fg="white")
listen_button.pack(pady=20)

exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 14), bg="red", fg="white")
exit_button.pack(pady=10)

root.mainloop()
