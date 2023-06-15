import tkinter as tk
from tkinter import RAISED, RIDGE, Button, Entry, Label, PhotoImage, messagebox
from modelos.paciente import *


class Pacientes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#242323')
        
        #retangulo azul da tela
        label_retangulo = Label(self, width=1000, height=4, bg='#02bae8')
        label_retangulo.place(x=0, y=0)

        #botão voltar
        img = PhotoImage(file='imagens/voltar_label.png')
        button_image = Button(self, image=img, bg='#02bae8', fg='#02bae8', activebackground='#02bae8', command=lambda: self.voltar_menu(
            controller), relief='solid', overrelief='solid', borderwidth=0, highlightthickness=0)
        button_image.image = img
        button_image.place(x=10, y=10)
    
        # botão cadastrar
        button_cadastrar = Button(self, text='CADASTRAR', font=("Arial", 16), activebackground='#02bae8', bg='#02bae8', fg='white', command=lambda: self.cadastrar_pacientes(controller), relief='solid', overrelief='solid', width=10, height=2, borderwidth=0, highlightthickness=0)
        button_cadastrar.place(x=100, y=2)


    def voltar_menu(self, controller):
        from telas.menu_opcoes import MenuOpcoes
        controller.show_frame(MenuOpcoes)

    def cadastrar_pacientes(self,controller):
        from telas.tela_paciente_cadastro import cadastrarPacientes
        controller.show_frame(cadastrarPacientes)


            
