from classes_Agenda import Agenda


def main():
    agenda = Agenda()
    while True:
        print("\n Agenda telefonica\n")
        print("1. Adicionar contato")
        print("2. Visualizar lista de contato")
        print("3. Editar contato")
        print("4. Marcar/Desmarcar como favorito")
        print("5. Ver lista de contatos favoritos")
        print("6. Apagar contato")
        print("7. Sair da agenda \n")
        opcao = input("Escolha a opcao:")

        if opcao == "1":
            nome = input("Nome do contato:")
            telefone = input("Telefone do contato:")
            email = input("E-mail do contato:")
            agenda.adicionar_contato(nome, telefone, email)
        elif opcao == "2":
            agenda.listar_contatos()

        elif opcao == "3":
            agenda.listar_contatos()
            indice = int(
                input(" Digite o indice do contato que deseja editar:"))
            nome = input("Novo nome:")
            telefone = input("Novo telefone:")
            email = input("Novo e-mail:")
            agenda.editar_contato(indice, nome, telefone, email)

        elif opcao == "4":
            agenda.listar_contatos()
            indice = int(
                input("Digite o indice do contato que deseja marcar/desmarcar como favorito:"))
            agenda.marcar_favorito(indice)

        elif opcao == "5":
            agenda.listar_favoritos()

        elif opcao == "6":
            indice = int(
                input(" Digite o indice do contato que deseja apagar:"))
            agenda.apagar_contato(indice)

        elif opcao == "7":
            print("Saindo...")
            break


if __name__ == "__main__":
    main()
