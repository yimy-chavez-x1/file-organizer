import customtkinter as ctk
from organizer import organizar_descargas
from tkinter import messagebox

app = ctk.CTk()
app.title("File Organizer")
app.geometry("400x300")

def organizar_y_avisar():
    organizar_descargas()
    messagebox.showinfo("Listo", "Carpeta organizada mi loco")

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

boton = ctk.CTkButton(app, text="Organizar Descargas", command=organizar_y_avisar)
boton.grid(row=0, column=0)


app.mainloop()

