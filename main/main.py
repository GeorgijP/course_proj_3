# Импорт нужных библиотек и функций
import datetime
from utils.utils import open_last_five_operation

# Создание функции с данными
operations = open_last_five_operation("https://jsonkeeper.com/b/0MZI")

# Цикл по преведению данных к корректному виду вывода
for i in range(5):

    # Преобразование даты в нужный формат
    date_time = datetime.datetime.fromisoformat(operations[i]['date'])
    date = datetime.datetime.strftime(date_time, '%d.%m.%Y')

    # Скрытие части номера получателя
    recipient_number = list(operations[i]['to'])
    recipient_number[0:-4] = "***"
    recipient_number = "".join(recipient_number)

    # Проверка наличия номера отправителя
    if 'from' not in operations[i]:
        # Вывод данных без номера отправителя
        print(f"{date} {operations[i]['description']}\nНомер счета отсутствует -> {recipient_number}\n{operations[i]['operationAmount']['amount']} {operations[0]['operationAmount']['currency']['name']}\n")
    else:
        number = list(operations[i]['from'])
        # Разделение номера отправителя на блоки "по 4"
        number.insert(-4, " "), number.insert(-9, " "), number.insert(-14, " ")
        # Скрытие части номера отправителя
        number[-9: -5] = "****"
        number[-12: -10] = "**"
        number = "".join(number)
        # Вывод данных с номером отправителя
        print(f"{date} {operations[i]['description']}\n{number} -> {recipient_number}\n{operations[i]['operationAmount']['amount']} {operations[0]['operationAmount']['currency']['name']}\n")
