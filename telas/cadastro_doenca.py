import tkinter as tk
from tkcalendar import DateEntry
from tkinter import END, RAISED, RIDGE, Button, Entry, Label, PhotoImage, messagebox
from modelos.paciente import *
from tkinter import ttk


class cadastrarDoencas(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#242323')

        # retangulo azul da tela
        label_retangulo = Label(self, width=1000, height=4, bg='#02bae8')
        label_retangulo.place(x=0, y=0)
        
        # Nome
        entrada_nome = Entry(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_nome.place(x=160, y=190)
        label_nome = Label(self, width=10, height=2, text='Nome:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_nome.place(x=145, y=150)

        self.entrada_nome = entrada_nome

        # cid
        entrada_cid = Entry(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_cid.place(x=160, y=340)
        label_cid = Label(self, width=10, height=2, text='CID:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_cid.place(x=140, y=300)

        self.entrada_cid = entrada_cid 

        #botão voltar
        img = PhotoImage(file='imagens/voltar_label.png')
        button_image = Button(self, image=img, bg='#02bae8', fg='#02bae8', activebackground='#02bae8', command=lambda: self.voltar_menu(
            controller), relief='solid', overrelief='solid', borderwidth=0, highlightthickness=0)
        button_image.image = img
        button_image.place(x=10, y=10)  

        #botão cadastrar
        button_cadastrar = Button(self, text='Confirmar', font=("Arial", 16), activebackground='#02bae8', bg='#02bae8', fg='white', command=lambda: self.fazer_cadastro(
            controller), relief='solid', overrelief='solid', width=10, height=2, borderwidth=0, highlightthickness=0)
        button_cadastrar.place(x=180, y=450)

    def voltar_menu(self, controller):
        from telas.menu_opcoes import MenuOpcoes
        controller.show_frame(MenuOpcoes)

    def fazer_cadastro(self, controller):
        from modelos.sistema_doencas import SistemaDoenca

        nome = self.entrada_nome.get()
        cid = self.entrada_cid.get()
    
        self.sistema_doencas = SistemaDoenca()
        resultado = self.sistema_doencas.cadastrar(nome=nome, cid=cid)
