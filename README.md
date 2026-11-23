# Organiza Festa — Sistema de Planejamento de Eventos

> Projeto desenvolvido para a disciplina de Fundamentos de Programação.

## Sobre o Projeto

Cláudia adora organizar festas e eventos, mas enfrenta dificuldades para controlar convidados, datas, fornecedores, orçamento e tarefas antes do grande dia. O **Organiza Festa** é um sistema de linha de comando (CLI) desenvolvido em **Python puro** para ajudar Cláudia — e qualquer outro organizador — a planejar eventos de forma prática, organizada e dentro do prazo e do orçamento.

## Requisitos Atendidos

### Requisitos Funcionais

- **CRUD de Eventos:** Cadastro, visualização detalhada, edição por campo e exclusão de eventos com nome, tipo (`aniversario`, `casamento` ou `reuniao`), data, local, orçamento disponível e número previsto de convidados.

- **Tarefas e Orçamento:** Cadastro de tarefas com custos individuais que são descontados automaticamente do orçamento disponível do evento, possibilidade de marcar/desmarcar tarefas como concluídas e remoção de itens com estorno automático para o saldo.

- **Contagem Regressiva:** Exibição automática de quantos dias faltam para o evento acontecer (além de avisos quando o evento é amanhã, hoje ou já ocorreu).

- **Armazenamento de Dados:** Persistência automática de eventos, tarefas e convidados em arquivos `.csv`, garantindo que o histórico continue disponível a cada execução.

- **Sugestões Personalizadas:** Recomendações dinâmicas de fornecedores, decoração, cardápio e atividades geradas de acordo com o tipo do evento e o porte baseado na quantidade de convidados.

- **Funcionalidades Extras:**
  - **Lista de Convidados com Controle de Presença (RSVP):** Cadastro de convidados vinculados a cada evento com controle de status (`pendente`, `confirmado` e `recusado`), alerta ao atingir a capacidade planejada e exclusão em cascata quando o evento é removido.

  - **Resumo do Evento (Painel de Progresso):** Barra de progresso visual das tarefas concluídas, percentual de utilização do orçamento com diagnóstico financeiro (`sob controle`, `quase no fim` ou `estourado`), contagem de confirmações e cálculo do custo previsto por convidado e do custo real por convidado confirmado.

### Requisitos Não Funcionais

- **Python Puro (CLI):** Desenvolvido inteiramente em Python para execução no terminal, utilizando exclusivamente bibliotecas nativas autorizadas (`os`, `datetime` e `random`).

- **Organização e Modularização:** Código separado por responsabilidade em módulos dentro do pacote `src/`, com funções específicas para evitar repetição e manter alta legibilidade.

- **Tratamento de Exceções:** Uso de blocos `try/except` para validar entradas do usuário (`ValueError`) e tratar falhas na leitura e gravação de arquivos (`FileNotFoundError`, `IndexError`, `OSError`), evitando interrupções inesperadas.

- **Manual do Usuário:** Documentação completa de uso e restrições integrada a este `README.md`.

## Estrutura do Projeto

```
organiza_festa/
├── data/                    # Criada automaticamente ao salvar os primeiros registros
│   ├── eventos.csv          # Dados dos eventos cadastrados
│   ├── tarefas.csv          # Tarefas e custos vinculados aos eventos
│   └── convidados.csv       # Lista de convidados e status de confirmação (RSVP)
├── src/
│   ├── __init__.py          # Define src como um pacote Python
│   ├── config.py            # Constantes globais, caminhos de arquivos e opções válidas
│   ├── utils.py             # Limpeza de tela, validações de entrada, formatação e datas
│   ├── armazenamento.py     # Leitura e escrita dos arquivos CSV com tratamento de erros
│   ├── eventos.py           # CRUD de eventos e exclusão em cascata
│   ├── tarefas.py           # Gerenciamento de tarefas e cálculos de orçamento
│   ├── convidados.py        # Gerenciamento da lista de convidados (RSVP)
│   └── relatorios.py        # Sugestões personalizadas e resumo do evento
├── main.py                  # Ponto de entrada e menu principal da aplicação
└── README.md                # Documentação e Manual do Usuário

```

## Pré-requisitos e Como Executar

### Pré-requisitos

- **Python 3.8 ou superior** instalado no computador.

