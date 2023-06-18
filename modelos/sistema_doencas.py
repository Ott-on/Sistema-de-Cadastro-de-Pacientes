import pandas as pd
import os.path


class SistemaDoenca:
    def __init__(self):
        self.arquivo_csv = "dados/doencas.csv"

        # Verificar se o arquivo existe
        if not os.path.isfile(self.arquivo_csv):
            # Criar o arquivo e adicionar os cabeçalhos das colunas
            df_cabecalho = pd.DataFrame(columns=["cid", "nome_doenca"])
            df_cabecalho.to_csv(self.arquivo_csv, index=False, sep=';')

    def obter_doencas(self):
        tabela_doencas = pd.read_csv(self.arquivo_csv, sep=";")
        doencas = []
        for _, row in tabela_doencas.iterrows():
            doenca = (
                row['cid'],
                row['nome_doenca'],
            )
            doencas.append(doenca)
        return doencas

    # Metodo para cadastrar doença
    def cadastrar(self, cid, nome_doenca):
        dados = {
            "cid": [cid],
            "nome_doenca": [nome_doenca],
        }

        df = pd.DataFrame(dados)
        df.to_csv(self.arquivo_csv, index=False,
                  sep=';', mode='a', header=False)

    def remover(self, cid):
        # Lê o arquivo CSV das doenças
        tabela_doencas = pd.read_csv(self.arquivo_csv, sep=';')

        # Procura as linhas das doenças com base no CID
        doencas_procuradas = tabela_doencas.loc[tabela_doencas['cid'] == cid]

        # Remove as linhas das doenças encontradas
        tabela_doencas = tabela_doencas.drop(doencas_procuradas.index)

        # Substitui o arquivo antigo pelo arquivo sem as doenças
        tabela_doencas.to_csv(self.arquivo_csv, index=False, sep=';')

    def alterar(self, cid, nome_doenca):
        self.remover(cid=cid)
        self.cadastrar(cid=cid, nome_doenca=nome_doenca)

    def consultar(self, buscador):
        # Converter o buscador para string
        buscador = str(buscador)

        # lê o arquivo csv dos doencas
        tabela_doencas = pd.read_csv(self.arquivo_csv, sep=";")

        procurado_pelo_nome = tabela_doencas.loc[tabela_doencas['nome_doenca'].astype(
            str).str.contains(buscador, case=False)]

        procurado_pelo_cid = tabela_doencas.loc[tabela_doencas['cid'].astype(
            str).str.contains(buscador)]

        if not procurado_pelo_nome.empty:
            doencas_procuradas = procurado_pelo_nome
        else:
            doencas_procuradas = procurado_pelo_cid

        # Se houver doencas encontrados, retorna as informações como uma lista de tuplas
        if not doencas_procuradas.empty:
            doencas_info = []
            for _, paciente in doencas_procuradas.iterrows():
                paciente_info = (
                    paciente['cid'],
                    paciente['nome_doenca'],
                )
                doencas_info.append(paciente_info)

            return doencas_info

        # Retorna None se não houver doencas encontrados
        return None
