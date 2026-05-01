import os
from openpyxl import Workbook
def rename_files(files_path):
    for file in os.listdir(files_path):
        name, ext = os.path.splitext(file)
        name  = name.split("_")[0] + "_" + name.split("_")[1]
        new_file = name + ext
        os.rename(f"{files_path}/{file}", f"{files_path}/{new_file}")
    print(f"Файлы переименованы")
def create_xls_file(files_path):
    wb = Workbook()
    ws = wb.active
    stats = {}
    for file in os.listdir(files_path):
        full_path = os.path.join(files_path, file)
        if os.path.isfile(full_path):
            name, ext = os.path.splitext(file)
            year = name.split("-")[0]
            stat_info = os.stat(full_path)
            stat_size = stat_info.st_size / 1024
            if year not in stats:
                stats[year] = {"count" : 0, "size": 0}
            stats[year]["count"] += 1
            stats[year]["size"] += stat_size

    ws.append(["Год","Количество файлов","Общий размер (КБ)"])
    for year, data in sorted(stats.items()):
        ws.append([year,data["count"],data["size"]])
    output_path = os.path.join(files_path,"rename_report.xlsx")
    wb.save(output_path)
print("rename_report.xlsx создан")
name_path = input("Введите путь папки: ")
rename_files(name_path)
create_xls_file(name_path)