import os
from src.config import (
    PASTA_DADOS,
    ARQUIVO_EVENTOS,
    ARQUIVO_TAREFAS,
    ARQUIVO_CONVIDADOS,
    SEPARADOR,
)


def carregar_eventos():
    eventos = []
    try:
        arquivo = open(ARQUIVO_EVENTOS, "r", encoding="utf-8")
        for linha in arquivo:
            linha = linha.strip()
            if linha == "":
                continue
            partes = linha.split(SEPARADOR)
            evento = {
                "id": int(partes[0]),
                "nome": partes[1],
                "tipo": partes[2],
                "data": partes[3],
                "local": partes[4],
                "orcamento": float(partes[5]),
                "convidados": int(partes[6])
            }
            eventos.append(evento)
        arquivo.close()
    except FileNotFoundError:
        pass
    except ValueError:
        print("Aviso: o arquivo de eventos tem algum valor com erro.")
    except IndexError:
        print("Aviso: o arquivo de eventos tem alguma linha incompleta.")
    return eventos


def salvar_eventos(eventos):
    try:
        os.makedirs(PASTA_DADOS, exist_ok=True)
        arquivo = open(ARQUIVO_EVENTOS, "w", encoding="utf-8")
        for evento in eventos:
            linha = (str(evento["id"]) + SEPARADOR + evento["nome"] + SEPARADOR +
                     evento["tipo"] + SEPARADOR + evento["data"] + SEPARADOR +
                     evento["local"] + SEPARADOR + str(evento["orcamento"]) + SEPARADOR +
                     str(evento["convidados"]))
            arquivo.write(linha + "\n")
        arquivo.close()
    except OSError:
        print("Erro ao salvar o arquivo de eventos!")


def carregar_tarefas():
    tarefas = []
    try:
        arquivo = open(ARQUIVO_TAREFAS, "r", encoding="utf-8")
        for linha in arquivo:
            linha = linha.strip()
            if linha == "":
                continue
            partes = linha.split(SEPARADOR)
            tarefa = {
                "id_evento": int(partes[0]),
                "descricao": partes[1],
                "custo": float(partes[2]),
                "feita": False
            }
            if partes[3] == "sim":
                tarefa["feita"] = True
            tarefas.append(tarefa)
        arquivo.close()
    except FileNotFoundError:
        pass
    except ValueError:
        print("Aviso: o arquivo de tarefas tem algum valor com erro.")
    except IndexError:
        print("Aviso: o arquivo de tarefas tem alguma linha incompleta.")
    return tarefas


def salvar_tarefas(tarefas):
    try:
        os.makedirs(PASTA_DADOS, exist_ok=True)
        arquivo = open(ARQUIVO_TAREFAS, "w", encoding="utf-8")
        for tarefa in tarefas:
            if tarefa["feita"]:
                feita = "sim"
            else:
                feita = "nao"
            linha = (str(tarefa["id_evento"]) + SEPARADOR + tarefa["descricao"] +
                     SEPARADOR + str(tarefa["custo"]) + SEPARADOR + feita)
            arquivo.write(linha + "\n")
        arquivo.close()
    except OSError:
        print("Erro ao salvar o arquivo de tarefas!")


def carregar_convidados():
    convidados = []
    try:
        arquivo = open(ARQUIVO_CONVIDADOS, "r", encoding="utf-8")
        for linha in arquivo:
            linha = linha.strip()
            if linha == "":
                continue
            partes = linha.split(SEPARADOR)
            convidado = {
                "id_evento": int(partes[0]),
                "nome": partes[1],
                "status": partes[2]
            }
            convidados.append(convidado)
        arquivo.close()
    except FileNotFoundError:
        pass
    except ValueError:
        print("Aviso: o arquivo de convidados tem algum valor com erro.")
    except IndexError:
        print("Aviso: o arquivo de convidados tem alguma linha incompleta.")
    return convidados


def salvar_convidados(convidados):
    try:
        os.makedirs(PASTA_DADOS, exist_ok=True)
        arquivo = open(ARQUIVO_CONVIDADOS, "w", encoding="utf-8")
        for convidado in convidados:
            linha = (str(convidado["id_evento"]) + SEPARADOR +
                     convidado["nome"] + SEPARADOR + convidado["status"])
            arquivo.write(linha + "\n")
        arquivo.close()
    except OSError:
        print("Erro ao salvar o arquivo de convidados!")