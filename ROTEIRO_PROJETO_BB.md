# 🏛️ Projeto de Estudos: DataBank Analytics
**Guia Prático para o Concurso do Banco do Brasil (TI)**

Este roteiro foi planejado para mapear os tópicos do edital do Banco do Brasil (Tecnologia da Informação) em um projeto prático de ponta a ponta. Ao desenvolver este projeto, você consolidará conceitos teóricos de **Machine Learning**, **Bancos de Dados (SQL e NoSQL)**, **Big Data**, **Análise de Dados com Python** e **Estruturas de Dados**.

---

## 🎯 Objetivo do Projeto
Construir um pipeline de dados e inteligência artificial para um banco digital simulado, passando pela ingestão de dados de clientes, processamento, previsão de risco de crédito (inadimplência), clusterização de perfis e análise de sentimentos do atendimento ao cliente (SAC).

---

## 🗺️ Roteiro Passo a Passo e Mapeamento do Edital

### Fase 1: Banco de Dados e Ingestão 🗄️
**Objetivo:** Configurar as bases de dados e modelar o armazenamento.

- [x] **1.1. PostgreSQL (Modelo Relacional):**
  - Suba um banco PostgreSQL local.
  - Modele e crie tabelas para clientes, contas e histórico de empréstimos.
  - *Foco de estudo:* Normalização (1FN, 2FN, 3FN), chaves primárias e estrangeiras, comandos DDL e DML em SQL.
- [x] **1.2. MongoDB (NoSQL Documento):**
  - Suba um banco MongoDB local.
  - Crie uma coleção para armazenar documentos JSON contendo históricos de chats/feedbacks do SAC e logs de cliques no app.
  - *Foco de estudo:* Conceito de bancos baseados em documentos, esquema dinâmico e chave/valor.

> [!IMPORTANT]
> **Conexão com o Edital:** Banco de dados NoSQL (MongoDB, conceitos de grafos/colunas/documentos); SGBD; Modelagem Entidade-Relacionamento; PostgreSQL; SQL2008.

---

### Fase 2: Preparação e Exploração dos Dados (Analytics) 📊
**Objetivo:** Consumir os dados dos bancos, limpá-los e gerar *insights* visuais.

- [x] **2.1. Conexão e Ingestão com Python:**
  - Crie scripts Python (versão 3.9+) utilizando bibliotecas como `sqlalchemy`/`psycopg2` e `pymongo` para extrair os dados.
- [x] **2.2. Limpeza com Pandas e NumPy:**
  - Converta os dados extraídos em `DataFrames`.
  - Trate valores ausentes (`.fillna()`, `.dropna()`), remova duplicatas e converta tipos de colunas.
- [ ] **2.3. Análise Exploratória (EDA):**
  - Utilize o **Matplotlib** para plotar gráficos de distribuição de renda, taxas de inadimplência por idade e volume de chamados no SAC.

> [!TIP]
> **Conexão com o Edital:** Python 3.9.X aplicada para Analytics; Bibliotecas Pandas, NumPy e Matplotlib; Big Data (Preparação e apresentação de dados).
> **Dica de Prova:** Memorize os métodos mais comuns do Pandas para fatiamento (`.loc`, `.iloc`) e agregação (`.groupby`).

---

### Fase 3: Machine Learning - Aprendizado Supervisionado 🤖
**Objetivo:** Criar um modelo preditivo para classificar se um cliente pagará ou não um empréstimo (Risco de Crédito).

- [ ] **3.1. Divisão dos Dados:**
  - Isole a variável alvo (`inadimplente: 0 ou 1`) e as *features* preditivas.
  - Divida os dados usando `train_test_split` da biblioteca **Scikit-learn**.
- [ ] **3.2. Treinamento de Modelos:**
  - Treine um modelo de **Regressão Logística** e uma **Árvore de Decisão** (`DecisionTreeClassifier`).
- [ ] **3.3. Avaliação de Métricas:**
  - Calcule e interprete a Matriz de Confusão, Acurácia, Precisão e Recall. Entenda o impacto do Falso Negativo (aprovar crédito para quem não vai pagar).

> [!NOTE]
> **Conexão com o Edital:** Aprendizagem de máquina: Fundamentos básicos; Noções de algoritmos supervisionados; Python para IA/ML (Scikit-learn).

---

### Fase 4: Machine Learning - Aprendizado Não Supervisionado 🔍
**Objetivo:** Descobrir perfis e padrões ocultos na base de clientes sem usar uma variável alvo.

- [ ] **4.1. Seleção de Features:**
  - Selecione colunas puramente comportamentais (ex: saldo médio, movimentação mensal, uso de cartão).
- [ ] **4.2. Agrupamento (Clustering):**
  - Aplique o algoritmo **K-Means** (do `scikit-learn`) para criar grupos de clientes (ex: $K=3$).
- [ ] **4.3. Análise dos Perfis:**
  - Analise os centróides para rotular os grupos (ex: *Perfil Conservador*, *Perfil Digital*, *Perfil de Alto Risco*).

> [!NOTE]
> **Conexão com o Edital:** Algoritmos de aprendizado não supervisionados; Scikit-learn e SciPy.

---

### Fase 5: Processamento de Linguagem Natural (PLN) 💬
**Objetivo:** Analisar automaticamente o teor das mensagens deixadas no SAC (MongoDB).

- [ ] **5.1. Pré-processamento de Texto:**
  - Extraia os textos, passe para minúsculas, remova pontuações e *stop words* em português.
- [ ] **5.2. Vetorização:**
  - Transforme o texto em vetores numéricos usando **Bag of Words** (`CountVectorizer`) ou **TF-IDF** (`TfidfVectorizer`).
- [ ] **5.3. Análise de Sentimento Simples:**
  - Treine um classificador simples para categorizar a mensagem como *Positiva*, *Neutra* ou *Reclamação Crítica*.

> [!NOTE]
> **Conexão com o Edital:** Noções de processamento de linguagem natural (PLN).

---

### 💡 Bônus: Estruturas de Dados e Algoritmos
Para cobrir o **Item 5 do Edital**, crie um módulo à parte no projeto (`algoritmos_estudo.py`) contendo implementações puras em Python:

- [ ] **Busca Binária:** Implemente a busca binária em um array ordenado de IDs de clientes para simular uma consulta rápida.
- [ ] **Algoritmos de Ordenação:** Implemente o **Bubble Sort** e o **Insertion Sort** para ordenar uma lista de transações e compare a lógica com os métodos nativos do Python.
- [ ] **Estruturas Lineares e Árvores:** Crie classes simples simulando o funcionamento de uma **Pilha** (LIFO - para histórico de navegação), uma **Fila** (FIFO - para fila de atendimento de chamados do banco) e nós de uma **Árvore Binária**.

---

## 🔗 Sugestões de Datasets Gratuitos

Para alimentar seu projeto, utilize os seguintes portais:
1. **Risco de Crédito:** [Kaggle - German Credit Risk](https://www.kaggle.com/datasets/uciml/german-credit) ou [Default of Credit Card Clients](https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset).
2. **Segmentação Bancária:** [Bank Marketing Dataset (UCI)](https://archive.ics.uci.edu/ml/datasets/bank+marketing).
3. **PLN em Português:** Datasets de reviews do B2W/Olist no Kaggle para simular o SAC.

---
*Bons estudos! Use este arquivo para guiar seu código e marcar os checkboxes conforme for avançando.*
