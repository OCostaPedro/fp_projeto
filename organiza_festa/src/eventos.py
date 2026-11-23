from src.armazenamento import salvar_eventos, salvar_tarefas, salvar_convidados
from src.convidados import convidados_do_evento
from src.tarefas import tarefas_do_evento, calcular_gasto
from src.utils import (
    limpar_tela,
    pausar,
    mostrar_titulo,
    ler_texto,
    ler_numero_inteiro,
    ler_valor,
    ler_data,
    ler_tipo,
    formatar_dinheiro,
    dias_para_evento,
    escolher_evento,
)


def gerar_novo_id(eventos):
    maior = 0
    for evento in eventos:
        if evento["id"] > maior:
            maior = evento["id"]
    return maior + 1


def cadastrar_evento(eventos):
    limpar_tela()
    mostrar_titulo("NOVO EVENTO")
    nome = ler_texto("Nome do evento: ")
    tipo = ler_tipo()
    data = ler_data("Data (DD/MM/AAAA): ")
    local = ler_texto("Local: ")
    orcamento = ler_valor("Orçamento disponível: R$ ")
    convidados = ler_numero_inteiro("Número de convidados: ")

    evento = {
        "id": gerar_novo_id(eventos),
        "nome": nome,
        "tipo": tipo,
        "data": data,
        "local": local,
        "orcamento": orcamento,
        "convidados": convidados
    }
    eventos.append(evento)
    salvar_eventos(eventos)
    print("\nEvento cadastrado com sucesso!")
    pausar()


def mostrar_evento(evento, tarefas):
    gasto = calcular_gasto(tarefas, evento["id"])
    disponivel = evento["orcamento"] - gasto
    dias = dias_para_evento(evento["data"])

    print(f"\nNome: {evento['nome']}")
    print(f"Tipo: {evento['tipo']}")
    print(f"Data: {evento['data']}")
    print(f"Local: {evento['local']}")
    print(f"Convidados: {evento['convidados']}")
    print(f"Orçamento total: {formatar_dinheiro(evento['orcamento'])}")
    print(f"Gasto com tarefas: {formatar_dinheiro(gasto)}")
    print(f"Orçamento disponível: {formatar_dinheiro(disponivel)}")

    if disponivel < 0:
        print("ATENÇÃO: o orçamento foi ultrapassado!")

    if dias > 1:
        print(f"Faltam {dias} dias para o evento!")
    elif dias == 1:
        print("O evento é AMANHÃ!")
    elif dias == 0:
        print("O evento é HOJE!")
    else:
        print(f"Esse evento já aconteceu há {-dias} dia(s).")


def listar_eventos(eventos, tarefas):
    limpar_tela()
    mostrar_titulo("MEUS EVENTOS")
    evento = escolher_evento(eventos)
    if evento is not None:
        mostrar_evento(evento, tarefas)
    pausar()


def editar_evento(eventos):
    limpar_tela()
    mostrar_titulo("EDITAR EVENTO")
    evento = escolher_evento(eventos)
    if evento is None:
        pausar()
        return

    print("\nO que deseja editar?")
    print("1 - Nome")
    print("2 - Tipo")
    print("3 - Data")
    print("4 - Local")
    print("5 - Orçamento")
    print("6 - Número de convidados")
    opcao = input("Opção: ")

    if opcao == "1":
        evento["nome"] = ler_texto("Novo nome: ")
    elif opcao == "2":
        evento["tipo"] = ler_tipo()
    elif opcao == "3":
        evento["data"] = ler_data("Nova data (DD/MM/AAAA): ")
    elif opcao == "4":
        evento["local"] = ler_texto("Novo local: ")
    elif opcao == "5":
        evento["orcamento"] = ler_valor("Novo orçamento: R$ ")
    elif opcao == "6":
        evento["convidados"] = ler_numero_inteiro("Novo número de convidados: ")
    else:
        print("Opção inválida.")
        pausar()
        return

    salvar_eventos(eventos)
    print("\nEvento atualizado!")
    pausar()


def excluir_evento(eventos, tarefas, convidados):
    limpar_tela()
    mostrar_titulo("EXCLUIR EVENTO")
    evento = escolher_evento(eventos)
    if evento is None:
        pausar()
        return

    confirmar = input(f"Tem certeza que deseja excluir '{evento['nome']}'? (s/n): ")
    if confirmar.lower() != "s":
        print("Exclusão cancelada.")
        pausar()
        return

    eventos.remove(evento)

    for tarefa in tarefas_do_evento(tarefas, evento["id"]):
        tarefas.remove(tarefa)

    for convidado in convidados_do_evento(convidados, evento["id"]):
        convidados.remove(convidado)

    salvar_eventos(eventos)
    salvar_tarefas(tarefas)
    salvar_convidados(convidados)
    print("Evento excluído!")
    pausar()