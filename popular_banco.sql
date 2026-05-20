-- Inserção de dados fictícios para fins de estudo e modelagem preditiva

-- 1. Inserir Clientes
INSERT INTO clientes (id, nome, email, idade, renda_mensal) VALUES
(1, 'João da Silva', 'joao.silva@email.com', 28, 3500.00),
(2, 'Maria Oliveira', 'maria.oliveira@email.com', 45, 8500.00),
(3, 'Pedro Santos', 'pedro.santos@email.com', 34, 2200.00),
(4, 'Ana Costa', 'ana.costa@email.com', 22, 1800.00),
(5, 'Carlos Rodrigues', 'carlos.rodrigues@email.com', 55, 12000.00),
(6, 'Beatriz Souza', 'beatriz.souza@email.com', 40, 6200.00),
(7, 'Lucas Lima', 'lucas.lima@email.com', 29, 2900.00),
(8, 'Juliana Alves', 'juliana.alves@email.com', 31, 4100.00);

-- 2. Inserir Contas Bancárias
INSERT INTO contas (id, tipo_conta, valor, id_cliente) VALUES
(1, 'Corrente', 150.50, 1),
(2, 'Poupança', 25000.00, 2),
(3, 'Corrente', -80.00, 3),        -- Saldo negativo (potencial inadimplente)
(4, 'Corrente', 12.00, 4),         -- Saldo muito baixo
(5, 'Corrente', 8500.00, 5),
(6, 'Poupança', 1200.00, 6),
(7, 'Corrente', 300.00, 7),
(8, 'Corrente', 1500.00, 8);

-- 3. Inserir Histórico de Empréstimos
-- O campo status_pagamento será usado na Fase 3 para definir a inadimplência (alvo)
INSERT INTO historico_emprestimos (id, valor, quantidade_parcelas, status_pagamento, id_cliente, id_conta) VALUES
(1, 5000.00, 12, 'Pago', 1, 1),
(2, 20000.00, 48, 'Pago', 2, 2),
(3, 4000.00, 12, 'Em Atraso', 3, 3), -- Inadimplente
(4, 1500.00, 6, 'Em Atraso', 4, 4),  -- Inadimplente
(5, 50000.00, 60, 'Pago', 5, 5),
(6, 10000.00, 24, 'Pago', 6, 6),
(7, 3000.00, 12, 'Em Atraso', 7, 7), -- Inadimplente
(8, 8000.00, 24, 'Pago', 8, 8);
