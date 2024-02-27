import tkinter as tk
from PIL import Image, ImageTk
import speech_recognition as sr
root = tk.Tk()
root.title("Virtual Assistant")

# Load images
blank_image = ImageTk.PhotoImage(Image.open("blank_image.png"))
listening_image = ImageTk.PhotoImage(Image.open("listening_image.png"))

# Create a label for the listening state graphic
listening_label = tk.Label(root, image=blank_image)
listening_label.pack()

# Create a button to start voice recognition
button = tk.Button(root, text="Start Voice Recognition", command=start_voice_recognition)
button.pack()

# Start the Tkinter event loop
root.mainloop()
