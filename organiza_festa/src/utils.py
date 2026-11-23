import os
import datetime
from src.config import SEPARADOR, TIPOS_DE_EVENTO


def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def pausar():
    input("\nPressione ENTER para continuar...")


def mostrar_titulo(titulo):
    print("=" * 40)
    print("   " + titulo)
    print("=" * 40)


def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto == "":
            print("O campo não pode ficar vazio.")
        elif SEPARADOR in texto:
            print("Não use o caractere ';'.")
        else:
            return texto


def ler_numero_inteiro(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            if numero < 0:
                print("Digite um número positivo.")
            else:
                return numero
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")


def ler_valor(mensagem):
    while True:
        try:
            texto = input(mensagem).replace(",", ".")
            valor = float(texto)
            if valor < 0:
                print("O valor não pode ser negativo.")
            else:
                return valor
        except ValueError:
            print("Valor inválido! Exemplo: 1500.50")


def ler_data(mensagem):
    while True:
        texto = input(mensagem).strip()
        try:
            datetime.datetime.strptime(texto, "%d/%m/%Y")
            return texto
        except ValueError:
            print("Data inválida! Use o formato DD/MM/AAAA.")


def ler_tipo():
    print("Tipos disponíveis:")
    for i in range(len(TIPOS_DE_EVENTO)):
        print(f"  {i + 1} - {TIPOS_DE_EVENTO[i]}")
    while True:
        opcao = ler_numero_inteiro("Escolha o tipo: ")
        if 1 <= opcao <= len(TIPOS_DE_EVENTO):
            return TIPOS_DE_EVENTO[opcao - 1]
        print("Opção inválida.")


def formatar_dinheiro(valor):
    return f"R$ {valor:.2f}".replace(".", ",")


def dias_para_evento(data_texto):
    data_evento = datetime.datetime.strptime(data_texto, "%d/%m/%Y").date()
    hoje = datetime.date.today()
    diferenca = data_evento - hoje
    return diferenca.days


def escolher_evento(eventos):
    if len(eventos) == 0:
        print("Nenhum evento cadastrado.")
        return None
    for i in range(len(eventos)):
        print(f"  {i + 1} - {eventos[i]['nome']} ({eventos[i]['data']})")
    while True:
        opcao = ler_numero_inteiro("Escolha o evento (0 para voltar): ")
        if opcao == 0:
            return None
        if 1 <= opcao <= len(eventos):
            return eventos[opcao - 1]
        print("Opção inválida.")