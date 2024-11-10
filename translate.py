from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

root = Tk()
root.title("Sampaio Translator")
root.geometry("1080x400")

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c.capitalize())
    label2.configure(text=c1.capitalize())
    root.after(1000, label_change)

def translate_now():
    try:
        text_ = text1.get(1.0, END).strip()
        source_lang = combo1.get()
        target_lang = combo2.get()
        
        if text_:
            # Obtém os códigos de idioma da seleção do usuário
            src_lang_code = language.get(source_lang.lower())
            tgt_lang_code = language.get(target_lang.lower())
            
            # Tradução usando deep_translator
            translated_text = GoogleTranslator(source=src_lang_code, target=tgt_lang_code).translate(text_)
            text2.delete(1.0, END)
            text2.insert(END, translated_text)
        else:
            text2.delete(1.0, END)  # Limpa o campo de saída se o campo de entrada estiver vazio
    except Exception as e:
        messagebox.showerror("Translation Error", f"Erro na tradução. Por favor, tente novamente.\nErro: {str(e)}")

def clear_output(event):
    if not text1.get(1.0, END).strip():
        text2.delete(1.0, END)

# Icon on top
image_icon = PhotoImage(file= r"img/Logo.png")
root.iconphoto(False, image_icon)

# Arrow
arrow_img = PhotoImage(file="img/arrow.png")
image_label = Label(root, image=arrow_img, width=150)
image_label.place(x=460, y=50)

# Define languages
language = {
    "english": "en",
    "portuguese": "pt",
    "spanish": "es",
    "french": "fr",
    "german": "de"
    # Adicione mais idiomas conforme necessário
}
languageV = list(language.keys())

# Left side language selection
combo1 = ttk.Combobox(root, values=languageV, font='Roboto 14', state='r')
combo1.place(x=110, y=20)
combo1.set("english")

# Label for original language
label1 = Label(root, text="English", font='segoe 30 bold', bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

# Text input frame
f = Frame(root, bg="black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)
text1.bind("<KeyRelease>", clear_output)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Right side language selection
combo2 = ttk.Combobox(root, values=languageV, font='Roboto 14', state='r')
combo2.place(x=730, y=20)
combo2.set("portuguese")

# Label for translated language
label2 = Label(root, text="Portuguese", font='segoe 30 bold', bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

# Text output frame
f1 = Frame(root, bg="black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate button
translate = Button(root, text="Translate", font="Roboto 15 bold italic", activebackground="purple", cursor="hand2", bd=5, bg="red", fg="white", command=translate_now)
translate.place(x=480, y=250)

label_change()

root.configure(bg="white")
root.mainloop()
