# ------importing modules----------
from tkinter import *
import tkinter as tk
from tkinter import *
import tkinter.ttk
from tkinter.ttk import Combobox
from PIL import *
from tkinter import filedialog
from tkinter import messagebox
import os

# ------creating main window----------
window = Tk()
window.geometry("800x500+200+120")
window.configure(bg="#005669")
window.title("Text To Speech")


# ---------speak button definitions------------------
def speak():
    import pyttsx3

    # getting values fo fields.
    textInput = textArea.get(1.0, "end-1c")
    textGender = genderText.get()
    textSpeed = speedText.get()
    if textInput == "":
        messagebox.showerror("Error", "text field is empty !")
    elif textGender == "select":
        messagebox.showerror("Error", "Please select voice gender !")
    elif textSpeed == "select":
        messagebox.showerror("Error", "Please select voice speed !")
    else:
        # inittialize the pyttsx3 module
        engine = pyttsx3.init()
        # voice change script
        voices = engine.getProperty("voices")
        if textGender == "Hindi":
            engine.setProperty("voice", voices[1].id)
        elif textGender == "English Women":
            engine.setProperty("voice", voices[2].id)
        # voice rate or speed script
        speed = engine.getProperty("rate")
        if textSpeed == "Slow":
            engine.setProperty("rate", 90)
        elif textSpeed == "Fast":
            engine.setProperty("rate", 220)
        else:
            engine.setProperty("rate", 150)
        # speak the string given in say().
        engine.say(textInput)
        engine.runAndWait()
        """for voice in voices:
            print("Voice: %s" % voice.name)
            print(" - ID: %s" % voice.id)
            print(" - Languages: %s" % voice.languages)
            print(" - Gender: %s" % voice.gender)
            print(" - Age: %s" % voice.age)
            print("\n")"""


# ---------save button definitions------------------
def save():
    # getting values fo fields.
    import pyttsx3

    textInput = textArea.get(1.0, "end-1c")
    textGender = genderText.get()
    textSpeed = speedText.get()
    if textInput == "":
        messagebox.showerror("Error", "text field is empty !")
    elif textGender == "select":
        messagebox.showerror("Error", "Please select voice gender !")
    elif textSpeed == "select":
        messagebox.showerror("Error", "Please select voice speed !")
    else:
        # inittialize the pyttsx3 module
        engine = pyttsx3.init()
        # voice change script
        voices = engine.getProperty("voices")
        if textGender == "Hindi":
            engine.setProperty("voice", voices[1].id)
        elif textGender == "English Women":
            engine.setProperty("voice", voices[2].id)
        # voice rate or speed script
        speed = engine.getProperty("rate")
        if textSpeed == "Slow":
            engine.setProperty("rate", 90)
        elif textSpeed == "Fast":
            engine.setProperty("rate", 220)
        else:
            engine.setProperty("rate", 150)
        # speak the string given in say().
        path = filedialog.askdirectory()
        os.chdir(path)
        engine.save_to_file(textInput, "speech.mp3")
        engine.runAndWait()
        messagebox.showinfo("info", "download successfull !")


# ---------close button definitions------------------
def close():
    textInput = textArea.get(1.0, "end-1c")
    if textInput != "":
        ans = messagebox.askquestion("Confirm", "Are you sure?")
        if ans == "yes":
            window.destroy()
    else:
        window.destroy()


# ------------field text variable---------------------
genderText = StringVar()
speedText = StringVar()

# ---------canvas on main window------------------
canvas = Canvas(
    window,
    bg="#005669",
    height=500,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
canvas.place(x=0, y=0)

# ---------text area script------------------
entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(294.0, 283.5, image=entry0_img)

textArea = Text(
    window,
    bd=0,
    padx=20,
    pady=20,
    bg="#252525",
    fg="white",
    font=("Times New Roman", 14),
    highlightthickness=0,
)
textArea.configure(insertbackground="white")
textArea.place(x=24, y=121, width=540, height=323)

# ---------gender box script------------------
gender = Combobox(
    window,
    values=["English men", "Hindi", "English Women"],
    font="arial 10",
    state="r",
    width=11,
    height=40,
    textvariable=genderText,
)
gender.place(x=660, y=211)
gender.set("select")

# ---------speed box script------------------
speed = Combobox(
    window,
    values=["Slow", "Normal", "Fast"],
    font="arial 10",
    state="r",
    width=11,
    height=40,
    textvariable=speedText,
)
speed.place(x=660, y=140)
speed.set("select")

# ---------background icon UI script------------------
background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(326.5, 253.0, image=background_img)

# ---------save button script------------------

img0 = PhotoImage(file=f"img0.png")
b0 = Button(
    image=img0, borderwidth=0, highlightthickness=0, command=save, relief="flat"
)

b0.place(x=659, y=38, width=104, height=23)
# ---------speech script------------------

img1 = PhotoImage(file=f"img1.png")
b1 = Button(
    image=img1, borderwidth=0, highlightthickness=0, command=speak, relief="flat"
)

b1.place(x=659, y=287, width=104, height=23)

# ---------close button script------------------
img2 = PhotoImage(file=f"img2.png")
b2 = Button(
    image=img2, borderwidth=0, highlightthickness=0, command=close, relief="flat"
)

b2.place(x=659, y=367, width=104, height=23)

window.resizable(False, False)
window.mainloop()
