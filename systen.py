is_running = True
collection = []
print("1 посмотреть задачу. \n2 добавить задачу \n3 -редактировать задачу \n удалить \n выход")
def show_collection(collection):
    print('='* 30)
    for i, j in enumerate(collection):
        print(f"{i + 1}. {j}")
    print("=" * 30)
while is_running:
    print("1 посмотреть задачу. \n2 добавить задачу \n3 -редактировать задачу \n удалить \n выход")
    clause_user = input("введите свой выбор")
    match str(clause_user):
        case '1':
            show_collection(collection)
        case '2':

            collection.append(input("Введите задачу"))
        case '3':
            show_collection(collection)
            select_task = int(input("введите номер задачи"))
            edit_task = input("Введите новый текст задачи задачи")

            collection[select_task - 1] = edit_task
        case '4':
            show_collection(collection)
            delete_task = int(input("Введите новый задачи для удаления"))
            collection.pop(delete_task - 1)
        case '5':
            is_running = False
            print('Адьес амиго')
        case _:
            print('НЕМА')

