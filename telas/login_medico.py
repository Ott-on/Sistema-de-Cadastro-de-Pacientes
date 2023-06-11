from tkinter import *

janela = Tk() #instância da janela
janela.title("Sistema de Cadastro de Pacientes") #nome da interface
janela.geometry('1000x600') #tamanho da tela
janela.config(bg='#242323') #cor do fundo
janela.iconphoto(False, PhotoImage(file='images/icon.png')) #icone 
janela.resizable(width=False, height=False) #não deixar que o usúario amplie a tela

"""
funções:
def pegar_usuario_senha():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    entrada_usuario.delete(0,END)
    entrada_senha.delete(0,END)
"""
#textos e títulos que aparecem:
#imagem da tela de login:
img= PhotoImage(file='images/tela de abertura2.png')
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
label_senha.place(x=650, y=260)
entrada_senha = Entry(janela, width=14, font=("Arial", 25), show = "*", bg='#636262', highlightthickness=0.5, relief='solid')
entrada_senha.place(x=670, y=290)

#botões:
fazer_login = Button(janela, text='Entrar', width=23, height=2, font=("Arial", 15), bg='#02bae8', relief=RAISED, overrelief=RAISED)
fazer_login.place(x=670, y=375)

janela.mainloop()
