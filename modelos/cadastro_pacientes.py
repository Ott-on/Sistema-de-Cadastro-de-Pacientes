import pandas as pd

from modelos.paciente import Paciente


class CadastroPacientes:
    def __init__(self):
        pass

    # Metodo para cadastrar paciente
    def cadastrar(self, paciente: Paciente):
        d = {
            "nome": [paciente.nome],
            "cpf": [paciente.cpf],
            "email": [paciente.email], 
            "telefone": [paciente.telefone], 
            "celular": [paciente.celular], 
            "data_nascimento": [paciente.data_nascimento], 
            "sexo": [paciente.sexo], 
            "estado_civil": [paciente.estado_civil],
        }

        df = pd.DataFrame(d)
        df.to_csv("dados/teste.csv", index=False, sep=',', mode='a')

        lido = pd.read_csv("teste.csv")
        print(lido)

    def remover(self):
        pass

    def alterar_cadastro(self):
        pass

    def consultar_paciente(self, valor_buscar):
        pass