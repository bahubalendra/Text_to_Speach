#not work
import pyttsx3

data = input("enter your text:\n")

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()