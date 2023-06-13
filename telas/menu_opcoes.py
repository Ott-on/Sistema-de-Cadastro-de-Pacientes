import tkinter as tk
from tkinter import RAISED, RIDGE, Button, Entry, Label, PhotoImage, messagebox


class MenuOpcoes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#242323')

        label_retangulo = Label(self, width=1000, height=5, bg='#02bae8')
        label_retangulo.place(x=0, y=0)

        #botão voltar
        botao_voltar = Button(self, text='Voltar', width=10, height=1, font=(
            "Arial", 30), bg='#02bae8',fg='white', relief='solid', overrelief='solid',borderwidth=0, highlightthickness=0)
        botao_voltar.place(x=5, y=5)
        
    def paciente(self):

        pass

    def doença(self):

        pass
    
    def relatório(self):
        
        pass
    


