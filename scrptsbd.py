import pymysql
from faker import Faker
import random
from datetime import datetime, timedelta

# Configuração do banco de dados
db_config = {
    "host": "127.0.0.1",
    "user": "lucas",
    "password": "",
    "database": "mev_estetica_automotiva"
}

# Inicialização do Faker
fake = Faker("pt_BR")

def conectar_db():
    return pymysql.connect(**db_config)

# Funções para popular dados

def inserir_usuarios(qtd_clientes=56):
    """
    Insere usuários no banco de dados com limite de tipos específicos.
    """
    print("Inserindo usuários...")
    connection = conectar_db()
    cursor = connection.cursor()
    
    # Define limites para cada tipo
    limite_por_tipo = {
        "gerente": 1,
        "supervisor": 1,
        "funcionario": 4
    }
    contador_tipos = {tipo: 0 for tipo in limite_por_tipo}  # Contador inicial para cada tipo
    
    # Lista para usuários
    tipos_disponiveis = ["cliente"]  # Clientes não têm limite

    # Adiciona os tipos que ainda têm espaço
    for tipo, limite in limite_por_tipo.items():
        tipos_disponiveis.extend([tipo] * limite)

    random.shuffle(tipos_disponiveis)  # Mistura a lista para aleatoriedade

    for _ in range(qtd_clientes):
        if tipos_disponiveis:
            tipo = tipos_disponiveis.pop()  # Retira o tipo da lista disponível
        else:
            tipo = "cliente"  # Insere apenas clientes quando os limites são atingidos
        
        # Gera dados
        nome = fake.name()
        email = fake.email()
        senha = "senha123"

        # Executa inserção
        query = "INSERT INTO usuarios (nome, email, senha, tipo) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (nome, email, senha, tipo))

    connection.commit()
    cursor.close()
    connection.close()
    print("Usuários inseridos com sucesso!")


def inserir_servicos():
    print("Inserindo serviços...")
    connection = conectar_db()
    cursor = connection.cursor()
    servicos = [
        ("Lavagem Simples", "Lavagem externa rápida", 50.0),
        ("Polimento Completo", "Polimento completo com produtos premium", 200.0),
        ("Higienização Interna", "Limpeza profunda interna", 150.0),
        ("Enceramento", "Aplicação de cera protetora", 120.0),
        ("Cristalização de Pintura", "Proteção avançada para pintura", 300.0)
    ]

    for nome, descricao, preco_base in servicos:
        query = "INSERT INTO servicos (nome, descricao, preco_base) VALUES (%s, %s, %s)"
        cursor.execute(query, (nome, descricao, preco_base))

    connection.commit()
    cursor.close()
    connection.close()

def inserir_produtos():
    print("Inserindo produtos...")
    connection = conectar_db()
    cursor = connection.cursor()
    produtos = [
        ("Shampoo Automotivo", "Shampoo para limpeza de carros", 30.0, 100),
        ("Cera Protetora", "Cera premium para proteção de pintura", 80.0, 50),
        ("Pano Microfibra", "Pano de microfibra para limpeza", 10.0, 200),
        ("Aromatizante", "Aromatizante para interior de veículos", 5.0, 300),
        ("Kit Polimento", "Kit completo para polimento", 250.0, 20)
    ]

    for nome, descricao, preco, estoque in produtos:
        query = "INSERT INTO produtos (nome, descricao, preco, estoque) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (nome, descricao, preco, estoque))

    connection.commit()
    cursor.close()
    connection.close()

def inserir_agendamentos(qtd=50):
    print("Inserindo agendamentos...")
    connection = conectar_db()
    cursor = connection.cursor()

    for _ in range(qtd):
        cliente_id = random.randint(1, 30)
        funcionario_id = random.randint(4, 7)
        servico_id = random.randint(1, 5)
        data_agendamento = datetime.now() - timedelta(days=random.randint(1, 365))
        status = random.choice(["pendente", "confirmado", "cancelado", "concluido"])
        observacoes = fake.sentence(nb_words=8)
        query = """
        INSERT INTO agendamentos (cliente_id, funcionario_id, servico_id, data_agendamento, status, observacoes)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (cliente_id, funcionario_id, servico_id, data_agendamento, status, observacoes))

    connection.commit()
    cursor.close()
    connection.close()

def inserir_financeiro(qtd_registros=50):
    if not isinstance(qtd_registros, int) or qtd_registros <= 0:
        raise ValueError("O parâmetro 'qtd_registros' deve ser um número inteiro positivo.")

    print("Inserindo registros financeiros...")
    connection = conectar_db()
    cursor = connection.cursor()
    for _ in range(qtd_registros):
        data_registro = datetime.now() - timedelta(days=random.randint(0, 365))
        receita = round(random.uniform(5000, 20000), 2)
        custos_fixos = round(random.uniform(1000, 5000), 2)
        custos_variaveis = round(random.uniform(500, 3000), 2)
        lucro_liquido = receita - (custos_fixos + custos_variaveis)
        dividas = round(random.uniform(0, 5000), 2)
        fluxo_caixa = lucro_liquido - dividas

        query = """
        INSERT INTO financeiro (data_registro, receita, custos_fixos, custos_variaveis, lucro_liquido, dividas, fluxo_caixa)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (data_registro, receita, custos_fixos, custos_variaveis, lucro_liquido, dividas, fluxo_caixa))

    connection.commit()
    cursor.close()
    connection.close()
    print("Registros financeiros inseridos com sucesso!")


