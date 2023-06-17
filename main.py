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
        self.geometry('1000x600')  # tamanho da tela
        self.title("Sistema de Cadastro de Pacientes")  # nome da interface
        self.config(bg='#242323')  # cor do fundo
        self.iconphoto(False, PhotoImage(file='imagens/icon.png'))  # icone
        # não deixar que o usúario amplie a tela
        self.resizable(width=False, height=False)

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.create_frames()

        self.show_frame(Pacientes)

    def create_frames(self):
        for F in (LoginMedico, CadastroMedico, MenuOpcoes, Relatorio, Pacientes, Doenca, cadastrarPacientes, cadastrarDoencas):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


app = tkinterApp()
app.mainloop()
