import tkinter as tk
from tkinter import RAISED, RIDGE, Button, Entry, Label, PhotoImage, messagebox


class MenuOpcoes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')

        label_retangulo = Label(self, width=1000, height=5, bg='#02bae8')
        label_retangulo.place(x=0, y=0)

        img2 = PhotoImage(file='imagens/menu1.png')
        button_image = Label(self, image=img2, bg='#02bae8', fg='#02bae8', relief='solid',borderwidth=0, highlightthickness=0)
        button_image.image = img2
        button_image.place(x=100, y=120)

        #botão sair
        import tkinter as tk
from tkinter import RAISED, RIDGE, Button, Entry, Label, PhotoImage, messagebox


class MenuOpcoes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')

        label_retangulo = Label(self, width=1000, height=5, bg='#02bae8')
        label_retangulo.place(x=0, y=0)

        img2 = PhotoImage(file='imagens/menu1.png')
        button_image = Label(self, image=img2, bg='#02bae8', fg='#02bae8', relief='solid',borderwidth=0, highlightthickness=0)
        button_image.image = img2
        button_image.place(x=100, y=120)

        #botão sair
        button_sair = Button(self, text='SAIR',font=(
            "Arial", 20), bg='#02bae8', fg='white', relief='solid', overrelief='solid',width=10, height=2, borderwidth=0, highlightthickness=0)
        button_sair.place(x=850, y=-2)
           
        #botão paciente:
        button_paciente = Button(self, bg='#02bae8', fg='white',relief=RAISED ,overrelief=RAISED, text='Paciente', width=10, height=2, font=(
            "Arial", 20))
        button_paciente.place(x=100,y=470)
        #botão doença:
        button_doenca = Button(self, bg='#02bae8', fg='white', relief=RAISED, overrelief=RAISED, text='Doenças', width=10, height=2, font=(
            "Arial", 20)) 
        button_doenca.place(x=410,y=470)
        #botão relatório:
        button_relatorio = Button(self, bg='#02bae8', fg='white', relief=RAISED, overrelief=RAISED, text='Relatório', width=10, height=2, font=(
            "Arial", 20))
        button_relatorio.place(x=730,y=470)
           
        


