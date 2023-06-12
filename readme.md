# Temas - Sistema de Cadastro de Pacientes

O objetivo deste sistema é cadastrar informações importantes sobre os pacientes de um determinado médico. Assim, o objetivo é auxiliar o médico na manutenção do cadastro do paciente para facilitar o acompanhamento da saúde do mesmo. Para isso, o sistema deve oferecer as seguintes funcionalidades:

## Cadastramento de paciente

Dados do usuário: Nome, CPF, email, telefone, celular, data de nascimento, sexo, estado civil.

Opções do menu de Cadastramento de Paciente:

- Cadastrar
- Remover
- Alterar
- Consultar (pelo nome, ou parte do nome, ou pelo CPF)

## Cadastramento de código de doença

Tem como objetivo manter no sistema os códigos universais das doenças, conforme tabela CID. Exemplo: [CID-10](http://www.bulas.med.br/cid-10/)

Opções do menu de Cadastramento de código de doença:

- Cadastrar
- Remover
- Alterar
- Consultar (pelo código, nome ou parte do nome da doença)

## Registrar atendimento ao paciente

Ao registrar um atendimento, o médico deve inicialmente consultar o paciente no sistema ou cadastrar um novo paciente.

Caso se trate de um paciente previamente atendido, o sistema apresenta para o médico as datas dos atendimentos anteriores, bem como a opção de visualizar os dados de um destes atendimentos em detalhes.

Quando o médico desejar, ele poderá em qualquer momento acionar o sistema para iniciar o registro dos dados do novo atendimento, a saber:

- Peso e altura do paciente
- Relato do paciente
- Anotações do médico
- Relação de exames passados
- Diagnóstico médico
- Código CID relacionado ao diagnóstico
- Tratamento e/ou medicamentos prescritos nesta seção de atendimento

O sistema também grava em arquivo o dia e a hora do atendimento.

## Relatórios

- Listagem dos pacientes atendidos em determinado dia ou período informado.
- Listagem dos pacientes diagnosticados com determinado código CID.
- Listagem do histórico de atendimento de determinado paciente.

## Outras funcionalidades

- Usar arquivos para armazenamento e carga de informações relevantes, de modo que o programa possa ser encerrado quando o médico desejar.
- Usar um login e senha para que o médico possa entrar no sistema.
- Usar funções e coleções de dados para melhor estruturação do código.
- Comentar o código em partes mais relevantes.
