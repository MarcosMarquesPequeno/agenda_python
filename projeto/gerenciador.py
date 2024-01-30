def add_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return

def ver_tarefa(tarefas):
    print("\n Lista de tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✔" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")

    return

def upload_nome_tarefas(tarefas, indice_tarefa, new_name):
    ajuste_indice = int(indice_tarefa) - 1
    if ajuste_indice >= 0 and ajuste_indice < len(tarefas):
        tarefas[ajuste_indice]["tarefa"] = new_name
        print(f"\nTarefa {indice_tarefa} atualizada para {new_name}")
    else:
        print("Indice de tarefa invalido.")
    return


def completar_tarefa(tarefas, indice_tarefa):
    ajuste_indice = int(indice_tarefa) - 1
    tarefas[ajuste_indice]["completada"] = True
    print(f"\nTarefa {indice_tarefa} marcada como completada")
    return


def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print("\nTarefas completadas deletadas!")
    return


tarefas = []
while True:
    print("\n Menu do Gerenciador de Lista de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Ver tarefa")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefa completadas")
    print("5. Deletar tarefa")
    print("6. Sair")

    escolha = input("Digite a sua escolha:")

    if escolha == "1":
        nova_tarefa = input("Digite o nome da nova tarefa: ")
        add_tarefa(tarefas, nova_tarefa)

    elif escolha == "2":
        ver_tarefa(tarefas)

    elif escolha == "3":
        ver_tarefa(tarefas)
        indice_tarefa = input("Digite numero da tarefa que deseja atualizar:")
        new_name = input("Digite o novo nome da tarefa:")
        upload_nome_tarefas(tarefas, indice_tarefa, new_name)

    if escolha == "4":
        ver_tarefa(tarefas)
        indice_tarefa = input("Digite numero da tarefa que deseja completar:")
        completar_tarefa(tarefas, indice_tarefa)

    if escolha == "5":
        deletar_tarefas_completadas(tarefas)
        ver_tarefa(tarefas)
        indice_tarefa = input("Digite numero da tarefa que deseja excluir:")

    elif escolha == "6":
        print("Programa finalizado")
        break
