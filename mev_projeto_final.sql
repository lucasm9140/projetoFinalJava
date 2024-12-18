-- Banco de Dados para Sistema de Estética Automotiva

CREATE DATABASE IF NOT EXISTS mev_estetica_automotiva;
USE mev_estetica_automotiva;
DROP DATABASE mev_estetica_automotiva;

select * from usuarios;
select * from agendamentos;
select * from financeiro;
select * from gastos_pessoais;
select * from itens_venda;
select * from produtos;
select * from servicos;
select * from vendas;
select * from pagamentos; 
select * from logs;



delete from usuarios where id=(select MAX(id) from usuarios);

-- Tabela de Usuários
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    tipo ENUM('administrador', 'gerente', 'supervisor', 'funcionario', 'cliente') NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Serviços
CREATE TABLE servicos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    preco_base DECIMAL(10, 2) NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Produtos
CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10, 2) NOT NULL,
    estoque INT NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Agendamentos
CREATE TABLE agendamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    funcionario_id INT NOT NULL,
    servico_id INT NOT NULL,
    data_agendamento DATETIME NOT NULL,
    status ENUM('pendente', 'confirmado', 'cancelado', 'concluido') DEFAULT 'pendente',
    observacoes TEXT,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES usuarios(id),
    FOREIGN KEY (funcionario_id) REFERENCES usuarios(id),
    FOREIGN KEY (servico_id) REFERENCES servicos(id)
);

-- Tabela de Vendas
CREATE TABLE vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    valor_total DECIMAL(10, 2) NOT NULL,
    status ENUM('pendente', 'pago') DEFAULT 'pendente',
    FOREIGN KEY (cliente_id) REFERENCES usuarios(id)
);

-- Tabela de Itens da Venda
CREATE TABLE itens_venda (
    id INT AUTO_INCREMENT PRIMARY KEY,
    venda_id INT NOT NULL,
    produto_id INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (venda_id) REFERENCES vendas(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);

-- Tabela de Pagamentos
CREATE TABLE pagamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    agendamento_id INT,
    venda_id INT,
    valor_pago DECIMAL(10, 2) NOT NULL,
    metodo_pagamento ENUM('dinheiro', 'cartao_credito', 'cartao_debito', 'pix') NOT NULL,
    status ENUM('pendente', 'pago', 'estornado') DEFAULT 'pendente',
    data_pagamento DATETIME DEFAULT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (agendamento_id) REFERENCES agendamentos(id),
    FOREIGN KEY (venda_id) REFERENCES vendas(id)
);

ALTER TABLE pagamentos MODIFY metodo_pagamento VARCHAR(50);
ALTER TABLE pagamentos MODIFY status VARCHAR(20);

ALTER TABLE pagamentos
ADD COLUMN cliente_id INT;

ALTER TABLE pagamentos
ADD CONSTRAINT fk_cliente_id FOREIGN KEY (cliente_id) REFERENCES usuarios(id);


-- Tabela Financeiro (Para IA de Previsão de Falência)
CREATE TABLE financeiro (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_registro DATE NOT NULL,
    receita DECIMAL(10, 2) NOT NULL,
    custos_fixos DECIMAL(10, 2) NOT NULL,
    custos_variaveis DECIMAL(10, 2) NOT NULL,
    lucro_liquido DECIMAL(10, 2) NOT NULL,
    dividas DECIMAL(10, 2) NOT NULL,
    fluxo_caixa DECIMAL(10, 2) NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Gastos Pessoais (Para IA de Previsão de Gastos e Ganhos Futuros)
CREATE TABLE gastos_pessoais (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_registro DATE NOT NULL,
    receita_pessoal DECIMAL(10, 2) NOT NULL,
    gastos_fixos DECIMAL(10, 2) NOT NULL,
    gastos_variaveis DECIMAL(10, 2) NOT NULL,
    saldo_acumulado DECIMAL(10, 2) NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Logs (Opcional - Para Auditoria e Rastreamento)
CREATE TABLE logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    acao VARCHAR(255) NOT NULL,
    descricao TEXT,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

ALTER TABLE vendas ADD cidade_satelite VARCHAR(80);

