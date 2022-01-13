from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox
import threading
import pyttsx3

root = Tk()
root.title('Translator')
root.geometry("880x300")


def Threading():
    t = threading.Thread(target=translate_it)
    t.start()


def translate_it():
    translated_text.delete(1.0, END)

    try:
        for key, value in languages.items():
            if value == original_combo.get():
                from_language_key = key

        for key, value in languages.items():
            if value == translated_combo.get():
                to_language_key = key

        words = textblob.TextBlob(original_text.get(1.0, END))

        words = words.translate(from_lang=from_language_key, to=to_language_key)

        translated_text.insert(1.0, words)

        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty('voice', voices[1].id)
        engine.say(words)
        engine.runAndWait()

    except Exception as e:
        messagebox.showerror("Translator", e)


def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)


languages = googletrans.LANGUAGES
language_list = list(languages.values())

original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)

translate_button = Button(root, text="Translate!", font=("Helvetica", 24), command=Threading)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0, column=2, pady=20, padx=10)

original_combo = ttk.Combobox(root, width=50, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(26)
translated_combo.grid(row=1, column=2)

clear_button = Button(root, text="Clear", command=clear)
clear_button.grid(row=2, column=1)

root.mainloop()
