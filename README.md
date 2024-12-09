# Visão Geral do Projeto
- Objetivo: Criar uma aplicação web em Java que permita gerenciar serviços de uma estética automotiva, com funcionalidades de previsão de falência e análise de gastos/ganhos futuros utilizando modelos de IA.
- Tecnologias:
- Java com Spring Boot para a aplicação web.
- HTML, CSS E JAVASCRIPT - caso quiser usar, Thymeleaf para o front-end da aplicação web.
- MySQL como banco de dados.
- Python com Scikit-Learn e Streamlit para os modelos de IA e interface de visualização.

Vamos adicionar os seguintes módulos à estrutura do projeto:

Modelos de Dados para agendamentos e pagamentos.
Repositórios e Serviços para manipulação dos dados de agendamento e pagamento.
Controladores para gerenciar as rotas de serviços, agendamentos e pagamentos.
Páginas Thymeleaf para interface do usuário.

Preparação do Ambiente de Desenvolvimento
Instalação do Java Development Kit (JDK):

- Verifique se o JDK está instalado com:
java -version
- Caso não tenha, faça o download aqui e instale.
Instalação do Python:
Verifique se o Python está instalado com:
python --version
Caso não tenha, faça o download aqui e instale.

- Instalação do Maven (para o projeto Java):
Verifique com:
mvn -v
Se não estiver instalado, siga o guia de instalação do Maven aqui.

- Instalação do Streamlit:

Instale o Streamlit com:
pip install streamlit
- Estrutura do Projeto
  - Java (Spring Boot):
  - src/main/java/com/estetica/automotiva
  - controller (Controladores)
  - model (Modelos de dados)
  - repository (Repositórios)
  - service (Serviços)
  - src/main/resources
  - templates (Páginas Thymeleaf)
  - application.properties (Configuração do banco de dados)

- Python (Streamlit e IA):

  - src/main/python/ia
  - modelo_previsao_falencia.py
  - modelo_gastos_ganhos.py
  - src/main/resources/static
  - streamlit_app.py

# Itens mínimos obrigatórios,
1. Documentação;
2. BD;
3. Código em linguagem Java;
4. CRUD;
5. Testes;
6. Implementação;
7. Apresentação (Ex: Power Point, Gamma, etc.)
