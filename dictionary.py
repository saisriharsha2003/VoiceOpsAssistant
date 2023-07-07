from PyDictionary import PyDictionary
import pyttsx3

user = "harsha"
assistant = 'Jarvis'
assistant = pyttsx3.init()
assistant.setProperty('rate', 150)
voices = assistant.getProperty("voices")
assistant.setProperty("voice", voices[0].id)


def output(audio):
    assistant.say(audio)
    assistant.runAndWait()


print("Which word do I need to explain the meaning of? Sir!")
word = input()
meaning_of_word = PyDictionary().meaning(word)
print(meaning_of_word)
pos_tag = list(meaning_of_word.keys())

meanings = list(meaning_of_word.values())
print(meanings)
for i in range(len(meaning_of_word)):
    output("when the " + word + " is a " + pos_tag[i] + ",its meaning is " + str(meanings[i]))
