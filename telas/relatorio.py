# importações das bibliotecas usadas na tela de relatorio
import tkinter as tk
from tkinter import Button, Entry, Label, PhotoImage, messagebox
from modelos.paciente import *
from tkinter.ttk import Treeview
from tkcalendar import DateEntry

from modelos.sistema_relatorio import SistemaRelatorios


class Relatorio(tk.Frame):
    def __init__(self, parent, controller):
        """
        Construtor da classe Relatorio.
        """
        tk.Frame.__init__(self, parent)
        self.configure(bg='#242323')

        print('ded')

        sistema_relatorio = SistemaRelatorios()
        self.todos_atendimentos = sistema_relatorio.obter_todos_atendimentos()

        # Criar a barra de rolagem
        scrollbar = tk.Scrollbar(self)
        scrollbar.place(x=972, y=150, height=446)

        # retangulo azul da tela
        label_retangulo = Label(self, width=1000, height=4, bg='#02bae8')
        label_retangulo.place(x=0, y=0)

        # botão pesquisar:
        img2 = PhotoImage(file='imagens/pesquisar.png')
        button_image = Button(self, image=img2, bg='#02bae8', fg='#02bae8', activebackground='#02bae8',
                              command=lambda: self.pesquisar(
                                  sistema_relatorio),
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

        '''
        Essas linhas atribuem os objetos de entrada de dados (entrada_nascimento, 
        entrada_cid e entrada_pesquisa) aos atributos correspondentes da instância atual 
        da classe Relatorio (self.entrada_nascimento, self.entrada_cid e self.entrada_pesquisa). 
        Isso permite acessar esses objetos posteriormente em outros métodos da classe, 
        garantindo que as informações inseridas pelo usuário possam ser utilizadas quando necessário.
        '''
        self.entrada_nascimento = entrada_nascimento
        self.entrada_cid = entrada_cid
        self.entrada_pesquisa = entrada_pesquisa

        # Adicionando um ouvinte de evento que quando digitamos algo chama essa função
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

        # CPF | Data de Atendimento | codigo CID | Nome

        self.treeview = Treeview(self, columns=(
            "CPF", "Data_Atendimento", "Código_CID", "Nome",), height=21,
            show="headings")

        self.treeview.column("CPF", width=200)
        self.treeview.column("Data_Atendimento", width=250)
        self.treeview.column("Código_CID", width=230)
        self.treeview.column("Nome", width=280)

        # Definir as colunas
        self.treeview.heading("CPF", text="CPF")
        self.treeview.heading("Data_Atendimento", text="Data de Atendimento")
        self.treeview.heading("Código_CID", text="Código CID")
        self.treeview.heading("Nome", text="Nome do Paciente")

        self.treeview.place(x=10, y=150)

        for dado in self.todos_atendimentos:
            self.treeview.insert("", "end", values=dado)

        self.treeview.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.treeview.yview)

    def __verificar_campo_pesquisa(self):
        """
        Verifica se os campos de pesquisa estão vazios e exibe todos os registros de atendimento se for o caso.
        """
        if len(self.entrada_cid.get()) == 0 and len(self.entrada_pesquisa.get()) == 0:
            self.treeview.delete(*self.treeview.get_children())
            for dado in self.todos_atendimentos:
                self.treeview.insert("", "end", values=dado)

    def pesquisar(self, sistema_relatorio: SistemaRelatorios):
        """
        Realiza a pesquisa com base nos critérios fornecidos e exibe os resultados na Treeview.
        :param sistema_relatorio: Instância do objeto SistemaRelatorios.
        :param controller: Objeto do controlador da GUI.
        """
        # Obtendo os valores selecionados
        periodo_selecionado = self.entrada_nascimento.get()
        codigo_cid = self.entrada_cid.get()
        paciente_cpf_ou_nome = self.entrada_pesquisa.get()

        resultado = []

        # verificando qual está preenchido
        if periodo_selecionado and not codigo_cid and not paciente_cpf_ou_nome:
            resultado = sistema_relatorio.listar_atendimentos_pelo_calendario(
                dia_mes_ano=periodo_selecionado)
        else:
            if codigo_cid and not paciente_cpf_ou_nome:
                resultado = sistema_relatorio.listar_atendimentos_pelo_codigo_cid(
                    codigo_cid=codigo_cid)
            else:
                resultado = sistema_relatorio.listar_atendimentos_pelo_nome_ou_cpf(
                    nome_ou_cpf=paciente_cpf_ou_nome)

        # Limpar a Treeview antes de exibir os resultados
        self.treeview.delete(*self.treeview.get_children())

        # Exibir os resultados na Treeview, se houver
        if resultado:
            for dado in resultado:
                self.treeview.insert("", "end", values=dado)
        else:
            # Exibir todos os registros de atendimento se nenhum resultado for encontrado
            for dado in self.todos_atendimentos:
                self.treeview.insert("", "end", values=dado)
            messagebox.showinfo(
                "Aviso!",
                "O sistema não identificou nenhum registro de atendimento com base nas informações fornecidas. "
                "Por favor, verifique os dados inseridos e tente novamente.",
                icon="warning"
            )

    def voltar_menu(self, controller):
        """
        Retorna ao menu de opções.
        :param controller: Objeto do controlador da GUI.
        """
        from telas.menu_opcoes import MenuOpcoes
        controller.show_frame(MenuOpcoes)
