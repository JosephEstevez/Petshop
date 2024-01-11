-- Cliente
CREATE TABLE Cliente (
    id_cliente INT PRIMARY KEY,
    nome_do_cliente VARCHAR(0),
    endereco VARCHAR(0),
    telefone VARCHAR(0)
);

-- Pet
CREATE TABLE Pet (
    id_pet INT PRIMARY KEY,
    nome_do_pet VARCHAR(0),
    especie VARCHAR(0),
    raca VARCHAR(0),
    idade INT,
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

-- Consulta_Veterinaria
CREATE TABLE ConsultaVeterinaria (
    id_consulta INT PRIMARY KEY,
    id_pet INT,
    data_da_consulta DATE,
    diagnostico TEXT,
    FOREIGN KEY (id_pet) REFERENCES Pet(id_pet)
);

-- Produto
CREATE TABLE Produto (
    id_produto INT PRIMARY KEY,
    nome_do_produto VARCHAR(0),
    preco DECIMAL(10, 2)
);

-- Compra
CREATE TABLE Compra (
    id_compra INT PRIMARY KEY,
    id_item INT,
    id_produto INT,
    id_cliente INT,
    data_da_compra DATE,
    valor_total DECIMAL(10, 2),
    FOREIGN KEY (id_item) REFERENCES Item(id_item),
    FOREIGN KEY (id_produto) REFERENCES Produto(id_produto),
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

-- Item
CREATE TABLE Item (
    id_item INT PRIMARY KEY,
    quantidade INT,
    preco DECIMAL(10, 2)
);

-- Funcionario
CREATE TABLE Funcionario (
    id_funcionario INT PRIMARY KEY,
    nome_do_funcionario VARCHAR(0),
    cargo VARCHAR(0),
    salario DECIMAL(10, 2)
);

-- Agendamento_Banho
CREATE TABLE AgendamentoBanho (
    id_agendamento INT PRIMARY KEY,
    id_pet INT,
    data_do_agendamento DATE,
    tipo_do_banho VARCHAR(0),
    FOREIGN KEY (id_pet) REFERENCES Pet(id_pet)
);

-- Servico_Adicional
CREATE TABLE ServicoAdicional (
    id_servico INT PRIMARY KEY,
    nome_do_servico VARCHAR(0),
    preco DECIMAL(10, 2)
);

-- Servico_Pet
CREATE TABLE ServicoPet (
    id_servico INT PRIMARY KEY,
    id_pet INT,
    id_servico_adicional INT,
    data_do_servico DATE,
    FOREIGN KEY (id_pet) REFERENCES Pet(id_pet),
    FOREIGN KEY (id_servico_adicional) REFERENCES ServicoAdicional(id_servico)
);

-- Banho_Cortesia
CREATE TABLE BanhoCortesia (
    id_banho_cortesia INT PRIMARY KEY,
    id_pet INT,
    data_do_banho_cortesia DATE,
    FOREIGN KEY (id_pet) REFERENCES Pet(id_pet)
);
