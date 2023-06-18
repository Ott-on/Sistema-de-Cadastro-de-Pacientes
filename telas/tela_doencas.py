import tkinter as tk
from tkinter import RAISED, RIDGE, Button, Entry, Label, PhotoImage, Scrollbar, messagebox
from tkinter.ttk import Treeview
from modelos.paciente import *
from modelos.sistema_doencas import SistemaDoenca
from modelos.sistema_pacientes import SistemaPacientes


class DoencasListagem(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#242323')

        sistema_doenca = SistemaDoenca()
        self.doencas_obtidas = sistema_doenca.obter_doencas()

        # Criar a barra de rolagem
        scrollbar = tk.Scrollbar(self)
        scrollbar.place(x=972, y=150, height=446)

        # retangulo azul da tela
        label_retangulo = Label(self, width=1000, height=4, bg='#02bae8')
        label_retangulo.place(x=0, y=0)

        # botão pesquisar:
        img2 = PhotoImage(file='imagens/pesquisar.png')
        button_image = Button(self, image=img2, bg='#02bae8', fg='#02bae8', activebackground='#02bae8', command=lambda: self.pesquisar(sistema_doenca, controller),
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
        button_cadastrar = Button(self, text='CADASTRAR DOENÇA', font=("Arial", 16), activebackground='#02bae8', bg='#02bae8', fg='white', command=lambda: self.cadastrar_doencas(
            controller), relief='solid', overrelief='solid', width=20, height=2, borderwidth=0, highlightthickness=0)
        button_cadastrar.place(x=100, y=2)

        label_selecionar_paciente = Label(self, width=26, height=2, text='Selecione e escolhar alguma ação:', font=(
            "Arial", 18), bg='#242323', fg='#888a89')
        label_selecionar_paciente.place(x=10, y=80)

        self.treeview = Treeview(self, columns=(
            "CID", "Nome"), height=21,  show="headings")

        self.treeview.column("CID", width=100)
        self.treeview.column("Nome", width=860)

        # Definir as colunas
        self.treeview.heading("CID", text="CID")
        self.treeview.heading("Nome", text="Nome")

        self.treeview.place(x=10, y=150)

        for dado in self.doencas_obtidas:
            self.treeview.insert("", "end", values=dado)

        self.treeview.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.treeview.yview)

        def alterar():
            from telas.paciente_cadastro import cadastrarPacientes
            # Lógica para alterar
            selected_item = self.treeview.selection()
            if selected_item:
                item = self.treeview.item(selected_item)
                controller.carregar_tela(
                    cadastrarPacientes, {"modo": "alterar", "paciente_alterar": item["values"]})

        def excluir():
            # Lógica para excluir
            selected_item = self.treeview.selection()
            if selected_item:
                item = self.treeview.item(selected_item)
                sistema_pacientes.remover(
                    cpf=item["values"][0], nome=item["values"][1])
                controller.carregar_tela(DoencasListagem)

        frame = tk.Frame(self)
        frame.place(x=400, y=95)

        botao_alterar = tk.Button(frame, text="Alterar", command=alterar)
        botao_alterar.pack(side="left", padx=2, pady=2)

        botao_excluir = tk.Button(frame, text="Excluir", command=excluir)
        botao_excluir.pack(side="left", padx=2, pady=2)

    # função que verifica se o campo de pesquisa esta vazio caso esteja ele carrega todos os pacientes
    def __verificar_campo_pesquisa(self):
        if len(self.entrada_pesquisa.get()) == 0:
            self.treeview.delete(*self.treeview.get_children())
            for dado in self.doencas_obtidas:
                self.treeview.insert("", "end", values=dado)

    def pesquisar(self, sistema_doencas: SistemaDoenca, controller):

        doenca_selecionado = self.entrada_pesquisa.get()

        doencas_encontradas = sistema_doencas.consultar(
            buscador=doenca_selecionado)

        if doencas_encontradas:
            self.treeview.delete(*self.treeview.get_children())
            for dado in doencas_encontradas:
                self.treeview.insert("", "end", values=dado)
        else:
            self.treeview.delete(*self.treeview.get_children())
            messagebox.showinfo(
                "Aviso!", "Paciente não encontrado!", icon="warning")

    def voltar_menu(self, controller):
        from telas.menu_opcoes import MenuOpcoes
        controller.show_frame(MenuOpcoes)

    def cadastrar_doencas(self, controller):
        from telas.cadastro_doenca import cadastrarDoencas
        controller.show_frame(cadastrarDoencas)
