from tkinter import *
from tkinter import messagebox


janela = Tk() #instância da janela
janela.title("Sistema de Cadastro de Pacientes") #nome da interface
janela.geometry('1000x600') #tamanho da tela
janela.config(bg='#242323') #cor do fundo
janela.iconphoto(False, PhotoImage(file='imagens/icon.png')) #icone 
janela.resizable(width=False, height=False) #não deixar que o usúario amplie a tela

# entrada_usuario.delete(0,END)
# entrada_senha.delete(0,END)

def fazer_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    # Aqui verificamos se os campos foram preenchidos caso não deve mostrar um erro pedindo para preencher os campos
    if len(usuario) != 0:
        # Se ocorrer tudo bem iremos dazer o login
        print(f"usuário:", usuario)
        print(f"senha:", senha)
    else:
        # Aqui exibimos um popup de aviso pedindo para os campos serem preenchidos
        messagebox.showinfo("Aviso!", "Preencha os campos para continuar", icon="warning")

img= PhotoImage(file='imagens/tela_abertura.png')
label_image = Label(janela, image=img)
label_image.place(x=-60,y=-5)

label_fundobranco = Label(janela, width=45, height=30, background='white', relief=RIDGE)
label_fundobranco.place(x=638,y=50)

#LOGIN:
label_LOGIN = Label(janela, width=10, height=2, text='LOGIN', font=("Arial", 25), bg='white',fg='#02bae8')
label_LOGIN.place(x=700, y=70)

#Usuário:
label_usuario = Label(janela, width=10, height=2, text='Usuário:', font=("Arial", 10), bg='white',fg='#888a89')
label_usuario.place(x=650, y=160)
entrada_usuario = Entry(janela, width=14, font=("Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
entrada_usuario.place(x=670, y=190)

#Senha:
label_senha = Label(janela, width=10, height=2, text='Senha:', font=("Arial", 10), bg='white',fg='#888a89')
label_senha.place(x=650, y=240)
entrada_senha = Entry(janela, width=14, font=("Arial", 25), show = "*", bg='#636262', highlightthickness=0.5, relief='solid')
entrada_senha.place(x=670, y=270)

#botões:
botao_login = Button(janela, text='Entrar', width=23, command=fazer_login, height=2, font=("Arial", 15), bg='#02bae8', relief=RAISED, overrelief=RAISED)
botao_login.place(x=670, y=330)
botao_cadastro = Button(janela, text='Cadastrar', width=23, command=fazer_login, height=2, font=("Arial", 15), bg='#eeeeee', relief=RAISED, overrelief=RAISED)
botao_cadastro.place(x=670, y=400)

janela.mainloop()