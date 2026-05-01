from openpyxl import Workbook
import os
from datetime import datetime
def folder_report(files_dir, output_file = "files_description.xlsx"):
    wb = Workbook()
    ws = wb.active
    array = [["Путь","Имя","Расширение","Размер[кБ]","Дата изменения","Дата создания"]]
    for item in os.listdir(files_dir):  
        full_path = os.path.join(files_dir, item)
        stat_info = os.stat(full_path)
        size_kb = stat_info.st_size / 1024
        time_change = stat_info.st_mtime
        time_birth = stat_info.st_ctime
        creation_date = datetime.fromtimestamp(time_birth).strftime("%Y-%m-%d %H:%M:%S")
        change_date = datetime.fromtimestamp(time_change).strftime("%Y-%m-%d %H:%M:%S")  
        rash = os.path.splitext(item)[1].lower()
        cd = os.path.abspath(full_path)
        file_name = os.path.basename(item)
        file_name_without_ext = os.path.splitext(file_name)[0]
        array.append([cd,file_name_without_ext,rash,size_kb,change_date,creation_date])
    for i in array:
        ws.append(i)
    wb.save(output_file)
folder = input("Введите путь к  папке: ")
folder_report(folder)
