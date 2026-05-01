import json
from datetime import datetime, timedelta
import os

if os.path.isfile('weather_log.json'):
    with open("weather_log.json", "r", encoding='utf-8') as json_file:
        data = json.load(json_file)
        now = datetime.now()
        temperature = []
        week_ago = now - timedelta(days=7)

        for record in data:
            date = datetime.strptime(record["timestamp"], '%d/%m/%Y %H:%M:%S')
            if date >= week_ago:
                temperature.append(record['data']['main']['feels_like'])

        if temperature:
            average = sum(temperature) / len(temperature)
            print(f"Средняя температура за семь дней: {average:.1f}°C")
        else:
            print("Нет данных за последние 7 дней")
else:
    print("Файл weather_log.json не найден. Сначала запустите weather_api.py")