import pandas as pd
import os.path

from modelos.atendimento import Atendimento


class SistemaAtendimento:
    def __init__(self):
        self.arquivo_csv = "dados/registros_atendimentos.csv"

        # Verificar se o arquivo existe
        if not os.path.isfile(self.arquivo_csv):
            # Criar o arquivo e adicionar os cabeçalhos das colunas
            df_cabecalho = pd.DataFrame(columns=[
                                        "cpf_paciente", "data_atendimento", "hora_atendimento", "peso_paciente", "altura_paciente", "relato_paciente", "anotacoes_medico", "exames_passados", "diagnostico_medico", "codigo_cid", "tratamento_ou_medicamentos_prescritos", ])
            df_cabecalho.to_csv(self.arquivo_csv, index=False, sep=';')

    def possui_registro(self, cpf):
        cpf = str(cpf)

        # lê o arquivo csv dos registros
        tabela_registros = pd.read_csv(self.arquivo_csv, sep=";")

        # busca algum registro
        registros_procurados = tabela_registros.loc[tabela_registros['cpf_paciente'].astype(
            str).str.contains(cpf)]

        # Se houver registros encontrados, retorna true senão false
        return not registros_procurados.empty

    def consultar_registros(self, cpf):
        # Converter o buscador para string
        cpf = str(cpf)

        # lê o arquivo csv dos registros
        tabela_registros = pd.read_csv(self.arquivo_csv, sep=";")

        # Verificar se o buscador é um CPF válido
        registros_procurados = tabela_registros.loc[tabela_registros['cpf_paciente'].astype(
            str).str.contains(cpf)]

        # Se houver registros encontrados, retorna as informações como uma lista de tuplas
        if not registros_procurados.empty:
            registros_atendimentos_info = []
            for _, registro in registros_procurados.iterrows():
                registro_atendimento_info = (
                    registro["cpf_paciente"],
                    registro["data_atendimento"],
                    registro["hora_atendimento"],
                    registro["peso_paciente"],
                    registro["altura_paciente"],
                    registro["relato_paciente"],
                    registro["anotacoes_medico"],
                    registro["exames_passados"],
                    registro["diagnostico_medico"],
                    registro["codigo_cid"],
                    registro["tratamento_ou_medicamentos_prescritos"],
                )
                registros_atendimentos_info.append(registro_atendimento_info)

            return registros_atendimentos_info

        # Retorna None se não houver registros encontrados
        return None

    def registrar(self, atendimento: Atendimento):
        dados = {
            "cpf_paciente": [atendimento.cpf_paciente],
            "data_atendimento": [atendimento.data_atendimento],
            "hora_atendimento": [atendimento.hora_atendimento],
            "peso_paciente": [atendimento.peso_paciente],
            "altura_paciente": [atendimento.altura_paciente],
            "relato_paciente": [atendimento.relato_paciente],
            "anotacoes_medico": [atendimento.anotacoes_medico],
            "exames_passados": [atendimento.exames_passados],
            "diagnostico_medico": [atendimento.diagnostico_medico],
            "codigo_cid": [atendimento.codigo_cid],
            "tratamento_ou_medicamentos_prescritos": [atendimento.tratamento_ou_medicamentos_prescritos],
        }

        df = pd.DataFrame(dados)

        df.to_csv(self.arquivo_csv, index=False,
                  sep=';', mode='a', header=False)

        lido = pd.read_csv(self.arquivo_csv)
        print(lido)
