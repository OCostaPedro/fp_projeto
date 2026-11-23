from src.armazenamento import carregar_eventos, carregar_tarefas, carregar_convidados
from src.convidados import menu_convidados
from src.eventos import cadastrar_evento, listar_eventos, editar_evento, excluir_evento
from src.relatorios import mostrar_sugestoes, mostrar_resumo
from src.tarefas import menu_tarefas
from src.utils import limpar_tela, pausar, mostrar_titulo


def menu_principal():
    eventos = carregar_eventos()
    tarefas = carregar_tarefas()
    convidados = carregar_convidados()
    while True:
        limpar_tela()
        mostrar_titulo("ORGANIZA FESTA")
        print("1 - Cadastrar evento")
        print("2 - Ver eventos")
        print("3 - Editar evento")
        print("4 - Excluir evento")
        print("5 - Tarefas e orçamento")
        print("6 - Sugestões para o evento")
        print("7 - Resumo do evento")
        print("8 - Lista de convidados (RSVP)")
        print("0 - Sair")
        opcao = input("\nEscolha uma opção: ")
        if opcao == "1":
            cadastrar_evento(eventos)
        elif opcao == "2":
            listar_eventos(eventos, tarefas)
        elif opcao == "3":
            editar_evento(eventos)
        elif opcao == "4":
            excluir_evento(eventos, tarefas, convidados)
        elif opcao == "5":
            menu_tarefas(eventos, tarefas)
        elif opcao == "6":
            mostrar_sugestoes(eventos)
        elif opcao == "7":
            mostrar_resumo(eventos, tarefas, convidados)
        elif opcao == "8":
            menu_convidados(eventos, convidados)
        elif opcao == "0":
            print("Até a próxima festa!")
            break
        else:
            print("Opção inválida!")
            pausar()


if __name__ == "__main__":
    menu_principal()