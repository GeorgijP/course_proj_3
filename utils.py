import requests
def open_list_operations():
    """
    Получает данные о переводах
    """
    list_operations = requests.request("GET", "https://jsonkeeper.com/b/0MZI", verify=False)
    list_operations = list_operations.json()
    return list_operations
