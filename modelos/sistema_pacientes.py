import pandas as pd
import os.path

from paciente import *

from modelos.paciente import Paciente


class SistemaPacientes:
    def __init__(self):
        self.arquivo_csv = "dados/otton.csv"

        # Verificar se o arquivo existe
        if not os.path.isfile(self.arquivo_csv):
            # Criar o arquivo e adicionar os cabeçalhos das colunas
            df_cabecalho = pd.DataFrame(columns=["Nome", "CPF", "Email", "Telefone", "Celular", "Data de Nascimento", "Sexo", "Estado Civil"])
            df_cabecalho.to_csv(self.arquivo_csv, index=False, sep=';')

    # Metodo para cadastrar paciente
    def cadastrar(self, paciente: Paciente):
        dados = {
            "nome": [paciente.nome],
            "cpf": [paciente.cpf],
            "email": [paciente.email], 
            "telefone": [paciente.telefone], 
            "celular": [paciente.celular], 
            "data_nascimento": [paciente.data_nascimento], 
            "sexo": [paciente.sexo], 
            "estado_civil": [paciente.estado_civil],
        }

        df = pd.DataFrame(dados)
        df.to_csv("dados/otton.csv", index=False, sep=',', mode='a')

        lido = pd.read_csv("dados/otton.csv")
        print(lido)

    def remover(self):
        pass

    def alterar_cadastro(self):
        pass

    def consultar_paciente(self, valor_buscar):
        pass