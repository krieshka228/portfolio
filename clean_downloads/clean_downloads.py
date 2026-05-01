import shutil
import os

def get_unique_path(dest):
    """Возвращает уникальное имя файла, если такой уже существует"""
    if not os.path.exists(dest):
        return dest
    name, ext = os.path.splitext(dest)
    counter = 1
    while os.path.exists(f"{name}_{counter}{ext}"):
        counter += 1
    return f"{name}_{counter}{ext}"

def clean_downloads(downloads_path):
    """Сортирует файлы в папке downloads по расширениям"""
    
    with open(os.path.join(downloads_path, "report.txt"), "w", encoding="utf-8") as log_file:
        # Расширения и папки
        extensions = {
            ".jpg": "image", ".jpeg": "image", ".png": "image", ".gif": "image",
            ".exe": "programs", ".msi": "programs",
            ".pdf": "docs", ".docx": "docs", ".doc": "docs", ".txt": "docs"
        }
        
        # Создаём папки
        for folder in set(extensions.values()):
            os.makedirs(os.path.join(downloads_path, folder), exist_ok=True)
        os.makedirs(os.path.join(downloads_path, "unknown"), exist_ok=True)
        
        # Обрабатываем файлы
        for item in os.listdir(downloads_path):
            source = os.path.join(downloads_path, item)
            
            # Пропускаем папки и сам отчёт
            if not os.path.isfile(source) or item == "report.txt":
                continue
            
            # Определяем расширение
            ext = os.path.splitext(item)[1].lower()
            target = extensions.get(ext, "unknown")
            
            # Перемещаем
            dest_dir = os.path.join(downloads_path, target)
            dest = os.path.join(dest_dir, item)
            dest = get_unique_path(dest)
            
            shutil.move(source, dest)
            log_file.write(f"Перемещён: {item} -> {target}\n")
            print(f"✓ {item} -> {target}")
    
    print(f"\n Готово! Отчёт: {downloads_path}/report.txt")

# Запуск
if __name__ == "__main__":
    HOME = "D:/!!!/Downloads"  # Смени на свой путь
    clean_downloads(HOME)
                    
            
            
    
    