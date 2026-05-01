import sqlite3
from openpyxl import Workbook
from datetime import datetime
import os


def export_tasks_to_excel(db_path="tasks.db", output_file=None):
    if output_file is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"tasks_export_{timestamp}.xlsx"

    if not os.path.exists(db_path):
        print(f"Ошибка: файл базы данных '{db_path}' не найден.")
        print("Сначала запустите todo_cli.py для создания базы данных.")
        return False

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("PRAGMA table_info(tasks)")
        columns_info = cursor.fetchall()

        if not columns_info:
            print("Ошибка: таблица 'tasks' не найдена в базе данных.")
            conn.close()
            return False

        headers = [col[1] for col in columns_info]

        cursor.execute("SELECT * FROM tasks")
        data = cursor.fetchall()

        wb = Workbook()
        ws = wb.active
        ws.title = "Задачи"

        ws.append(headers)

        for row in data:
            ws.append(row)

        wb.save(output_file)
        conn.close()

        print(f"Успешно экспортировано {len(data)} задач в файл: {output_file}")
        return True

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        return False
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return False


if __name__ == "__main__":
    print("=== Экспорт задач из SQLite в Excel ===")
    print()

    custom_name = input("Введите имя выходного файла (или нажмите Enter для автоматического): ").strip()

    if custom_name:
        if not custom_name.endswith(".xlsx"):
            custom_name += ".xlsx"
        export_tasks_to_excel(output_file=custom_name)
    else:
        export_tasks_to_excel()

    input("Нажмите Enter для выхода...")