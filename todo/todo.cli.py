import sqlite3

con = sqlite3.connect('tasks.db')
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)""")

choice = True
while choice:
    x = input(
        "=== Меню ===\n1. Добавить задачу\n2. Показать невыполненные\n3. Выполнить задачу\n4. Выйти\nВыберите действие: ")

    if x == "1":
        task = input("Введите задачу: ")
        cur.execute("INSERT INTO tasks (title) VALUES (?)", (task,))
        con.commit()
        print("Задача успешно добавлена.")

    elif x == "2":
        cur.execute("SELECT * FROM tasks WHERE status = 0")
        task = cur.fetchall()
        if task:
            for item in task:
                print(f"{item[0]}. {item[1]} Создана: {item[3]}")
        else:
            print("Невыполненных задач нет.")

    elif x == "3":
        task_id = input("Введите id выполненной задачи: ")
        cur.execute("UPDATE tasks SET status = 1 WHERE id = ?", (task_id,))
        con.commit()
        print("Задача отмечена как выполнена!!!")

    elif x == "4":
        choice = False

con.close()