def inserir_gastos_pessoais(qtd_registros=50):
    """
    Insere registros de gastos pessoais simulados.
    """
    print("Inserindo registros de gastos pessoais...")
    connection = conectar_db()
    cursor = connection.cursor()

    # Use o parâmetro qtd_registros corretamente dentro do loop
    for _ in range(qtd_registros):  # Corrigido: passando o parâmetro qtd_registros diretamente
        data_registro = datetime.now() - timedelta(days=random.randint(0, 365))
        receita_pessoal = round(random.uniform(2000, 10000), 2)
        gastos_fixos = round(random.uniform(500, 3000), 2)
        gastos_variaveis = round(random.uniform(300, 5000), 2)
        saldo_acumulado = receita_pessoal - (gastos_fixos + gastos_variaveis)

        query = """
        INSERT INTO gastos_pessoais (data_registro, receita_pessoal, gastos_fixos, gastos_variaveis, saldo_acumulado)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (data_registro, receita_pessoal, gastos_fixos, gastos_variaveis, saldo_acumulado))

    connection.commit()
    cursor.close()
    connection.close()
    print("Registros de gastos pessoais inseridos com sucesso!")



def inserir_vendas(qtd=30):
    print("Inserindo vendas...")
    connection = conectar_db()
    cursor = connection.cursor()

    for _ in range(qtd):
        cliente_id = random.randint(1, 30)
        valor_total = round(random.uniform(100, 2000), 2)
        status = random.choice(["pendente", "pago", "cancelado"])
        query = "INSERT INTO vendas (cliente_id, valor_total, status) VALUES (%s, %s, %s)"
        cursor.execute(query, (cliente_id, valor_total, status))

    connection.commit()
    cursor.close()
    connection.close()

def inserir_itens_venda(qtd=50):
    print("Inserindo itens de venda...")
    connection = conectar_db()
    cursor = connection.cursor()

    for _ in range(qtd):
        venda_id = random.randint(1, 30)
        produto_id = random.randint(1, 5)
        quantidade = random.randint(1, 5)
        preco_unitario = round(random.uniform(10, 500), 2)
        query = """
        INSERT INTO itens_venda (venda_id, produto_id, quantidade, preco_unitario)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (venda_id, produto_id, quantidade, preco_unitario))

    connection.commit()
    cursor.close()
    connection.close()

def inserir_logs(qtd=20):
    print("Inserindo logs...")
    connection = conectar_db()
    cursor = connection.cursor()

    for _ in range(qtd):
        usuario_id = random.randint(1, 30)
        acao = fake.sentence(nb_words=3)
        descricao = fake.text()
        query = "INSERT INTO logs (usuario_id, acao, descricao) VALUES (%s, %s, %s)"
        cursor.execute(query, (usuario_id, acao, descricao))

    connection.commit()
    cursor.close()
    connection.close()

def inserir_pagamentos(qtd_registros=50):
    print("Inserindo registros de pagamentos...")

    # Conectar ao banco de dados
    connection = conectar_db()
    cursor = connection.cursor()

    for _ in range(qtd_registros):
        # Aleatoriedade nos dados de pagamento
        venda_id = random.randint(1, 30)  # Relacionando ao id da venda
        valor_pago = round(random.uniform(50, 2000), 2)  # Valor pago
        metodo_pagamento = random.choice(["cartão de crédito", "dinheiro", "pix", "boleto"])  # Forma de pagamento
        data_pagamento = datetime.now() - timedelta(days=random.randint(1, 365))  # Data de pagamento aleatória
        status = random.choice(["pendente", "pago", "cancelado"])  # Status do pagamento

        # Query para inserir dados na tabela de pagamentos
        query = """
        INSERT INTO pagamentos (venda_id, valor_pago, metodo_pagamento, data_pagamento, status)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (venda_id, valor_pago, metodo_pagamento, data_pagamento, status))

    # Commit para salvar as mudanças e fechar a conexão
    connection.commit()
    cursor.close()
    connection.close()

    print(f"{qtd_registros} registros de pagamentos inseridos com sucesso!")



def main():
    inserir_usuarios()
    inserir_servicos()
    inserir_produtos()
    inserir_agendamentos()
    inserir_vendas()
    inserir_itens_venda()
    inserir_logs()
    inserir_financeiro()       
    inserir_gastos_pessoais()
    inserir_pagamentos()
    print("Banco de dados populado com sucesso!")

if __name__ == "__main__":
    main()
