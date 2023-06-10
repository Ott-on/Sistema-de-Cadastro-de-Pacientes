from modelos.cadastro_pacientes import CadastroPacientes
from tkinter import *
from tkinter import ttk

cadastro = CadastroPacientes()

def imprima():
    cadastro.cadastrar('nome', 'cpf', 'email', 'telefone', 'celular', f'dia/mes/ano', 'sexo', 'civil')

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=imprima).grid(column=1, row=0)
root.mainloop()
