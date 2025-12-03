Sistemas Distribuídos - Trabalho Prático (AP2)

Este repositório contém os artefatos desenvolvidos para a Avaliação Prática 2 (AP2) da disciplina de Sistemas Distribuídos. O trabalho aborda conceitos fundamentais de sincronização lógica e consistência em sistemas distribuídos.

📋 Conteúdo

O projeto está dividido em duas partes principais:

Simulação de Relógios de Lamport: Implementação em Python do algoritmo de sincronização lógica para ordenação de eventos.

Estudo de Caso (Google Docs): Análise teórica sobre controle de concorrência otimista e tolerância a falhas em editores de texto colaborativos.

🚀 Tecnologias Utilizadas

Linguagem: Python 3.x

Conceitos: Relógios Lógicos, Exclusão Mútua, Algoritmos de Eleição, Consenso.

⚙️ Como Executar a Simulação

Certifique-se de ter o Python instalado em sua máquina.

Clone este repositório:

git clone https://github.com/FelipeFreires-Costa/Sistemas-Distribu-dos---Trabalho-Pr-tico-AP2-.git


Navegue até a pasta do projeto:

cd sistemas-distribuidos-lamport


Execute o script da simulação:

python simulacao_lamport.py


📊 Exemplo de Saída (Logs)

A execução do algoritmo gera os seguintes logs, demonstrando a correção dos timestamps lógicos conforme as regras de Lamport (Incremento prévio e Max(local, recebido) + 1):

=== Início da Simulação dos Relógios de Lamport ===

[P1] Evento Interno -> Relógio: 1
--------------------
[P2] Enviando msg para P3 -> Relógio (envio): 1
[P3] Recebeu de P2 (Ts: 1) | Ajuste: max(0, 1) + 1 -> Relógio: 2
--------------------
[P1] Enviando msg para P2 -> Relógio (envio): 2
[P3] Evento Interno -> Relógio: 3
--------------------
[P2] Recebeu de P1 (Ts: 2) | Ajuste: max(1, 2) + 1 -> Relógio: 3
--------------------
[P2] Enviando msg para P1 -> Relógio (envio): 4
[P1] Recebeu de P2 (Ts: 4) | Ajuste: max(2, 4) + 1 -> Relógio: 5

=== Estado Final dos Relógios ===
P1: 5
P2: 4
P3: 3


📄 Relatório Completo

O relatório detalhado contendo as respostas teóricas, a explicação da implementação e o estudo de caso completo pode ser encontrado no arquivo PDF anexado à entrega oficial na plataforma de ensino.

Autor: Felipe Freires Da Costa
