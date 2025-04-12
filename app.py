from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

root = Tk()
root.title("Translator")
root.geometry("1150x500")  
root.config(bg="#f2f2f2")  

translator = Translator()

#translation function
def translate_fun():
    try:
        text_ = text1.get(1.0, END).strip()  # Get input text
        cb1 = c1.get()  #source language
        cb2 = c2.get()  #destination language

        if not text_:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        #detecting source lang as default english
        from_lang_code = "en"
        for code, lang in language.items():
            if lang == cb1:
                from_lang_code = code
                break

        #detecting destination language
        to_lang_code = None
        for code, lang in language.items():
            if lang == cb2:
                to_lang_code = code
                break

        if not to_lang_code:
            messagebox.showerror("Language Error", "Target language not found.")
            return

        
        translated_text = translator.translate(text_, src=from_lang_code, dest=to_lang_code).text
        text2.delete(1.0, END)
        text2.insert(END, translated_text)

    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")

#logo and pic

try:
    logo = PhotoImage(file="./assests/malogo.png")
    root.iconphoto(False, logo)
except Exception as e:
    print(f"Error loading logo: {e}")

try:
    arrow = PhotoImage(file="./assests/arrow.png")
    img = Label(root, image=arrow, bg="#f2f2f2")
    img.place(x=505, y=180)
except Exception as e:
    print(f"Error loading arrow image: {e}")
####################

language = LANGUAGES
valeurs = list(language.values())

#source language by default english
Label(root, text="Source Language", font="Calibri 14", bg="#f2f2f2").place(x=100, y=50)
c1 = ttk.Combobox(root, values=valeurs, font="Calibri 14", state="readonly")
c1.place(x=100, y=80, width=300)
c1.set("English")  

#input text source
Label(root, text="Input Text", font="Calibri 14", bg="#f2f2f2").place(x=100, y=120)
f1 = Frame(root, bg="#ffffff", bd=2, relief=SOLID)
f1.place(x=100, y=150, width=350, height=200)
text1 = Text(f1, font="Calibri 14", bg="white", relief=FLAT, wrap=WORD)
text1.place(x=0, y=0, width=340, height=190)

scrollbar1 = Scrollbar(f1)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#destination language
Label(root, text="Target Language", font="Calibri 14", bg="#f2f2f2").place(x=700, y=50)
c2 = ttk.Combobox(root, values=valeurs, font="Calibri 14", state="readonly")
c2.place(x=700, y=80, width=300)
c2.set("Select language")  # Default target language

#output text destination
Label(root, text="Translated Text", font="Calibri 14", bg="#f2f2f2").place(x=700, y=120)
f2 = Frame(root, bg="#ffffff", bd=2, relief=SOLID)
f2.place(x=700, y=150, width=350, height=200)
text2 = Text(f2, font="Calibri 14", bg="white", relief=FLAT, wrap=WORD)
text2.place(x=0, y=0, width=340, height=190)

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

#the translate button 
translate = Button(root, text="Translate", font="Calibri 16 bold", cursor="hand2", 
                   bg="#4caf50", fg="white", activebackground="#45a049", activeforeground="white", 
                   command=translate_fun)
translate.place(x=510, y=350, width=120, height=40)

root.mainloop()
