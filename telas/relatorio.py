import tkinter as tk
from tkinter import RAISED, RIDGE, Button, Entry, Label, PhotoImage, messagebox
from modelos.paciente import *
from modelos.sistema_pacientes import SistemaPacientes
from tkinter.ttk import Treeview
from tkcalendar import DateEntry
import datetime

class Relatorio(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#242323')

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
        button_image = Button(self, image=img2, bg='#02bae8', fg='#02bae8', activebackground='#02bae8',
                              command=lambda: self.pesquisar(sistema_pacientes, controller),
                              relief='solid', overrelief='solid', borderwidth=0, highlightthickness=0)
        button_image.image = img2
        button_image.place(x=920, y=10)

        # entrada da pesquisa por dia ou periodo informado:
        label_nascimento = Label(self, width=15, height=2, text='Dia:', font=(
            "Arial", 10), bg='#02bae8', fg='#242323')
        label_nascimento.place(x=110, y=6)

        entrada_nascimento = DateEntry(self, width=12, background='#02bae8',
                                       foreground='white', borderwidth=2, locale='pt_BR', date_pattern="dd/mm/yyyy")
        entrada_nascimento.place(x=120, y=40)

        self.entrada_nascimento = entrada_nascimento

        # Colocando para começar em 30 01 1995 o DateEntry
        data_padrao = datetime.date(1995, 1, 30)
        self.entrada_nascimento.set_date(data_padrao)

        # entrada da pesquisa por código CID:
        label_cid = Label(self, width=15, height=2, text='Código CID:', font=(
            "Arial", 10), bg='#02bae8', fg='#242323')
        label_cid.place(x=310, y=12)

        entrada_cid = Entry(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0, relief='solid')
        entrada_cid.place(x=420, y=10)

        # entrada da pesquisa por nome/cpf:
        label_nome_cpf = Label(self, width=15, height=2, text='Nome/CPF:', font=(
            "Arial", 10), bg='#02bae8', fg='#242323')
        label_nome_cpf.place(x=615, y=12)

        entrada_pesquisa = Entry(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0, relief='solid')
        entrada_pesquisa.place(x=720, y=10)

        # Adicionando um ouvinte de evento que quando digitamos algo chama essa função

        self.entrada_nascimento = entrada_nascimento
        self.entrada_cid = entrada_cid
        self.entrada_pesquisa = entrada_pesquisa

        entrada_nascimento.bind(
            '<KeyRelease>', lambda event: self.__verificar_campo_pesquisa())
        entrada_cid.bind(
            '<KeyRelease>', lambda event: self.__verificar_campo_pesquisa())
        entrada_pesquisa.bind(
            '<KeyRelease>', lambda event: self.__verificar_campo_pesquisa())
        

        # Voltar
        img = PhotoImage(file='imagens/voltar_label.png')
        button_image = Button(self, image=img, bg='#02bae8', fg='#02bae8', activebackground='#02bae8',
                              command=lambda: self.voltar_menu(
                                  controller), relief='solid', overrelief='solid', borderwidth=0, highlightthickness=0)
        button_image.image = img
        button_image.place(x=10, y=10)


        # Texto de título da página relatório
        label_selecionar_paciente = Label(self, width=30, height=2, text='Relatório dos pacientes classificados:', font=(
            "Arial", 18), bg='#242323', fg='#888a89')
        label_selecionar_paciente.place(x=10, y=80)

        self.treeview = Treeview(self, columns=(
            "CPF", "Nome", "Email", "Telefone", "Celular", "Data_Nascimento", "Sexo", "Estado_Civil"), height=21,
                                 show="headings")
        
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

    # função que verifica se o campo de pesquisa esta vazio caso esteja ele carrega todos os pacientes

    def __verificar_campo_pesquisa(self):
        if len(self.entrada_nascimento.get()) == 0 and len(self.entrada_cid.get()) == 0 and len(self.entrada_pesquisa.get()) == 0:
            self.treeview.delete(*self.treeview.get_children())
            for dado in self.pacientes:
                self.treeview.insert("", "end", values=dado)
        
    def pesquisar(self, sistema_pacientes: SistemaPacientes, controller):

        # Obtendo os valores selecionados
        periodo_selecionado = self.entrada_nascimento.get()
        doenca_selecionado = self.entrada_cid.get()
        paciente_selecionado = self.entrada_pesquisa.get()

        # Criando um dicionário com os critérios de busca
        buscador = {
            'periodo': periodo_selecionado,
            'doenca': doenca_selecionado,
            'paciente': paciente_selecionado
        }

        # Chamando o método consultar do sistema de pacientes com o buscador
        pacientes_encontrados = sistema_pacientes.consultar(buscador=buscador)

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