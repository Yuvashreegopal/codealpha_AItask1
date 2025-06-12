from tkinter import *
from googletrans import Translator, LANGUAGES

# Initialize main window
root = Tk()
root.title("🌐 Language Translator")
root.geometry("550x600")
root.config(bg="#ffe6f0")  # Soft pink background

translator = Translator()
lang_codes = list(LANGUAGES.keys())
lang_names = list(LANGUAGES.values())
lang_dict = dict(zip(lang_names, lang_codes))

# Header
Label(
    root,
    text="🌐 Language Translator",
    font=("Segoe UI", 20, "bold"),
    bg="#ffe6f0",
    fg="#0033cc"
).pack(pady=20)

# Input Frame
input_frame = Frame(root, bg="#ffe6f0")
input_frame.pack(pady=5)

Label(
    input_frame,
    text="Enter Text:",
    font=("Segoe UI", 12, "bold"),
    bg="#ffe6f0",
    fg="#0033cc"
).grid(row=0, column=0, sticky=W)

input_text = Text(
    input_frame,
    height=7,
    width=60,
    font=("Segoe UI", 11),
    bg="white",
    fg="#0033cc",
    bd=2,
    relief="groove"
)
input_text.grid(row=1, column=0, padx=10, pady=5)

# Language Selection
lang_frame = Frame(root, bg="#ffe6f0")
lang_frame.pack(pady=10)

Label(lang_frame, text="From:", font=("Segoe UI", 11), bg="#ffe6f0", fg="#0033cc").grid(row=0, column=0, padx=5, sticky=E)
src_lang = StringVar()
src_lang.set("english")
OptionMenu(lang_frame, src_lang, *lang_names).grid(row=0, column=1, padx=5)

Label(lang_frame, text="To:", font=("Segoe UI", 11), bg="#ffe6f0", fg="#0033cc").grid(row=0, column=2, padx=5, sticky=E)
dest_lang = StringVar()
dest_lang.set("tamil")
OptionMenu(lang_frame, dest_lang, *lang_names).grid(row=0, column=3, padx=5)

# Translate Button
def translate():
    try:
        src = lang_dict[src_lang.get()]
        dest = lang_dict[dest_lang.get()]
        translated = translator.translate(input_text.get("1.0", END), src=src, dest=dest)
        output_text.delete("1.0", END)
        output_text.insert(END, translated.text)
    except Exception as e:
        output_text.delete("1.0", END)
        output_text.insert(END, f"Error: {str(e)}")

Button(
    root,
    text="🔁 Translate",
    command=translate,
    bg="#ff3399",  # Deep pink for button
    fg="white",
    font=("Segoe UI", 12, "bold"),
    padx=20,
    pady=8,
    relief="raised",
    bd=2
).pack(pady=20)

# Output Frame
output_frame = Frame(root, bg="#ffe6f0")
output_frame.pack()

Label(
    output_frame,
    text="Translated Text:",
    font=("Segoe UI", 12, "bold"),
    bg="#ffe6f0",
    fg="#0033cc"
).grid(row=0, column=0, sticky=W)

output_text = Text(
    output_frame,
    height=7,
    width=60,
    font=("Segoe UI", 11),
    bg="white",
    fg="#0033cc",
    bd=2,
    relief="groove"
)
output_text.grid(row=1, column=0, padx=10, pady=5)

root.mainloop()