- Não é necessário instalar pacotes via `pip`.

### Passo a passo

1. Clone o repositório:

   ```
   git clone https://github.com/OCostaPedro/fp_projeto.git

   ```

2. Acesse a pasta da aplicação no terminal:

   ```
   cd fp_projeto/organiza_festa

   ```

3. Execute o arquivo principal:

   ```
   python main.py

   ```

   _(Em sistemas Linux ou macOS, utilize `python3 main.py` caso necessário.)_

## Manual do Usuário

Ao iniciar o sistema, o menu principal é exibido no terminal:

```
========================================
   ORGANIZA FESTA
========================================
1 - Cadastrar evento
2 - Ver eventos
3 - Editar evento
4 - Excluir evento
5 - Tarefas e orçamento
6 - Sugestões para o evento
7 - Resumo do evento
8 - Lista de convidados (RSVP)
0 - Sair

```

Digite o número correspondente à ação desejada e pressione **Enter**. Em listas de seleção (eventos, tarefas ou convidados), digite `0` a qualquer momento para retornar ao menu anterior.

### 1. Cadastrar evento

Permite registrar um novo evento informando:

- **Nome do evento** (ex.: `Aniversário da Cláudia`);

- **Tipo do evento**, escolhido por número: `1 - aniversario`, `2 - casamento` ou `3 - reuniao`;

- **Data**, no formato `DD/MM/AAAA` (ex.: `15/12/2026`);

- **Local** (ex.: `Salão Primavera`);

- **Orçamento disponível**, em reais (ex.: `5000.00` ou `5000,00`);

- **Número previsto de convidados** (número inteiro positivo).

Os dados são salvos automaticamente em `data/eventos.csv`.

### 2. Ver eventos

Lista todos os eventos cadastrados com suas respectivas datas. Ao selecionar um evento, o sistema mostra:

- Dados gerais (nome, tipo, data, local e convidados previstos);

- Resumo financeiro (orçamento total, gasto acumulado em tarefas e orçamento disponível);

- Alerta automático caso o orçamento tenha sido ultrapassado;

- **Contagem regressiva** indicando quantos dias faltam para o evento, se é amanhã, se é hoje ou há quantos dias já ocorreu.

### 3. Editar evento

Permite selecionar um evento existente e alterar individualmente qualquer um dos seus campos:

1. Nome

2. Tipo

3. Data

4. Local

5. Orçamento

6. Número de convidados

A alteração é gravada imediatamente no arquivo de eventos.

### 4. Excluir evento

Seleciona um evento e solicita confirmação (`s/n`) antes de excluí-lo. Confirmada a exclusão, o evento e **todas as tarefas e convidados associados a ele** são removidos definitivamente dos arquivos `.csv`.

### 5. Tarefas e orçamento

Após selecionar o evento, abre o submenu de gestão de tarefas exibindo a lista atual (com `[ ]` para pendente e `[X]` para concluída) e o saldo restante do orçamento:

- **`1 - Adicionar tarefa`:** Solicita descrição e custo. Se o valor ultrapassar o orçamento disponível, o sistema exibe um alerta e pergunta se deseja continuar mesmo assim (`s/n`).

- **`2 - Marcar/desmarcar tarefa como feita`:** Alterna o status da tarefa entre concluída (`[X]`) e pendente (`[ ]`).

- **`3 - Remover tarefa`:** Exclui a tarefa selecionada e devolve automaticamente o custo dela ao orçamento disponível.

- **`0 - Voltar`:** Retorna ao menu principal.

### 6. Sugestões para o evento

Ao selecionar um evento, o sistema analisa o **tipo** (`aniversario`, `casamento` ou `reuniao`) e o **porte** com base na quantidade de convidados:

- **Pequeno:** até 20 convidados;

- **Médio:** de 21 a 100 convidados;

- **Grande:** acima de 100 convidados.

A partir disso, exibe uma recomendação de fornecedores adequada ao porte e sorteia sugestões de **decoração**, **cardápio** e **atividade**. Abrir a opção novamente gera novas combinações.

### 7. Resumo do evento

Apresenta um relatório consolidado do evento escolhido contendo:

- Quantidade de tarefas concluídas e barra visual de progresso (ex.: `[######----] 60%`);

