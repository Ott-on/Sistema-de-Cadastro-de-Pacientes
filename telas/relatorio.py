import tkinter as tk
from tkinter import RAISED, RIDGE, Button, Entry, Label, PhotoImage, messagebox
from modelos.paciente import *


class Relatorio(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#242323')

        #retangulo azul da tela
        label_retangulo = Label(self, width=1000, height=4, bg='#02bae8')
        label_retangulo.place(x=0, y=0)

        # Nome
        entrada_nome = Entry(self,width=14, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_nome.place(x=60, y=450)

        self.entrada_nome = entrada_nome

        # CPF
        entrada_cpf = Entry(self,width=14, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_cpf.place(x=160, y=450)

        self.entrada_cpf = entrada_cpf

        # Email
        entrada_email = Entry(self,width=14, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_email.place(x=260, y=450)

        self.entrada_email = entrada_email

        # Celular
        entrada_celular = Entry(self,width=14, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_celular.place(x=360, y=450)

        self.entrada_celular = entrada_celular

        # Telefone
        entrada_telefone = Entry(self,width=14, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_telefone.place(x=460, y=450)

        self.entrada_telefone = entrada_telefone

        # Data de Nascimento
        
        # Sexo
        entrada_sexo = Entry(self,width=14, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_sexo.place(x=560, y=450)

        self.entrada_sexo = entrada_sexo

        # Estado Civil
        entrada_civil = Entry(self,width=14, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_civil.place(x=660, y=450)

        self.entrada_civil = entrada_civil
        img = PhotoImage(file='imagens/voltar_label.png')
        button_image = Button(self, image=img, bg='#02bae8', fg='#02bae8', activebackground='#02bae8', command=lambda: self.voltar_menu(
            controller), relief='solid', overrelief='solid', borderwidth=0, highlightthickness=0)
        button_image.image = img
        button_image.place(x=10, y=10)  

    def voltar_menu(self, controller):
        from telas.menu_opcoes import MenuOpcoes
        controller.show_frame(MenuOpcoes)
        
    def fazer_cadastro(self):
        nome = self.entrada_nome.get()
        cpf = self.entrada_cpf.get()
        email = self.entrada_email.get()
        telefone = self.entrada_telefone.get()
        celular = self.entrada.celular.get()
        nascimento = self.entrada_nascimento.get()
        sexo = self.entrada_sexo.get()
        civil = self.entrada_civil.get()

        # Aqui verificamos se os campos foram preenchidos caso não deve mostrar um erro pedindo para preencher os campos
        if cpf.isdigit() and len(cpf) == 11 and telefone.isalpha() and celular.isalpha() and len(nascimento) != 0 and sexo.isalpha() and civil.isalpha():
            print('ok')
            Paciente(nome, cpf, email, telefone, celular, nascimento, sexo, civil)

        else:
            # Aqui exibimos um popup de aviso pedindo para os campos serem preenchidos
            messagebox.showinfo(
                "Aviso!", "Preencha os campos para continuar", icon="warning")
