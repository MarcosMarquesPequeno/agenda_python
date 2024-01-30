
class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = False


class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone, email):
        novo_contato = Contato(nome, telefone, email)
        self.contatos.append(novo_contato)
        print("Contato adicionado com sucesso!")

    def listar_contatos(self):
        if not self.contatos:
            print("Nenhum contato na agenda.")
        else:
            for i, contato in enumerate(self.contatos):
                print(
                    f"{i+1}. {contato.nome} - {contato.telefone} - {contato.email} {'(Favorito)' if contato.favorito else ''}")

    def editar_contato(self, indice, nome, telefone, email):
        if 1 <= indice <= len(self.contatos):
            contato = self.contatos[indice - 1]
            contato.nome = nome
            contato.telefone = telefone
            contato.email = email
            print("Contato editado com sucesso!")
        else:
            print("Índice de contato inválido.")

    def marcar_favorito(self, indice):
        if 1 <= indice <= len(self.contatos):
            contato = self.contatos[indice - 1]
            contato.favorito = not contato.favorito
            print(
                f"Contato {contato.nome} {'marcado' if contato.favorito else 'desmarcado'} como favorito.")
        else:
            print("Índice de contato inválido.")

    def listar_favoritos(self):
        favoritos = [contato for contato in self.contatos if contato.favorito]
        if not favoritos:
            print("Nenhum contato favorito.")
        else:
            print("--- Contatos Favoritos ---")
            for i, contato in enumerate(favoritos):
                print(
                    f"{i+1}. {contato.nome} - {contato.telefone} - {contato.email}")

    def apagar_contato(self, indice):
        if 1 <= indice <= len(self.contatos):
            del self.contatos[indice - 1]
            print("Contato apagado com sucesso!")
        else:
            print("Índice de contato inválido.")


def main():
    agenda = Agenda()
    while True:
        print("\n--- Agenda de Contatos ---")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Editar Contato")
        print("4. Marcar/Desmarcar como Favorito")
        print("5. Listar Contatos Favoritos")
        print("6. Apagar Contato")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do contato: ")
            telefone = input("Telefone do contato: ")
            email = input("E-mail do contato: ")
            agenda.adicionar_contato(nome, telefone, email)
            
        elif escolha == "2":
            agenda.listar_contatos()
        elif escolha == "3":
            indice = int(
                input("Digite o índice do contato que deseja editar: "))
            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")
            email = input("Novo e-mail: ")
            agenda.editar_contato(indice, nome, telefone, email)
        elif escolha == "4":
            indice = int(
                input("Digite o índice do contato que deseja marcar/desmarcar como favorito: "))
            agenda.marcar_favorito(indice)
        elif escolha == "5":
            agenda.listar_favoritos()
        elif escolha == "6":
            indice = int(
                input("Digite o índice do contato que deseja apagar: "))
            agenda.apagar_contato(indice)
        elif escolha == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
