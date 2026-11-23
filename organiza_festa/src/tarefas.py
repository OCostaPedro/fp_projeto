from src.armazenamento import salvar_tarefas
from src.utils import (
    limpar_tela,
    pausar,
    mostrar_titulo,
    ler_texto,
    ler_numero_inteiro,
    ler_valor,
    formatar_dinheiro,
    escolher_evento,
)


def tarefas_do_evento(tarefas, id_evento):
    lista = []
    for tarefa in tarefas:
        if tarefa["id_evento"] == id_evento:
            lista.append(tarefa)
    return lista


def calcular_gasto(tarefas, id_evento):
    total = 0
    for tarefa in tarefas_do_evento(tarefas, id_evento):
        total = total + tarefa["custo"]
    return total


def adicionar_tarefa(evento, tarefas):
    descricao = ler_texto("Descrição da tarefa (ex: buffet): ")
    custo = ler_valor("Custo da tarefa: R$ ")
    disponivel = evento["orcamento"] - calcular_gasto(tarefas, evento["id"])
    if custo > disponivel:
        print(f"Atenção: essa tarefa passa do orçamento disponível ({formatar_dinheiro(disponivel)}).")
        confirmar = input("Deseja adicionar mesmo assim? (s/n): ")
        if confirmar.lower() != "s":
            print("Tarefa não adicionada.")
            return
    tarefa = {
        "id_evento": evento["id"],
        "descricao": descricao,
        "custo": custo,
        "feita": False
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    novo_disponivel = disponivel - custo
    print(f"Tarefa adicionada! Orçamento disponível agora: {formatar_dinheiro(novo_disponivel)}")


def listar_tarefas(evento, tarefas):
    lista = tarefas_do_evento(tarefas, evento["id"])
    if len(lista) == 0:
        print("Nenhuma tarefa cadastrada.")
        return lista
    for i in range(len(lista)):
        if lista[i]["feita"]:
            marcador = "[X]"
        else:
            marcador = "[ ]"
        print(f"  {i + 1} - {marcador} {lista[i]['descricao']} - {formatar_dinheiro(lista[i]['custo'])}")
    return lista


def escolher_tarefa(lista):
    while True:
        opcao = ler_numero_inteiro("Escolha a tarefa (0 para voltar): ")
        if opcao == 0:
            return None
        if 1 <= opcao <= len(lista):
            return lista[opcao - 1]
        print("Opção inválida.")


def marcar_tarefa_feita(evento, tarefas):
    lista = listar_tarefas(evento, tarefas)
    if len(lista) == 0:
        return
    tarefa = escolher_tarefa(lista)
    if tarefa is not None:
        if tarefa["feita"]:
            tarefa["feita"] = False
        else:
            tarefa["feita"] = True
        salvar_tarefas(tarefas)
        print("Status da tarefa atualizado!")


def remover_tarefa(evento, tarefas):
    lista = listar_tarefas(evento, tarefas)
    if len(lista) == 0:
        return
    tarefa = escolher_tarefa(lista)
    if tarefa is not None:
        tarefas.remove(tarefa)
        salvar_tarefas(tarefas)
        print("Tarefa removida! O valor voltou para o orçamento.")


def menu_tarefas(eventos, tarefas):
    limpar_tela()
    mostrar_titulo("TAREFAS DO EVENTO")
    evento = escolher_evento(eventos)
    if evento is None:
        pausar()
        return
    while True:
        limpar_tela()
        mostrar_titulo("TAREFAS: " + evento["nome"])
        listar_tarefas(evento, tarefas)
        disponivel = evento["orcamento"] - calcular_gasto(tarefas, evento["id"])
        print(f"\nOrçamento disponível: {formatar_dinheiro(disponivel)}")
        print("\n1 - Adicionar tarefa")
        print("2 - Marcar/desmarcar tarefa como feita")
        print("3 - Remover tarefa")
        print("0 - Voltar")
        opcao = input("Opção: ")
        if opcao == "1":
            adicionar_tarefa(evento, tarefas)
            pausar()
        elif opcao == "2":
            marcar_tarefa_feita(evento, tarefas)
            pausar()
        elif opcao == "3":
            remover_tarefa(evento, tarefas)
            pausar()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
            pausar()