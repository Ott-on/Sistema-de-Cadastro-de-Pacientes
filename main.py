import pandas
123
#  listas  com os dados dos pacientes

informacoes_paciente = []

todas_informacoes = []

# função cadastrar paciente

def cadastrar_paciente():
  global informacoes_paciente
  
  cadastro_paciente = []

  cadastro_paciente.append(input('\nNome do paciente: ')) 1233
  cadastro_paciente.append(input('CPF do paciente: '))
  cadastro_paciente.append(input('Email do paciente: '))
  cadastro_paciente.append(input('Telefone do paciente: '))
  cadastro_paciente.append(input('Celular do paciente: '))
  cadastro_paciente.append(input('Data de Nascimento do paciente: '))
  cadastro_paciente.append(input('Sexo do paciente: '))
  cadastro_paciente.append(input('Estado Civil do paciente: '))

  informacoes_paciente.append(cadastro_paciente)
  
 # função remover paciente

def remover_cadastro():
  global informacoes_paciente, todas_informações

  contador = 0

  remover = input('digite o CPF do paciente: ')

  for i in todas_informacoes:
    if i[0][1] == remover:
      todas_informacoes.pop(contador)
      
    contador += 1
  
 # função alterar cadatro

def alterar_cadastro():
  global informações_paciente, todas_informacoes

  alterar = input()

# menu de cadastramento

opcoes = input('Cadastrar (1), Remover (2), Alterar (3), Consultar nome/CPF (4): ')

if opcoes == '1':
  cadastrar_paciente()

elif opcoes == '2':
  remover_cadastro()




todas_informacoes.append(informacoes_paciente)
informacoes_paciente = []

print(informacoes_paciente)
print(todas_informacoes)



























