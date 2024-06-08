class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}
    
    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print(f"Contato {nome} já existe.")
        else:
            self.contatos[nome] = telefone
            print(f"Contato {nome} adicionado com sucesso.")
    
    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"Contato {nome} removido com sucesso.")
        else:
            print(f"Contato {nome} não encontrado.")
    
    def pesquisar_contato(self, nome):
        if nome in self.contatos:
            print(f"{nome}: {self.contatos[nome]}")
        else:
            print(f"Contato {nome} não encontrado.")
    
    def listar_contatos(self):
        if not self.contatos:
            print("Agenda vazia.")
        else:
            for nome, telefone in self.contatos.items():
                print(f"{nome}: {telefone}")

def menu():
    agenda = AgendaTelefonica()
    while True:
        print("\nMenu:")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Pesquisar Contato")
        print("4. Listar Contatos")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            agenda.adicionar_contato(nome, telefone)
        elif opcao == '2':
            nome = input("Nome: ")
            agenda.remover_contato(nome)
        elif opcao == '3':
            nome = input("Nome: ")
            agenda.pesquisar_contato(nome)
        elif opcao == '4':
            agenda.listar_contatos()
        elif opcao == '5':
            print("Saindo da agenda. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()
