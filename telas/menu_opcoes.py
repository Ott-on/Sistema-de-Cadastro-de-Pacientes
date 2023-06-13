import tkinter as tk
from tkinter import RAISED, RIDGE, Button, Entry, Label, PhotoImage, messagebox


class MenuOpcoes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#242323')
        imagem = tk.PhotoImage(file="imagens/voltar_label.png")

        label_retangulo = Label(self, width=1000, height=5, bg='#02bae8')
        label_retangulo.place(x=0, y=0)

        #botão voltar
        img = PhotoImage(file='imagens/voltar_label.png')
        button_image = Button(self, image=img, bg='#02bae8', fg='#02bae8', relief='solid', overrelief='solid',borderwidth=0, highlightthickness=0)
        button_image.image = img
        button_image.place(x=10, y=20)
           
        


