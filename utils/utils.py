import requests


def open_last_five_operation(path=""):
    """
    Формирует список из 5 последних выполненных операций - last_five_operation
    """
    # Получает данные о переводах
    list_operations = requests.request("GET", path, verify=False).json()

    # Создаем необходимые пустые списки
    executed_operations = []
    last_five_operation = []

    # Формирует список выполненных переводов - executed_operations
    for index in range(len(list_operations)):
        if 'state' not in list_operations[index]:
            continue
        if list_operations[index]['state'] == 'EXECUTED':
            executed_operations.append(list_operations[index])

    # Сортирует список по дате начиная с самой ближней к настоящему времени - executed_operations_sorted
    executed_operations_sorted = sorted(executed_operations, key=lambda x: x.get('date'), reverse=True)

    # Формируем список последних 5 выполненных операций
    for index in range(5):
        last_five_operation.append(executed_operations_sorted[index])

    return last_five_operation
