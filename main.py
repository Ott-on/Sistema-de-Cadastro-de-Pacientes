# paciente = Paciente('Otton', '12345678910', 'otton@gmail.com', '123465678', '12345678', f'20/03/2003', 'M', 'solteiro')

# cadastro = CadastroPacientes()
# cadastro.cadastrar(paciente)

import tkinter as tk
from tkinter import PhotoImage, ttk

from telas.login_medico import LoginMedico
from telas.cadastro_medico import CadastroMedico
from telas.menu_opcoes import MenuOpcoes


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

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginMedico, CadastroMedico, MenuOpcoes):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginMedico)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


app = tkinterApp()
app.mainloop()
