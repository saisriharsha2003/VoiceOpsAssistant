import speech_recognition as sr


def recognize_email_from_speech():
    # Initialize the speech recognizer with the CMU Sphinx engine
    recognizer = sr.Recognizer()

    # Record audio from the microphone
    with sr.Microphone() as source:
        print("Say an email address:")
        audio = recognizer.listen(source)

    try:
        # Use the CMU Sphinx engine for speech recognition
        recognized_text = recognizer.recognize_sphinx(audio)
        print(recognized_text)
        # Find email patterns in the recognized text
        email_addresses = find_email_addresses(recognized_text)

        if email_addresses:
            print("Detected email addresses:")
            for email in email_addresses:
                print(email)
        else:
            print("No email addresses detected.")
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print("Error during speech recognition; {0}".format(e))


def find_email_addresses(text):
    import re
    # Regular expression pattern to match email addresses
    pattern = r'[\w\.-]+@[\w\.-]+'
    return re.findall(pattern, text)


if __name__ == "__main__":
    recognize_email_from_speech()
