import requests
def open_list_operations():
    """
    Получает данные о переводах.
    Формирует список выполненных переводов
    """
    executed_operations = []

    list_operations = requests.request("GET", "https://jsonkeeper.com/b/0MZI", verify=False).json()

    for i in range(len(list_operations)):
        if 'state' not in list_operations[i]:
            continue
        if list_operations[i]['state'] == 'EXECUTED':
            executed_operations.append(list_operations[i])

    return executed_operations

