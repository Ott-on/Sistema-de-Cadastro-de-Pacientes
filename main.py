import tkinter as tk
from tkinter import PhotoImage, ttk

from telas.login_medico import LoginMedico
from telas.cadastro_medico import CadastroMedico
from telas.menu_opcoes import MenuOpcoes
from telas.relatorio import Relatorio
from telas.tela_paciente import Pacientes
from telas.doencas_cadastradas import Doenca
from telas.paciente_cadastro import cadastrarPacientes
from telas.cadastro_doenca import cadastrarDoencas

LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('1000x600')  # Define o tamanho da tela
        # Define o nome da interface
        self.title("Sistema de Cadastro de Pacientes")
        self.config(bg='#242323')  # Define a cor de fundo
        self.iconphoto(False, PhotoImage(
            file='imagens/icon.png'))  # Define o ícone
        # Impede que o usuário redimensione a tela
        self.resizable(width=False, height=False)

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.create_frames()

        self.show_frame(LoginMedico)

    def create_frames(self):
        # Cria as instâncias dos frames e armazena em um dicionário
        for F in (LoginMedico, CadastroMedico, MenuOpcoes, Relatorio, Pacientes, Doenca, cadastrarPacientes, cadastrarDoencas):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, cont):
        # Mostra o frame correspondente à tela desejada
        frame = self.frames[cont]
        frame.tkraise()

    def carregar_tela(self, screen, *args):
        # Função que instancia um novo frame e troca para a nova tela
        frame = screen(self.container, self, *args)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()


app = tkinterApp()
app.mainloop()
