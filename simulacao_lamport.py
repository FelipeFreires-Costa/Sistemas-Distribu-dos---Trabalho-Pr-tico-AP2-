import time

class Processo:
    def __init__(self, pid, nome):
        self.pid = pid
        self.nome = nome
        self.relogio = 0  # Inicializa o relógio lógico com 0

    def evento_interno(self):
        """Regra 1: Incrementa o relógio antes de um evento interno."""
        self.relogio += 1
        print(f"[{self.nome}] Evento Interno -> Relógio: {self.relogio}")

    def enviar_mensagem(self, destino):
        """
        Regra 1: Incrementa o relógio antes de enviar.
        Regra 2 (envio): Envia o timestamp junto com a mensagem.
        """
        self.relogio += 1
        print(f"[{self.nome}] Enviando msg para {destino.nome} -> Relógio (envio): {self.relogio}")
        return self.relogio

    def receber_mensagem(self, remetente, timestamp_recebido):
        """
        Regra 2 (recebimento): Ajusta o relógio local com max(local, recebido) + 1.
        """
        antigo = self.relogio
        self.relogio = max(self.relogio, timestamp_recebido) + 1
        print(f"[{self.nome}] Recebeu de {remetente.nome} (Ts: {timestamp_recebido}) | Ajuste: max({antigo}, {timestamp_recebido}) + 1 -> Relógio: {self.relogio}")

def main():
    print("=== Início da Simulação dos Relógios de Lamport ===\n")

    # Inicialização dos processos
    p1 = Processo(1, "P1")
    p2 = Processo(2, "P2")
    p3 = Processo(3, "P3")

    # Sequência solicitada no enunciado:
    
    # 1. P1: evento interno
    p1.evento_interno()
    
    print("-" * 20)

    # 2. P2: envia msg p/ P3
    # 3. P3: recebe msg de P2
    ts_msg_p2_p3 = p2.enviar_mensagem(p3)
    p3.receber_mensagem(p2, ts_msg_p2_p3)

    print("-" * 20)

    # 4. P1: envia msg p/ P2
    ts_msg_p1_p2 = p1.enviar_mensagem(p2)
    
    # O enunciado diz "P3: evento interno" antes de P2 receber a mensagem de P1?
    # Vamos seguir a ordem da lista do enunciado estritamente.
    
    # 5. P3: evento interno
    p3.evento_interno()

    print("-" * 20)

    # 6. P2: recebe msg de P1 (aquela enviada no passo 4)
    p2.receber_mensagem(p1, ts_msg_p1_p2)

    print("-" * 20)

    # 7. P2: envia msg p/ P1
    # 8. P1: recebe msg de P2
    ts_msg_p2_p1 = p2.enviar_mensagem(p1)
    p1.receber_mensagem(p2, ts_msg_p2_p1)

    print("\n=== Estado Final dos Relógios ===")
    print(f"{p1.nome}: {p1.relogio}")
    print(f"{p2.nome}: {p2.relogio}")
    print(f"{p3.nome}: {p3.relogio}")

if __name__ == "__main__":
    main()