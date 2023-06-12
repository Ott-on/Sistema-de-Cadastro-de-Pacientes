import tkinter as tk
from tkinter import RAISED, RIDGE, Button, Entry, Label, PhotoImage, messagebox


class LoginMedico(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        img = PhotoImage(file='imagens/tela_abertura.png')
        label_image = Label(self, image=img)
        label_image.place(x=-60, y=-5)

        label_fundobranco = Label(
            self, width=45, height=30, background='white', relief=RIDGE)
        label_fundobranco.place(x=638, y=50)

        # LOGIN:
        label_LOGIN = Label(self, width=10, height=2, text='LOGIN', font=(
            "Arial", 25), bg='white', fg='#02bae8')
        label_LOGIN.place(x=700, y=70)

        # Usuário:
        label_usuario = Label(self, width=10, height=2, text='Usuário:', font=(
            "Arial", 10), bg='white', fg='#888a89')
        label_usuario.place(x=650, y=160)
        entrada_usuario = Entry(self, width=14, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_usuario.place(x=670, y=190)

        self.entrada_usuario = entrada_usuario

        # Senha:
        label_senha = Label(self, width=10, height=2, text='Senha:', font=(
            "Arial", 10), bg='white', fg='#888a89')
        label_senha.place(x=650, y=240)
        entrada_senha = Entry(self, width=14, font=(
            "Arial", 25), show="*", bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_senha.place(x=670, y=270)

        self.entrada_senha = entrada_senha

        # botões:
        botao_login = Button(self, text='Entrar', width=23, command=self.fazer_login, height=2, font=(
            "Arial", 15), bg='#02bae8', relief=RAISED, overrelief=RAISED)
        botao_login.place(x=670, y=330)
        botao_cadastro = Button(self, text='Cadastrar', width=23, command=self.fazer_cadastro, height=2, font=(
            "Arial", 15), bg='#eeeeee', relief=RAISED, overrelief=RAISED)
        botao_cadastro.place(x=670, y=400)

    def fazer_login(self):
        usuario = self.entrada_usuario.get()
        senha = self.entrada_senha.get()

        # Aqui verificamos se os campos foram preenchidos caso não deve mostrar um erro pedindo para preencher os campos
        if len(usuario) != 0:
            # Se ocorrer tudo bem iremos fazer o login
            print(f"usuário:", usuario)
            print(f"senha:", senha)
        else:
            # Aqui exibimos um popup de aviso pedindo para os campos serem preenchidos
            messagebox.showinfo(
                "Aviso!", "Preencha os campos para continuar", icon="warning")


# app = tk.Tk()
# app.title("Sistema de Cadastro de Pacientes")
# app.geometry('1000x600')
# app.config(bg='#242323')
# app.iconphoto(False, PhotoImage(file='imagens/icon.png'))
# app.resizable(width=False, height=False)

# login_medico = LoginMedico(app, app)
# login_medico.pack()

# app.mainloop()

