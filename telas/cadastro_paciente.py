import tkinter as tk
from tkinter import RAISED, RIDGE, Button, Entry, Label, PhotoImage, messagebox


class CadastroPaciente(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#242323')

        # Nome

        # CPF

        # Email

        # Celular

        # Telefone

        # Data de Nascimento

        # Sexo

        # Estado Civil

    def fazer_login(self):
        nome = self.entrada_nome.get()
        cpf = self.entrada_cpf.get()
        email = self.entrada_email.get()
        telefone = self.entrada_telefone.get()
        celular = self.entrada.celular.get()
        nascimento = self.entrada_nascimento.get()
        sexo = self.entrada_sexo.get()
        civil = self.entrada_civil.get()

        # Aqui verificamos se os campos foram preenchidos caso não deve mostrar um erro pedindo para preencher os campos
        if cpf.isdigit() and len(cpf) == 11 and telefone.isalpha() and celular.isalpha() and len(nascimento) != 0 and sexo.isalpha() and civil.isalpha():
            print('ok')

        else:
            # Aqui exibimos um popup de aviso pedindo para os campos serem preenchidos
            messagebox.showinfo(
                "Aviso!", "Preencha os campos para continuar", icon="warning")
