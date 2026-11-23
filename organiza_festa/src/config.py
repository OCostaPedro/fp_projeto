import os

PASTA_DADOS = "data"
ARQUIVO_EVENTOS = os.path.join(PASTA_DADOS, "eventos.csv")
ARQUIVO_TAREFAS = os.path.join(PASTA_DADOS, "tarefas.csv")
ARQUIVO_CONVIDADOS = os.path.join(PASTA_DADOS, "convidados.csv")
SEPARADOR = ";"

TIPOS_DE_EVENTO = ["aniversario", "casamento", "reuniao"]
STATUS_CONVIDADO = ["pendente", "confirmado", "recusado"]