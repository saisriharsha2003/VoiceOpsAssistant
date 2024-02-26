from nltk.corpus import wordnet
from CommonFunctions import desktop_assistant, speak, user, inputCommand

def meaning_of_the_word():
    print(desktop_assistant + ":Which word do I need to explain its meaning for?!")
    speak("Which word do I need to explain its meaning for?!")
    word = inputCommand()
    print(f"{user}: {word}")
    synsets = wordnet.synsets(word)
    if synsets:
        meaning_of_word = synsets[0].definition()
        print(meaning_of_word)
        speak(f"The meaning of {word} is {meaning_of_word}")
    else:
        meaning_of_word = "Meaning not found."