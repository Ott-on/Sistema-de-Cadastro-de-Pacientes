import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os.path


class SistemaMedico:
    def __init__(self):
        self.arquivo_csv = "dados/medicos.csv"

        # Verificar se o arquivo existe
        if not os.path.isfile(self.arquivo_csv):
            # Criar o arquivo e adicionar os cabeçalhos das colunas
            df_cabecalho = pd.DataFrame(
                columns=["CRM", "Nome_do_Medico", "usuarios", "senhas"])
            df_cabecalho.to_csv(self.arquivo_csv, index=False, sep=';')

    # Método para cadastrar médico
    def cadastrar(self, crm, nome_medico, usuario, senha, transacao_tela):
        d = {
            "CRM": [crm],
            "Nome_do_Medico": [nome_medico],
            "usuarios": [usuario],
            "senhas": [senha],
        }

        df_novo_medico = pd.DataFrame(d)

        # Adicionar os dados do médico ao arquivo CSV
        df_novo_medico.to_csv(self.arquivo_csv, index=False,
                              sep=';', mode='a', header=False)

        messagebox.showinfo(
            "Sucesso", "Médico cadastrado com sucesso! Faça Login para entrar em sua conta")
        transacao_tela()

    def login(self, usuario, senha, limpar_campos, transacao_tela):
        # Lendo os dados da planilha de médicos
        usuarios_df = pd.read_csv(self.arquivo_csv, sep=';')

        # Verificar se o login do médico existe na planilha
        usuario_existe = usuarios_df["usuarios"].isin([usuario]).any()

        if usuario_existe:
            # Obter a senha registrada para o médico
            senha_registrada = usuarios_df.loc[usuarios_df["usuarios"]
                                               == usuario, "senhas"].values[0]
            print(usuarios_df)
            print(usuarios_df.loc[usuarios_df["usuarios"]
                                  == usuario, "senhas"].values[0])

            if str(senha) == str(senha_registrada):
                # Usuário e senha corretos
                messagebox.showinfo("Sucesso", "Login bem-sucedido")
                transacao_tela()
                limpar_campos()
            else:
                # Senha incorreta
                messagebox.showerror("Erro", "Senha incorreta")
        else:
            # Usuário não encontrado
            messagebox.showerror("Erro", "Usuário não encontrado")
