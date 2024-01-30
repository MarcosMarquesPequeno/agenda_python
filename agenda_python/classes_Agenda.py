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
            for indice, contato in enumerate(self.contatos, start=1):
                status = "✔" if contato.favorito else " "
                print(
                    f"{indice}.{status} Nome: {contato.nome}" +
                    f" Fone: {contato.telefone} E-mail: {contato.email}")

    def editar_contato(self, indice, nome, telefone, email):
        if 1 <= indice <= len(self.contatos):
            contato = self.contatos[indice - 1]
            contato.nome = nome
            contato.telefone = telefone
            contato.email = email
            print("Contato editado com sucesso!")

    def marcar_favorito(self, indice):
        if 1 <= indice <= len(self.contatos):
            contato = self.contatos[indice - 1]
            contato.favorito = not contato.favorito
            print(
                f"Contato {contato.nome} {'marcado' if contato.favorito else 'desmarcado'} como favorito.")
        else:
            print("Índice de contato inválido.")

    def listar_favoritos(self):
        favoritos = [Contato for contato in self.contatos if contato.favorito]
        if not favoritos:
            print("Nenhum contato favorito.")
        else:
            print("-- Contatos Favoritos -- ")
            for i, contato in enumerate(favoritos):
                print(f"{i+1}. Nome: {contato.nome}" +
                      f" Fone: {contato.telefone} E-mail: {contato.email}")

    def apagar_contato(self, indice):
        if 1 <= indice <= len(self.contatos):
            del self.contatos[indice - 1]
            print("Contato apagado com sucesso!")
        else:
            print("Indice de contato invalido.")
