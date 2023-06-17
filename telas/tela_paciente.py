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
        pacientes = sistema_pacientes.obter_pacientes()
        print(pacientes)

        # Criar a barra de rolagem
        scrollbar = tk.Scrollbar(self)
        scrollbar.place(x=950, y=80)

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

        treeview = Treeview(self, columns=(
            "CPF", "Nome", "Email", "Telefone", "Celular", "Data_Nascimento", "Sexo", "Estado_Civil"), height=21,  show="headings")

        treeview.column("CPF", width=100)
        treeview.column("Telefone", width=100)
        treeview.column("Celular", width=100)
        treeview.column("Data_Nascimento", width=120)
        treeview.column("Estado_Civil", width=80)
        treeview.column("Sexo", width=50)

        # Definir as colunas
        treeview.heading("CPF", text="CPF")
        treeview.heading("Nome", text="Nome")
        treeview.heading("Email", text="Email")
        treeview.heading("Telefone", text="Telefone")
        treeview.heading("Celular", text="Celular")
        treeview.heading("Data_Nascimento", text="Data de Nascimento")
        treeview.heading("Sexo", text="Sexo")
        treeview.heading("Estado_Civil", text="Estado Civil")

        treeview.place(x=10, y=150)

        # Adicionar dados de exemplo
        dados = [
            ("João", 25, "123.456.789-01"),
            ("Maria", 30, "987.654.321-09"),
            ("Pedro", 40, "456.789.123-45"),
        ]

        for dado in pacientes:
            print(dado)
            treeview.insert("", "end", values=dado)

        treeview.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=treeview.yview)

        # Posicionar o Treeview na janela
        # treeview.pack(side="left", fill="both", expand=False)

        # Adicionar botões de ação

        def atender():
            # Lógica para atender
            selected_item = treeview.selection()
            if selected_item:
                item = treeview.item(selected_item)
                print("Atender:", item["values"])

        def alterar():
            # Lógica para alterar
            selected_item = treeview.selection()
            if selected_item:
                item = treeview.item(selected_item)
                print("Alterar:", item["values"])

        def excluir():
            # Lógica para excluir
            selected_item = treeview.selection()
            if selected_item:
                item = treeview.item(selected_item)
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

    def pesquisar(self, controller):
        from modelos.sistema_pacientes import SistemaPacientes

        paciente_selecionado = self.entrada_pesquisa.get()

        self.sistema_pacientes = SistemaPacientes()
        paciente = self.sistema_pacientes.consultar(
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
