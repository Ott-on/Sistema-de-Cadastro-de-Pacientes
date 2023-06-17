import tkinter as tk
from tkinter import RAISED, RIDGE, Button, Entry, Label, PhotoImage, messagebox
from modelos.paciente import *


class Pacientes(tk.Frame):
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
        label_paciente = Label(self, text='', width=30, height=8, bg='white')
        label_paciente.grid(row=1, column=0)

        label_paciente.place(x=10, y=100)

        self.label_paciente = label_paciente

        # botão voltar
        img = PhotoImage(file='imagens/voltar_label.png')
        button_image = Button(self, image=img, bg='#02bae8', fg='#02bae8', activebackground='#02bae8', command=lambda: self.voltar_menu(
            controller), relief='solid', overrelief='solid', borderwidth=0, highlightthickness=0)
        button_image.image = img
        button_image.place(x=10, y=10)

        # botão cadastrar:
        button_cadastrar = Button(self, text='CADASTRAR', font=("Arial", 16), activebackground='#02bae8', bg='#02bae8', fg='white', command=lambda: self.cadastrar_pacientes(
            controller), relief='solid', overrelief='solid', width=10, height=2, borderwidth=0, highlightthickness=0)
        button_cadastrar.place(x=100, y=2)

    def pesquisar(self, controller):
        from modelos.sistema_pacientes import SistemaPacientes

        paciente_selecionado = self.entrada_pesquisa.get()

        self.sistema_pacientes = SistemaPacientes()
        paciente = self.sistema_pacientes.consultar_paciente(
            paciente_selecionado=paciente_selecionado)

        if paciente:
            # Atualizar o texto do label_paciente com os dados do paciente encontrado
            self.label_paciente.config(
                text=f"Nome: {paciente['nome']}\nCpf: {paciente['cpf']}\nEmail: {paciente['email']}\nTelefone: {paciente['telefone']}\nCelular: {paciente['celular']}\nData_mascimento: {paciente['data_nascimento']}\nSexo: {paciente['sexo']}\nEstado_civil: {paciente['estado_civil']}", justify='left', anchor='w')

        else:
            self.label_paciente.config(
                text="Paciente não encontrado", anchor='center')

    def voltar_menu(self, controller):
        from telas.menu_opcoes import MenuOpcoes
        controller.show_frame(MenuOpcoes)

    def cadastrar_pacientes(self, controller):
        from telas.paciente_cadastro import cadastrarPacientes
        controller.show_frame(cadastrarPacientes)
