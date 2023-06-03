import pandas

#  listas  com os dados dos pacientes

informacoes_pacientes = []

informacoes_doencas = []

informacoes_registros = []

informacoes_relatorios = []

class CadastroPaciente():
  def __init__(self):

    pass

  #função cadastrar paciente

  def cadastrar_paciente(self):
    global informacoes_pacientes
    
    cadastro_paciente = []

    cadastro_paciente.append(input('\nNome do paciente: '))
    cadastro_paciente.append(input('CPF do paciente: '))
    cadastro_paciente.append(input('Email do paciente: '))
    cadastro_paciente.append(input('Telefone do paciente: '))
    cadastro_paciente.append(input('Celular do paciente: '))
    cadastro_paciente.append(input('Data de Nascimento do paciente: '))
    cadastro_paciente.append(input('Sexo do paciente: '))
    cadastro_paciente.append(input('Estado Civil do paciente: '))

    informacoes_pacientes.append(cadastro_paciente)

  # função remover paciente

  def remover_cadastro(self):
    global informacoes_pacientes

    paciente = 0

    remover = input('digite o CPF do paciente: ')

    for i in informacoes_pacientes:
      if i[1] == remover:
        informacoes_pacientes.pop(paciente)
        
      paciente += 1


  # função alterar cadatro

  def alterar_cadastro(self):
    global informacoes_pacientes

    alterar = input('digite o cpf do paciente que deseja alterar informações: ')
    
    paciente = 0
    
    for i in informacoes_pacientes:
      if i[1] == alterar:
        o_que = int(input('o que você deseja alterar: nome (1), cpf (2), Email(3), Telefone(4), Celular(5), Data de nascimento(6), Sexo do paciente(7), Estado Civil(8)'))
        informacoes_pacientes[paciente][o_que - 1] = input('Digite o novo dado: ')
      paciente += 1

        
  # função consultar informações

  def consultar_cadastro(self):
    global informacoes_pacientes

    consulta = input('Digite o cpf ou o nome do paciente que deseja consultar informações: ')

    for i in informacoes_pacientes:
      if i[1] == consulta or i[0] == consulta:
        print(i)
    else:
      print("\nEste paciente ainda não foi cadastrado, cadastre-o:")
      funcionalidade_1.cadastrar_paciente()

    

class CadastroDoenca():
  def __init__(self):

    pass
  
  # função  cadastrar doenças

  
  
  def cadastrar_doenca(self):
    global informacoes_doencas
    print('fewgverhjnrt6ju65')
    cadastro_doenca = []

    cadastro_doenca.append(input('Digite o código da doença: '))
    cadastro_doenca.append(input('Digite o nome da doenca: '))

    informacoes_doencas.append(cadastro_doenca)
    


# criando objetos

funcionalidade_1 = CadastroPaciente()
funcionalidade_2 = CadastroDoenca()


while True:

  funcionalidade = input('\nCadastro do paciente (1), cadastrar código de doença (2), registrar atendimento ao paciente (3), relatório (4), encerrar (s): ')
    
  # menu de cadastramento do paciente

  if funcionalidade == '1':

    opcoes_cadastro_paciente = input('Cadastrar (1), Remover (2), Alterar (3), Consultar nome/CPF (4): ')

    if opcoes_cadastro_paciente == '1':
      funcionalidade_1.cadastrar_paciente()

    elif opcoes_cadastro_paciente == '2':
      funcionalidade_1.remover_cadastro()
      
    elif opcoes_cadastro_paciente == '3':
      funcionalidade_1.alterar_cadastro()

    elif opcoes_cadastro_paciente == '4':
      funcionalidade_1.consultar_cadastro()

  elif funcionalidade == 's':
    break
  # menu de cadastramento de doença

  elif funcionalidade == '2':

    opcoes_cadastro_doenca = input('Cadastrar (1), Remover (2), Alterar (3), Consultar (4): ')

    if opcoes_cadastro_doenca == '1':
      funcionalidade_2.cadastrar_doenca()
  
  

print(informacoes_pacientes)
print(informacoes_doencas)


























