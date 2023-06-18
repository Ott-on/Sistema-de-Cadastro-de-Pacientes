import tkinter as tk
from tkinter import RAISED, RIDGE, Button, Entry, Label, PhotoImage, Scrollbar, messagebox
from tkinter.ttk import Treeview
from modelos.paciente import *
from modelos.sistema_doencas import SistemaDoenca
from modelos.sistema_pacientes import SistemaPacientes


class ConsultarPaciente(tk.Frame):
    def __init__(self, parent, controller, *args):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#242323')

        self.paciente_dados = {}

        if args:
            self.paciente_dados = args[0]["paciente"]

        print(self.paciente_dados)

        sistema_doenca = SistemaDoenca()
        self.doencas_obtidas = sistema_doenca.obter_doencas()

        # Criar a barra de rolagem
        scrollbar = tk.Scrollbar(self)
        scrollbar.place(x=972, y=300, height=284)

        # retangulo azul da tela
        label_retangulo = Label(self, width=1000, height=4, bg='#02bae8')
        label_retangulo.place(x=0, y=0)

        img = PhotoImage(file='imagens/voltar_label.png')
        button_image = Button(self, image=img, bg='#02bae8', fg='#02bae8', activebackground='#02bae8', command=lambda: self.voltar(
            controller), relief='solid', overrelief='solid', borderwidth=0, highlightthickness=0)
        button_image.image = img
        button_image.place(x=10, y=10)

        # botão cadastrar:
        button_atender = Button(self, text='ATENDER', font=("Arial", 16), activebackground='gray', bg='grey',
                                fg='white',  relief='solid', overrelief='solid', width=10, height=2, borderwidth=0, highlightthickness=0)
        button_atender.place(x=850, y=2)

        label_nome_paciente = Label(self, width=15, height=2, justify="center", bg='#242323', text='Nome do paciente:', font=(
            "Arial", 16), fg='#888a89')
        label_nome_paciente.place(x=10, y=80)

        nome_paciente = self.paciente_dados[1] if self.paciente_dados else "Não setado"
        label_nome_paciente_dado = Label(self, width=40, justify="center", anchor="w",  height=1, bg='#242323', text=nome_paciente, font=(
            "Arial", 20), fg='#888a89')
        label_nome_paciente_dado.place(x=10, y=120)

        cpf_paciente = self.paciente_dados[0] if self.paciente_dados else "Não setado"
        label_cpf_paciente = Label(self, width=15, height=2, justify="center", bg='#242323', text=cpf_paciente, font=(
            "Arial", 16), fg='#888a89')
        label_cpf_paciente.place(x=450, y=80)

        label_cpf_paciente_dado = Label(self, width=30, justify="center", anchor="w",  height=1, bg='#242323', text='123.456.789-10', font=(
            "Arial", 20), fg='#888a89')
        label_cpf_paciente_dado.place(x=450, y=120)

        label_selecionar_paciente = Label(self, width=27, height=2, anchor="w", text='Selecione e escolhar alguma ação:', font=(
            "Arial", 18), bg='#242323', fg='#888a89')
        label_selecionar_paciente.place(x=10, y=180)

        label_historico_paciente = Label(self, width=27, height=2, anchor="w", text='Histórico de atendimentos', font=(
            "Arial", 18), bg='#242323', fg='#888a89')
        label_historico_paciente.place(x=10, y=240)

        self.treeview = Treeview(self, columns=(
            "Hora", "Data"), height=13,  show="headings")

        self.treeview.column("Hora", width=100)
        self.treeview.column("Data", width=860)

        # Definir as colunas
        self.treeview.heading("Hora", text="Hora")
        self.treeview.heading("Data", text="Data")

        self.treeview.place(x=10, y=300)

        dados = [
            ('23:25', "23/02/2023")
        ]

        for dado in dados:
            self.treeview.insert("", "end", values=dado)

        self.treeview.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.treeview.yview)

        def visualizar_dados_atendimentos():
            # Lógica para alterar
            selected_item = self.treeview.selection()
            if selected_item:
                item = self.treeview.item(selected_item)
                # controller.carregar_tela(
                #     cadastrarDoencas, {"modo": "alterar", "doenca_alterar": item["values"]})
            else:
                messagebox.showinfo(
                    "Aviso!", "Selecione um item do historico de atendimentos para visualizar os seus dados!", icon="warning")

        frame = tk.Frame(self)
        frame.place(x=400, y=195)

        botao_alterar = tk.Button(
            frame, text="Visualizar dados do atentimento", command=visualizar_dados_atendimentos)
        botao_alterar.pack(side="left", padx=2, pady=2)

    def voltar(self, controller):
        from telas.tela_paciente import Pacientes
        controller.carregar_tela(Pacientes)
