import tkinter as tk
from tkinter import RAISED, RIDGE, Button, Entry, Label, PhotoImage, Scrollbar, messagebox
from tkinter.ttk import Treeview
from modelos.paciente import *
from modelos.sistema_pacientes import SistemaPacientes


class Pacientes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#242323')

        print("pacientes=============>")

        sistema_pacientes = SistemaPacientes()
        self.pacientes = sistema_pacientes.obter_pacientes()

        # Criar a barra de rolagem
        scrollbar = tk.Scrollbar(self)
        scrollbar.place(x=972, y=150, height=446)

        # retangulo azul da tela
        label_retangulo = Label(self, width=1000, height=4, bg='#02bae8')
        label_retangulo.place(x=0, y=0)

        # botão pesquisar:
        img2 = PhotoImage(file='imagens/pesquisar.png')
        print(self.pacientes)
        button_image = Button(self, image=img2, bg='#02bae8', fg='#02bae8', activebackground='#02bae8', command=lambda: self.pesquisar(sistema_pacientes, controller),
                              relief='solid', overrelief='solid', borderwidth=0, highlightthickness=0)
        button_image.image = img2
        button_image.place(x=920, y=10)

        # entrada da pesquisa:
        entrada_pesquisa = Entry(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0, relief='solid')
        entrada_pesquisa.place(x=720, y=10)

        # Adicionando um ouvinte de evento que quando digitamos algo chama essa função
        entrada_pesquisa.bind(
            '<KeyRelease>', lambda event: self.__verificar_campo_pesquisa())

        self.entrada_pesquisa = entrada_pesquisa

        img = PhotoImage(file='imagens/voltar_label.png')
        button_image = Button(self, image=img, bg='#02bae8', fg='#02bae8', activebackground='#02bae8', command=lambda: self.voltar_menu(
            controller), relief='solid', overrelief='solid', borderwidth=0, highlightthickness=0)
        button_image.image = img
        button_image.place(x=10, y=10)

        # botão cadastrar:
        button_cadastrar = Button(self, text='CADASTRAR', font=("Arial", 16), activebackground='#02bae8', bg='#02bae8', fg='white', command=lambda: self.cadastrar_pacientes(
            controller), relief='solid', overrelief='solid', width=10, height=2, borderwidth=0, highlightthickness=0)
        button_cadastrar.place(x=100, y=2)

        label_selecionar_paciente = Label(self, width=26, height=2, text='Selecione e escolhar alguma ação:', font=(
            "Arial", 18), bg='#242323', fg='#888a89')
        label_selecionar_paciente.place(x=10, y=80)

        self.treeview = Treeview(self, columns=(
            "CPF", "Nome", "Email", "Telefone", "Celular", "Data_Nascimento", "Sexo", "Estado_Civil"), height=21,  show="headings")

        self.treeview.column("CPF", width=100)
        self.treeview.column("Email", width=150)
        self.treeview.column("Telefone", width=120)
        self.treeview.column("Celular", width=110)
        self.treeview.column("Data_Nascimento", width=120)
        self.treeview.column("Estado_Civil", width=80)
        self.treeview.column("Sexo", width=80)

        # Definir as colunas
        self.treeview.heading("CPF", text="CPF")
        self.treeview.heading("Nome", text="Nome")
        self.treeview.heading("Email", text="Email")
        self.treeview.heading("Telefone", text="Telefone")
        self.treeview.heading("Celular", text="Celular")
        self.treeview.heading("Data_Nascimento", text="Data de Nascimento")
        self.treeview.heading("Sexo", text="Sexo")
        self.treeview.heading("Estado_Civil", text="Estado Civil")

        self.treeview.place(x=10, y=150)

        for dado in self.pacientes:
            self.treeview.insert("", "end", values=dado)

        self.treeview.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.treeview.yview)

        def atender():
            # Lógica para atender
            selected_item = self.treeview.selection()
            if selected_item:
                item = self.treeview.item(selected_item)
                print("Atender:", item["values"])

        def alterar():
            # Lógica para alterar
            selected_item = self.treeview.selection()
            if selected_item:
                item = self.treeview.item(selected_item)
                print("Alterar:", item["values"])

        def excluir():
            # Lógica para excluir
            selected_item = self.treeview.selection()
            if selected_item:
                item = self.treeview.item(selected_item)
                print("Excluir:", item["values"])

        frame = tk.Frame(self)
        frame.place(x=400, y=95)

        botao_atender = tk.Button(frame, text="Atender", command=atender)
        botao_atender.pack(side="left", padx=2, pady=2)

        botao_consultar = tk.Button(frame, text="Consultar", command=atender)
        botao_consultar.pack(side="left", padx=2, pady=2)

        botao_alterar = tk.Button(frame, text="Alterar", command=alterar)
        botao_alterar.pack(side="left", padx=2, pady=2)

        botao_excluir = tk.Button(frame, text="Excluir", command=excluir)
        botao_excluir.pack(side="left", padx=2, pady=2)

    # função que verifica se o campo de pesquisa esta vazio caso esteja ele carrega todos os pacientes
    def __verificar_campo_pesquisa(self):
        if len(self.entrada_pesquisa.get()) == 0:
            self.treeview.delete(*self.treeview.get_children())
            for dado in self.pacientes:
                self.treeview.insert("", "end", values=dado)

    def pesquisar(self, sistema_pacientes: SistemaPacientes, controller):

        paciente_selecionado = self.entrada_pesquisa.get()

        pacientes_encontrados = sistema_pacientes.consultar(
            buscador=paciente_selecionado)

        if pacientes_encontrados:
            self.treeview.delete(*self.treeview.get_children())
            for dado in pacientes_encontrados:
                self.treeview.insert("", "end", values=dado)
        else:
            self.treeview.delete(*self.treeview.get_children())
            messagebox.showinfo(
                "Aviso!", "Paciente não encontrado!", icon="warning")

    def voltar_menu(self, controller):
        from telas.menu_opcoes import MenuOpcoes
        controller.show_frame(MenuOpcoes)

    def cadastrar_pacientes(self, controller):
        from telas.paciente_cadastro import cadastrarPacientes
        controller.show_frame(cadastrarPacientes)