- Percentual do orçamento utilizado e diagnóstico da situação financeira (`sob controle` até 80%, `quase no fim` acima de 80% e `ESTOURADO!` acima de 100%);

- Resumo de confirmações de convidados em relação à lista cadastrada e à capacidade prevista;

- **Custo previsto por convidado** (gasto total dividido pelos convidados previstos);

- **Custo real por confirmado** (gasto total dividido pelos convidados com status `confirmado`).

### 8. Lista de convidados (RSVP)

Após selecionar o evento, abre o gerenciamento da lista de convidados exibindo os nomes, etiquetas de status (`[Pendente]`, `[Confirmado]`, `[Recusado]`), contadores por status e a capacidade prevista:

- **`1 - Adicionar convidado`:** Cadastra um novo convidado com status inicial `pendente`. Caso a lista já tenha atingido o limite previsto do evento, exibe um alerta e solicita confirmação (`s/n`).

- **`2 - Alterar confirmação (RSVP)`:** Permite selecionar um convidado e atualizar seu status para `1 - pendente`, `2 - confirmado` ou `3 - recusado`.

- **`3 - Remover convidado`:** Exclui o convidado da lista do evento.

- **`0 - Voltar`:** Retorna ao menu principal.

### 0. Sair

Encerra a aplicação com segurança. Como todas as operações salvam imediatamente nos arquivos `.csv`, nenhum dado é perdido ao sair.

## Restrições Gerais da Aplicação

Para garantir a integridade dos dados e o funcionamento correto do sistema, observe as seguintes restrições:

1. **Caractere proibido (`;`):** Não é permitido utilizar ponto e vírgula (`;`) em nomes de eventos, locais, descrições de tarefas ou nomes de convidados, pois esse caractere é utilizado como separador de colunas nos arquivos `.csv`.

2. **Campos obrigatórios:** Nenhum campo de texto pode ficar vazio ou conter apenas espaços.

3. **Formato de data:** As datas devem seguir rigorosamente o padrão `DD/MM/AAAA` e corresponder a uma data real do calendário (por exemplo, `31/02/2026` é rejeitada).

4. **Valores numéricos:** Orçamentos, custos e quantidades de convidados não podem ser negativos. Valores monetários aceitam tanto ponto (`.`) quanto vírgula (`,`) como separador decimal.

5. **Tipos e status fixos:** Os tipos de evento são restritos a `aniversario`, `casamento` e `reuniao`, e os status de RSVP são restritos a `pendente`, `confirmado` e `recusado`.

6. **Exclusão irreversível:** Não há lixeira ou opção de desfazer; excluir um evento apaga permanentemente o evento, suas tarefas e seus convidados.

7. **Armazenamento local:** Os dados são armazenados localmente na pasta `data/` (relativa ao diretório de execução). Recomenda-se executar o comando `python main.py` sempre de dentro da pasta `organiza_festa/` para manter os arquivos no local esperado.

8. **Edição manual dos CSVs:** Alterar manualmente os arquivos dentro de `data/` fora do padrão de colunas pode causar avisos de leitura no sistema.

9. **Ambiente de uso:** A aplicação opera exclusivamente via terminal (linha de comando) e para uso local monousuário (sem acesso simultâneo em rede).

## Persistência de Dados (Formato dos Arquivos CSV)

Os arquivos são gerados automaticamente em `data/` com codificação UTF-8 e separador `;`:

| Arquivo          | Estrutura das Colunas                          | Exemplo                                                             |
| ---------------- | ---------------------------------------------- | ------------------------------------------------------------------- |
| `eventos.csv`    | `id;nome;tipo;data;local;orcamento;convidados` | `1;Festa da Cláudia;aniversario;20/12/2026;Salão Central;3500.0;50` |
| `tarefas.csv`    | `id_evento;descricao;custo;feita`              | `1;Buffet completo;1800.0;sim`                                      |
| `convidados.csv` | `id_evento;nome;status`                        | `1;Maria Silva;confirmado`                                          |

## Equipe

| Integrante   | GitHub                                                         |
| ------------ | -------------------------------------------                    |
| Pedro Costa  | [@](https://github.com/OCostaPedro) OCostaPedro                |
| Pedro Otavio | [@](https://github.com/PedroOGMS) PedroOGMS                    |
| Diogo Araujo | [@](https://github.com/diogodeda1997-maker) diogodeda1997-maker|
