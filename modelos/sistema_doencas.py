import pandas as pd
import os.path


class SistemaDoenca:
    def __init__(self):
        self.arquivo_csv = "dados/doencas.csv"

        # Verificar se o arquivo existe
        if not os.path.isfile(self.arquivo_csv):
            # Criar o arquivo e adicionar os cabeçalhos das colunas
            df_cabecalho = pd.DataFrame(columns=["Nome", "CID"])
            df_cabecalho.to_csv(self.arquivo_csv, index=False, sep=';')

    # Metodo para cadastrar doença
    def cadastrar_doenca(self, nome, cid):
        dados = {
            "nome": [nome],
            "cid": [cid],        
        }

        df = pd.DataFrame(dados)
        df.to_csv("dados/otton.csv", index=False, sep=',', mode='a')

        lido = pd.read_csv("dados/doencas.csv")
        print(lido)

    def remover_doenca(self):
        pass

    def alterar_doenca(self):
        pass

    def consultar_doenca(self):
        pass