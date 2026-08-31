from dataclasses import dataclass, field

@dataclass
class SimuladorDesfazer:
    pilha_acoes: list = field(default_factory=list)

    def inserir_acao(self, tipo_acao, conteudo):
        acao = {"tipo": tipo_acao, "conteudo": conteudo}
        self.pilha_acoes.append(acao)
        print(f"Ação Registrada: [{tipo_acao.upper()}] '{conteudo}'")

    def desfazer(self):
        if not self.pilha_acoes:
            print("Nenhuma ação pra desfazer")
            return None
        
        ultima_acao = self.pilha_acoes.pop()
        print(f"\n[desfazendo] Revertendo o comando: {ultima_acao['tipo'].upper()}")

        if ultima_acao["tipo"] == "digitar":
            print(f"-> Removendo: '{ultima_acao['conteudo']}'")
        elif ultima_acao["tipo"] == "apagar":
            print(f"-> Restaurando: '{ultima_acao['conteudo']}'")

        return ultima_acao

if __name__ == "__main__":
    simulador = SimuladorDesfazer()

    print("--- SIMULADOR DE DESFAZER ATIVO ---")
    print("Comandos disponíveis: digitar, apagar, desfazer, sair")
    
    while True:
        print("\n" + "-"*30)
        comando = input("O que deseja fazer? ").strip().lower()

        if comando == "sair":
            print("Encerrando o simulador. Até logo!")
            break

        elif comando == "desfazer":
            simulador.desfazer()

        elif comando in ["digitar", "apagar"]:
            texto = input(f"Digite o texto que deseja {comando}: ")
            simulador.inserir_acao(comando, texto)

        else:
            print("Comando inválido! Escolha entre: digitar, apagar, desfazer ou sair.")