import os
import requests
import json
from datetime import datetime

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Moscow&appid=9aa97bd67726834abbf280f4f7a9074e&units=metric')

try:
    with open("weather_log.json", 'r', encoding='utf-8') as json_file:
        if os.path.getsize("weather_log.json") > 0:
            data = json.load(json_file)
            if isinstance(data, dict):
                data = [data]
        else:
            data = []
except (FileNotFoundError, json.JSONDecodeError):
    data = []

date_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
new_record = {"timestamp": date_time}
new_record["data"] = r.json()
data.append(new_record)

temp = new_record["data"]["main"]["feels_like"]
if temp < 0:
    print("Мороз!")

with open("weather_log.json", "w", encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print(f"Погода сохранена. Температура по ощущениям: {temp}°C")