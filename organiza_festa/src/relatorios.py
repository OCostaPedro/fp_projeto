import random
from src.convidados import convidados_do_evento, contar_por_status
from src.tarefas import tarefas_do_evento, calcular_gasto
from src.utils import (
    limpar_tela,
    pausar,
    mostrar_titulo,
    formatar_dinheiro,
    escolher_evento,
)


def mostrar_sugestoes(eventos):
    limpar_tela()
    mostrar_titulo("SUGESTÕES")
    evento = escolher_evento(eventos)
    if evento is None:
        pausar()
        return
    tipo = evento["tipo"]
    convidados = evento["convidados"]
    if tipo == "aniversario":
        decoracoes = ["Balões coloridos", "Painel com fotos", "Tema neon", "Tema anos 80"]
        cardapios = ["Salgadinhos e bolo", "Hambúrguer artesanal", "Pizza e refrigerante"]
        atividades = ["Karaokê", "Caça ao tesouro", "Cabine de fotos", "Bingo"]
    elif tipo == "casamento":
        decoracoes = ["Flores brancas", "Estilo rústico", "Luzes penduradas", "Arranjos de mesa"]
        cardapios = ["Jantar completo", "Finger food", "Massas e risotos"]
        atividades = ["Banda ao vivo", "DJ", "Valsa dos noivos", "Cabine de fotos"]
    else:
        decoracoes = ["Ambiente simples e organizado", "Plantas na mesa", "Projetor e telão"]
        cardapios = ["Coffee break", "Café e biscoitos", "Lanche natural"]
        atividades = ["Dinâmica de apresentação", "Rodada de perguntas", "Brainstorm em grupo"]
    if convidados <= 20:
        tamanho = "pequeno"
        fornecedor = "Um buffet pequeno ou comida caseira já resolve."
    elif convidados <= 100:
        tamanho = "médio"
        fornecedor = "Vale contratar um buffet e pelo menos 2 garçons."
    else:
        tamanho = "grande"
        fornecedor = "Contrate um buffet completo, equipe de garçons e segurança."
    print(f"\nEvento: {evento['nome']} ({tipo}, {convidados} convidados - porte {tamanho})")
    print(f"\nFornecedores: {fornecedor}")
    print(f"Decoração sugerida: {random.choice(decoracoes)}")
    print(f"Cardápio sugerido: {random.choice(cardapios)}")
    print(f"Atividade sugerida: {random.choice(atividades)}")
    print("\n(Abra de novo para ver outras sugestões!)")
    pausar()


def mostrar_resumo(eventos, tarefas, convidados):
    limpar_tela()
    mostrar_titulo("RESUMO DO EVENTO")
    evento = escolher_evento(eventos)
    if evento is None:
        pausar()
        return
    lista = tarefas_do_evento(tarefas, evento["id"])
    total_tarefas = len(lista)
    feitas = 0
    for tarefa in lista:
        if tarefa["feita"]:
            feitas = feitas + 1
    gasto = calcular_gasto(tarefas, evento["id"])
    print(f"\nEvento: {evento['nome']}")
    if total_tarefas == 0:
        print("Nenhuma tarefa cadastrada ainda.")
    else:
        porcentagem = feitas * 100 // total_tarefas
        barra = "#" * (porcentagem // 10) + "-" * (10 - porcentagem // 10)
        print(f"Tarefas concluídas: {feitas} de {total_tarefas}")
        print(f"Progresso: [{barra}] {porcentagem}%")
    if evento["orcamento"] > 0:
        uso = gasto * 100 / evento["orcamento"]
        print(f"Orçamento usado: {round(uso, 1)}%")
        if uso > 100:
            print("Situação: orçamento ESTOURADO!")
        elif uso > 80:
            print("Situação: cuidado, o orçamento está quase no fim.")
        else:
            print("Situação: orçamento sob controle.")

    lista_convidados = convidados_do_evento(convidados, evento["id"])
    confirmados = contar_por_status(convidados, evento["id"], "confirmado")
    print(f"Lista de convidados: {confirmados} confirmado(s) de {len(lista_convidados)} cadastrado(s) (previsto: {evento['convidados']})")

    if evento["convidados"] > 0:
        por_pessoa = gasto / evento["convidados"]
        print(f"Custo previsto por convidado: {formatar_dinheiro(por_pessoa)}")
    if confirmados > 0:
        por_confirmado = gasto / confirmados
        print(f"Custo real por confirmado: {formatar_dinheiro(por_confirmado)}")
    pausar()