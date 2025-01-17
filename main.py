import datetime as dt

FORMAT = '%H:%M:%S'
WEIGHT = 75  # Вес
HEIGHT = 175  # Рост
K_1 = 0.035  # Коэфициент для подсчёта калорий
K_2 = 0.029  # Коэфициент для подсчёта калорий
STEP_M = 0.65  # Длина одного шага в метрах
TRANS_KOEF = 1000  # Коэффициент перевода  расстояния из метров в километры
storage_data = {}  # Словарь для хранения полученных данных.

# steps and time будут из входящих кортежей (<time>, <steps>)
time = None
hours = None
minutes = hours * 60
steps = None
distance = steps * STEP_M / TRANS_KOEF  # Напишите формулу расчёта
speed = distance / hours
spent_calories = (
    K_1 * WEIGHT + (speed ** 2 / HEIGHT) * K_2 * WEIGHT
    ) * minutes

# Выбор вида поздравления
congratulations = ''
if distance >= 6.5:
    congratulations = 'Отличный результат! Цель достигнута.'
elif distance >= 3.9 and distance < 6.5:
    congratulations = 'Неплохо! День был продуктивным.'
elif distance >= 2 and distance < 3.9:
    congratulations = 'Маловато, но завтра наверстаем!'
else:
    congratulations = 'Лежать тоже полезно! Главное участие, а не победа!'

output = f'''
Сегодня вы прошли {steps} шагов.
Пройденная дистанция {distance:.2f} км.
Вы сожгли {spent_calories:.2f} ккал.
{congratulations}'''


# Функции


def check_correct_data(data):
    if len(data) != 2:
        return False
    if (
        not data[0]
        or not data[1]
    ):
        return False
    else:
        return True

    """Проверка корректности полученного пакета."""
    # Если длина пакета отлична от 2
    # или один из элементов пакета имеет пустое значение -
    # функция вернет False, иначе - True.


def check_correct_time(time):
    time = dt.datetime.strptime(time, FORMAT)
    if len(storage_data) > 0:
        last_time = max(storage_data.keys())
        if time <= last_time:
            return False
    else:
        return True
        """Проверка корректности параметра времени."""
    # Если словарь для хранения не пустой
    # и значение времени, полученное в аргументе,
    # меньше или равно самому большому значению ключа в словаре,
    # функция вернет False.
    # Иначе - True


def get_step_day(steps):
    last_steps = sum(storage_data.values())
    total_steps = last_steps + steps
    return total_steps
    """Получить количество пройденных шагов за этот день."""
    # Посчитайте все шаги, записанные в словарь storage_data,
    # прибавьте к ним значение из последнего пакета
    # и верните  эту сумму.


def get_distance(steps):
    steps_in_km = steps * STEP_M / TRANS_KOEF
    return steps_in_km
    """Получить дистанцию пройденного пути в км."""
    # Посчитайте дистанцию в километрах,
    # исходя из количества шагов и длины шага.


def get_spent_calories(dist, current_time):
    spent_calories = (
        K_1 * WEIGHT()
    )
    """Получить значения потраченных калорий."""
    # В уроке «Последовательности» вы написали формулу расчета калорий.