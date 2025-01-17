import datetime as dt

FORMAT = '%H:%M:%S'
WEIGHT = 75  # Вес
HEIGHT = 175  # Рост
K_1 = 0.035  # Коэфициент для подсчёта калорий
K_2 = 0.029  # Коэфициент для подсчёта калорий
STEP_M = 0.65  # Длина одного шага в метрах
TRANS_KOEF = 1000  # Коэффициент перевода  расстояния из метров в километры
storage_data = {}  # Словарь для хранения полученных данных.

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
    if storage_data:
        last_time = max(storage_data.keys())
        last_time = dt.datetime.strptime(
            last_time, FORMAT
        )
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


def get_distance(steps):
    """
    Получить дистанцию пройденного пути в км,
    исходя из количества шагов и длины шага.
    """
    dist_in_km = steps * STEP_M / TRANS_KOEF
    return dist_in_km


def get_step_day(steps):
    """
    Получить количество пройденных шагов за этот день.
    Посчитайте все шаги, записанные в словарь storage_data,
    прибавьте к ним значение из последнего пакета
    и верните эту сумму.
    """
    last_steps = sum(storage_data.values())
    total_steps = last_steps + steps
    return total_steps


def get_spent_calories(dist, current_time):
    current_dt = dt.datetime.strptime(current_time, FORMAT)
    hour = current_dt.hour
    minute = current_dt.minute
    minutes = hour * 60 + minute

    if hour == 0:
        speed = 0
    else:
        speed = dist / hour

    spent_calories = (
        K_1 * WEIGHT +
        (speed**2 / HEIGHT) * K_2 * WEIGHT
    ) * minutes
    return spent_calories
    """Получить значения потраченных калорий."""
    # В уроке «Последовательности» вы написали формулу расчета калорий.


def show_message(current_time, step_day, dist, calories):
    # Определяем сообщение в зависимости от dist
    if dist >= 6.5:
        congrats = 'Отличный результат! Цель достигнута.'
    elif dist >= 3.9:
        congrats = 'Неплохо! День был продуктивным.'
    elif dist >= 2:
        congrats = 'Маловато, но завтра наверстаем!'
    else:
        congrats = 'Лежать тоже полезно! Главное участие, а не победа!'

    print(f'''
Время: {current_time}.
Количество шагов за сегодня: {step_day}.
Дистанция составила {dist:.2f} км.
Вы сожгли {calories:.2f} ккал.
{congrats}
''')


def accept_package(data):
    """Точка входа в программу.
    Принимает пакет данных (<time_str>, <steps>),
    проверяет корректность, записывает в словарь,
    считает статистику, выводит сообщение и возвращает storage_data."""
    # 1. Проверяем корректность пакета.
    if not check_correct_data(data):
        return storage_data

    # 2. Распаковываем кортеж: (time_str, steps).
    time_str, steps = data

    # 3. Проверяем корректность времени.
    if not check_correct_time(time_str):
        return storage_data

    # 4. Записываем данные в словарь.
    storage_data[time_str] = steps

    # 5. Суммируем шаги за день.
    step_day = get_step_day(steps)

    # 6. Получаем дистанцию.
    dist = get_distance(step_day)

    # 7. Считаем калории.
    calories = get_spent_calories(dist, time_str)

    # 8. Выводим сообщение.
    show_message(time_str, step_day, dist, calories)

    # 9. Возвращаем текущие данные.
    return storage_data


result = accept_package(('09:36:02', 5700))
print(result)
