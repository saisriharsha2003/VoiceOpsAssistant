from CommonFunctions import desktop_assistant, speak, user
from config import authorized_password

def authenticate(max_attempts=3):
    attempts = 0
    while attempts < max_attempts:
        print(desktop_assistant + ": Whats the password?")
        speak("Whats the password?")
        password = input("Type Your Password to Authenticate yourself: ")
        print(f"{user}: {password}")
        if password.lower() == authorized_password:
            print("Authentication successful. Starting the virtual assistant.")
            speak("Authentication successful. Starting the virtual assistant.")
            return True
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                print(f"{desktop_assistant}: Incorrect password. {remaining_attempts} attempts remaining. Try again.")
                speak(f"Incorrect password. {remaining_attempts} attempts remaining. Try again.")
            else:
                print(f"{desktop_assistant}: Incorrect password. Maximum attempts reached. Exiting.")
                exit()