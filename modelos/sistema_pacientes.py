import pandas as pd
import os.path
from modelos.paciente import Paciente


class SistemaPacientes:
    def __init__(self):
        self.arquivo_csv = "dados/pacientes.csv"

        # Verificar se o arquivo existe
        if not os.path.isfile(self.arquivo_csv):
            # Criar o arquivo e adicionar os cabeçalhos das colunas
            df_cabecalho = pd.DataFrame(columns=[
                                        "nome", "cpf", "email", "telefone", "celular", "data_nascimento", "sexo", "estado_civil"])
            df_cabecalho.to_csv(self.arquivo_csv, index=False, sep=';')

    def obter_pacientes(self):
        tabela_pacientes = pd.read_csv(self.arquivo_csv, sep=";")
        pacientes = []
        for _, row in tabela_pacientes.iterrows():
            paciente = (
                row['cpf'],
                row['nome'],
                row['email'],
                row['telefone'],
                row['celular'],
                row['data_nascimento'],
                row['sexo'],
                row['estado_civil']
            )
            pacientes.append(paciente)
        return pacientes

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

        df.to_csv(self.arquivo_csv, index=False,
                  sep=';', mode='a', header=False)

        lido = pd.read_csv(self.arquivo_csv)
        print(lido)

    def remover(self, paciente_selecionado):

        # lê o arquivo csv dos pacientes
        tabela_pacientes = pd.read_csv("dados/pacientes.csv")

        # procura a linha do paciente no arquivo
        paciente_procurado = tabela_pacientes.loc[tabela_pacientes['Nome'] ==
                                                  paciente_selecionado | tabela_pacientes['CPF'] == paciente_selecionado]

        # retira a linha do arquivo
        tabela_pacientes = tabela_pacientes.drop(paciente_procurado.index)

        # substitui o arquivo antigo pelo arquivo sem o paciente
        tabela_pacientes.to_csv('dados/pacientes.csv', index=False, sep=';')

    def alterar(self, paciente_selecionado, dado_para_alterar, novo_dado):

        # lê o arquivo csv dos pacientes
        tabela_pacientes = pd.read_csv("dados/pacientes.csv")

        # procura a linha do paciente no arquivo
        paciente_procurado = tabela_pacientes.loc[tabela_pacientes['Nome'] ==
                                                  paciente_selecionado | tabela_pacientes['CPF'] == paciente_selecionado]

        # altera o dado especifico da linha
        paciente_procurado.loc[paciente_procurado.index,
                               dado_para_alterar] = novo_dado
        # coloca o novo dado no arquivo principal de pacientes
        tabela_pacientes.loc[paciente_procurado.index] = paciente_procurado

        # substitui a o arquivo antigo pelo arquivo alterado
        tabela_pacientes.to_csv(self.arquivo_csv, index=False, sep=';')

    def consultar(self, buscador):
        # Converter o buscador para string
        buscador = str(buscador)

        # lê o arquivo csv dos pacientes
        tabela_pacientes = pd.read_csv(self.arquivo_csv, sep=";")

        # Verificar se o buscador é um CPF válido
        if buscador.isdigit():
            # Buscar pelo CPF
            pacientes_procurados = tabela_pacientes.loc[tabela_pacientes['cpf'].astype(
                str).str.contains(buscador)]
        else:
            # Buscar pelo nome ou parte do nome
            pacientes_procurados = tabela_pacientes.loc[tabela_pacientes['nome'].astype(
                str).str.contains(buscador, case=False)]

        # Se houver pacientes encontrados, retorna as informações como uma lista de tuplas
        if not pacientes_procurados.empty:
            pacientes_info = []
            for _, paciente in pacientes_procurados.iterrows():
                paciente_info = (
                    paciente['cpf'],
                    paciente['nome'],
                    paciente['email'],
                    paciente['telefone'],
                    paciente['celular'],
                    paciente['data_nascimento'],
                    paciente['sexo'],
                    paciente['estado_civil'],
                )
                pacientes_info.append(paciente_info)

            return pacientes_info

        # Retorna None se não houver pacientes encontrados
        return None
