from src.armazenamento import salvar_convidados
from src.config import STATUS_CONVIDADO
from src.utils import (
    limpar_tela,
    pausar,
    mostrar_titulo,
    ler_texto,
    ler_numero_inteiro,
    escolher_evento,
)


def convidados_do_evento(convidados, id_evento):
    lista = []
    for convidado in convidados:
        if convidado["id_evento"] == id_evento:
            lista.append(convidado)
    return lista


def contar_por_status(convidados, id_evento, status):
    total = 0
    for convidado in convidados_do_evento(convidados, id_evento):
        if convidado["status"] == status:
            total = total + 1
    return total


def ler_status():
    print("Status disponíveis:")
    for i in range(len(STATUS_CONVIDADO)):
        print(f"  {i + 1} - {STATUS_CONVIDADO[i]}")
    while True:
        opcao = ler_numero_inteiro("Escolha o status: ")
        if 1 <= opcao <= len(STATUS_CONVIDADO):
            return STATUS_CONVIDADO[opcao - 1]
        print("Opção inválida.")


def adicionar_convidado(evento, convidados):
    lista = convidados_do_evento(convidados, evento["id"])
    if len(lista) >= evento["convidados"]:
        print(f"Atenção: o evento já atingiu o limite previsto de {evento['convidados']} convidado(s).")
        confirmar = input("Deseja adicionar mesmo assim? (s/n): ")
        if confirmar.lower() != "s":
            print("Convidado não adicionado.")
            return

    nome = ler_texto("Nome do convidado: ")
    convidado = {
        "id_evento": evento["id"],
        "nome": nome,
        "status": "pendente"
    }
    convidados.append(convidado)
    salvar_convidados(convidados)
    print(f"'{nome}' adicionado(a) à lista como pendente!")


def listar_convidados(evento, convidados):
    lista = convidados_do_evento(convidados, evento["id"])
    if len(lista) == 0:
        print("Nenhum convidado cadastrado.")
        return lista

    etiquetas = {
        "confirmado": "[Confirmado]",
        "pendente": "[Pendente]",
        "recusado": "[Recusado]"
    }
    for i in range(len(lista)):
        etiqueta = etiquetas.get(lista[i]["status"], "[Pendente]")
        print(f"  {i + 1} - {etiqueta} {lista[i]['nome']}")
    return lista


def escolher_convidado(lista):
    while True:
        opcao = ler_numero_inteiro("Escolha o convidado (0 para voltar): ")
        if opcao == 0:
            return None
        if 1 <= opcao <= len(lista):
            return lista[opcao - 1]
        print("Opção inválida.")


def alterar_status_convidado(evento, convidados):
    lista = listar_convidados(evento, convidados)
    if len(lista) == 0:
        return
    convidado = escolher_convidado(lista)
    if convidado is not None:
        convidado["status"] = ler_status()
        salvar_convidados(convidados)
        print("Status do convidado atualizado!")


def remover_convidado(evento, convidados):
    lista = listar_convidados(evento, convidados)
    if len(lista) == 0:
        return
    convidado = escolher_convidado(lista)
    if convidado is not None:
        convidados.remove(convidado)
        salvar_convidados(convidados)
        print("Convidado removido da lista!")


def menu_convidados(eventos, convidados):
    limpar_tela()
    mostrar_titulo("LISTA DE CONVIDADOS")
    evento = escolher_evento(eventos)
    if evento is None:
        pausar()
        return

    while True:
        limpar_tela()
        mostrar_titulo("CONVIDADOS: " + evento["nome"])
        listar_convidados(evento, convidados)

        confirmados = contar_por_status(convidados, evento["id"], "confirmado")
        pendentes = contar_por_status(convidados, evento["id"], "pendente")
        recusados = contar_por_status(convidados, evento["id"], "recusado")
        print(f"\nResumo: {confirmados} confirmado(s) | {pendentes} pendente(s) | {recusados} recusado(s)")
        print(f"Capacidade prevista do evento: {evento['convidados']}")

        print("\n1 - Adicionar convidado")
        print("2 - Alterar confirmação (RSVP)")
        print("3 - Remover convidado")
        print("0 - Voltar")
        opcao = input("Opção: ")

        if opcao == "1":
            adicionar_convidado(evento, convidados)
            pausar()
        elif opcao == "2":
            alterar_status_convidado(evento, convidados)
            pausar()
        elif opcao == "3":
            remover_convidado(evento, convidados)
            pausar()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
            pausar()