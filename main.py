from modelos.cadastro_pacientes import CadastroPacientes
from modelos.paciente import Paciente

# paciente = Paciente('Otton', '12345678910', 'otton@gmail.com', '123465678', '12345678', f'20/03/2003', 'M', 'solteiro')

# cadastro = CadastroPacientes()
# cadastro.cadastrar(paciente)

import tkinter as tk
from tkinter import PhotoImage, ttk

from telas.login_medico import LoginMedico
from telas.cadastro_medico import CadastroMedico


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

        for F in (StartPage, Page1, Page2, LoginMedico, CadastroMedico):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg='#242323')

        label = ttk.Label(self, text="Startpage", font=LARGEFONT)

        label.grid(row=0, column=4, padx=10, pady=10)
        button1 = ttk.Button(self, text="Login Medico",
                             command=lambda: controller.show_frame(LoginMedico))

        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(CadastroMedico))

        button2.grid(row=2, column=1, padx=10, pady=10)


class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#242323')
        label = ttk.Label(self, text="Page 1", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: controller.show_frame(StartPage))

        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page2))

        button2.grid(row=2, column=1, padx=10, pady=10)


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#242323')
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)
        label2 = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label2.grid(row=0, column=8, padx=10, pady=10)

        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(Page1))

        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        button2.grid(row=2, column=1, padx=10, pady=10)


app = tkinterApp()
app.mainloop()
