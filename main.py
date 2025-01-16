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

DISTANCE = steps * STEP_M / TRANS_KOEF  # Напишите формулу расчёта
mean_speed = DISTANCE / hours
MINUTES = hours * 60
spent_calories = (0.035 * WEIGHT + (mean_speed ** 2 / HEIGHT) * 0.029 * WEIGHT) * MINUTES
congratulations = ''





if DISTANCE >= 6.5:
    congratulations = 'Отличный результат! Цель достигнута.'
elif DISTANCE >= 3.9 and DISTANCE < 6.5:
    congratulations = 'Неплохо! День был продуктивным.'
elif DISTANCE >= 2 and DISTANCE < 3.9:
    congratulations = 'Маловато, но завтра наверстаем!'
else:
    congratulations = 'Лежать тоже полезно! Главное участие, а не победа!'

output = f'''
Сегодня вы прошли {steps} шагов.
Пройденная дистанция {DISTANCE:.2f} км.
Вы сожгли {spent_calories:.2f} ккал.
{congratulations}'''

print(output)
