from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27018/")
db = client["learning_machines"]
collection = db["feedbacks_sac"]

documents = [
    {
        "id_chamado": "SAC-001",
        "id_cliente": 1,
        "data_contato": "2026-05-13",
        "canal": "Aplicativo Mobile",
        "motivo": "Falha no Pix",
        "texto_mensagem": "Tentei fazer um Pix ontem à noite e o aplicativo travou na tela de senha. O dinheiro saiu da conta mas não chegou no destino. Preciso de ajuda urgente!",
        "nota_avaliacao": 1
    },
    {
        "id_chamado": "SAC-002",
        "id_cliente": 2,
        "data_contato": "2026-05-12",
        "canal": "Chat Online",
        "motivo": "Dúvida sobre Investimentos",
        "texto_mensagem": "Estou querendo investir no Tesouro Direto pelo app, mas não entendi a diferença entre prefixado e pós-fixado. Poderiam me ajudar?",
        "nota_avaliacao": 5
    },
    {
        "id_chamado": "SAC-003",
        "id_cliente": 3,
        "data_contato": "2026-05-13",
        "canal": "Telefone",
        "motivo": "Bloqueio de Cartão",
        "texto_mensagem": "Perdi meu cartão de crédito e gostaria de bloquear imediatamente. Onde encontro essa opção no aplicativo?",
        "nota_avaliacao": 4
    }
]

result = collection.insert_many(documents)

print("Documentos inseridos com sucesso: ", result.inserted_ids)