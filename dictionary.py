from nltk.corpus import wordnet
import pyttsx3
import speech_recognition as sr


user = "harsha"
assistant = 'Jarvis'
assistant = pyttsx3.init()
assistant.setProperty('rate', 150)
voices = assistant.getProperty("voices")
assistant.setProperty("voice", voices[0].id)

def speak(audio):
    assistant.say(audio)
    assistant.runAndWait()

def inputCommand():
    rec = sr.Recognizer()
    count = 0
    while count < 1:
        with sr.Microphone() as source:
            rec.pause_threshold = 1
            rec.adjust_for_ambient_noise(source)
            audio = rec.listen(source)
            try:
                query = rec.recognize_google(audio, language="en-IN")
                count += 1
            except Exception:
                speak("Sorry,I can't hear you!")
    return query

def output(audio):
    assistant.say(audio)
    assistant.runAndWait()

def speak(audio):
    assistant.say(audio)
    assistant.runAndWait()

def get_meaning(word):
    synsets = wordnet.synsets(word)
    if synsets:
        return synsets[0].definition()
    else:
        return "Meaning not found."

speak("Which word do I need to explain the meaning of? Sir!")
word = inputCommand()
print(word)
meaning_of_word = get_meaning(word)
print(meaning_of_word)
output(f"The meaning of {word} is {meaning_of_word}")
