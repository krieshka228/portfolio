import random
from openpyxl import Workbook
import os

def generate_price_list(input_file, output_file="prices_new.xlsx"):
        wb = Workbook()
        ws = wb.active
        if not os.path.exists(input_file):
            print(f"❌ Ошибка: файл {input_file} не найден!")
            return

        with open(input_file,"r") as file:
            content = file.read().split()
            array_exel = [ ["Товар", "Цена старая", "Цена новая"]]
            for word in content:
                old_price = random.randint(100, 5000)
                if(old_price > 1000):
                    new_price = round(old_price * 0.9)
                else:
                    new_price = random.randint(50,1000)
                array_exel.append([word,old_price,new_price])
            for i in array_exel:
                ws.append(i)
            wb.save(output_file)
file_name = input("Введите название файла или путь к нему: ")
exel_name = input("Введите название таблицы: ")
generate_price_list(file_name,exel_name)
