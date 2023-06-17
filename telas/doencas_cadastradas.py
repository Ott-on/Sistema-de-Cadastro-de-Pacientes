import tkinter as tk
from tkinter import RAISED, RIDGE, Button, Entry, Label, PhotoImage, messagebox
from modelos.sistema_doencas import *


class Doenca(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#242323')

        # retangulo azul da tela
        label_retangulo = Label(self, width=1000, height=4, bg='#02bae8')
        label_retangulo.place(x=0, y=0)

        # botão pesquisar:
        img2 = PhotoImage(file='imagens/pesquisar.png')
        button_image = Button(self, image=img2, bg='#02bae8', fg='#02bae8', activebackground='#02bae8', command=lambda: self.pesquisar(controller),
                              relief='solid', overrelief='solid', borderwidth=0, highlightthickness=0)
        button_image.image = img2
        button_image.place(x=920, y=10)

        # entrada da pesquisa:
        entrada_pesquisa = Entry(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0, relief='solid')
        entrada_pesquisa.place(x=720, y=10)

        self.entrada_pesquisa = entrada_pesquisa

        # mostrar paciente
        label_doenca = Label(
            Label(self, text='', width=20, height=4, bg='white'))
        label_doenca.grid(row=1, column=0)

        self.label_doenca = label_doenca
        # botão voltar
        img = PhotoImage(file='imagens/voltar_label.png')
        button_image = Button(self, image=img, bg='#02bae8', fg='#02bae8', activebackground='#02bae8', command=lambda: self.voltar_menu(
            controller), relief='solid', overrelief='solid', borderwidth=0, highlightthickness=0)
        button_image.image = img
        button_image.place(x=10, y=10)

        # botão cadastrar:
        button_cadastrar = Button(self, text='CADASTRAR DOENÇA', font=("Arial", 16), activebackground='#02bae8', bg='#02bae8', fg='white', command=lambda: self.cadastrar_doencas(
            controller), relief='solid', overrelief='solid', width=20, height=2, borderwidth=0, highlightthickness=0)
        button_cadastrar.place(x=90, y=2)

    def voltar_menu(self, controller):
        from telas.menu_opcoes import MenuOpcoes
        controller.show_frame(MenuOpcoes)

    def pesquisar(self, controller):
        from modelos.sistema_doencas import SistemaDoenca

        doenca_selecionada = self.entrada_pesquisa.get()

        self.sistema_doencas = SistemaDoenca()
        doenca = self.sistema_doencas.consultar(
            doenca_selecionada=doenca_selecionada)

    def cadastrar_doencas(self, controller):
        from telas.cadastro_doenca import cadastrarDoencas
        controller.show_frame(cadastrarDoencas)

    def fazer_login(self):
        nome = self.entrada_nome.get()
        cid = self.entrada_cid.get()

        # Aqui verificamos se os campos foram preenchidos caso não deve mostrar um erro pedindo para preencher os campos
        if nome.isalpha() and cid.isalpha():
            print('ok')
            SistemaDoenca(nome, cid)

        else:
            # Aqui exibimos um popup de aviso pedindo para os campos serem preenchidos
            messagebox.showinfo(
                "Aviso!", "Preencha os campos para continuar", icon="warning")
