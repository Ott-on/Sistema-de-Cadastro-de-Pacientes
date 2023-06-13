import tkinter as tk
from tkinter import RAISED, RIDGE, Button, Entry, Label, PhotoImage, messagebox
from sistema_doencas import *


class CadastroDoenca(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#242323')

        # Nome
        self.entrada_nome = entrada_nome
        # CID
        self.entrada_cpf = entrada_cpf
        # Email
        

    def fazer_login(self):
        nome = self.entrada_nome.get()
        cid = self.entrada_cid.get()
        
        # Aqui verificamos se os campos foram preenchidos caso não deve mostrar um erro pedindo para preencher os campos
        if nome.isalpha() and cid.isalpha():
            print('ok')
            SistemaDoenca(nome, cid)

        else:
            # Aqui exibimos um popup de aviso pedindo para os campos serem preenchidos
            messagebox.showinfo(
                "Aviso!", "Preencha os campos para continuar", icon="warning")
