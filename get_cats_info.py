def get_cats_info(path):
    cats_info = []
    try:
        with open(path, "r", encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                parts = line.split(',')
                if len(parts) != 3:
                    continue
                cat_dict = {
                    'id': parts[0],
                    'name': parts[1],
                    'age': parts[2],
                }
                cats_info.append(cat_dict)
    except FileNotFoundError:
        print("Файл не знайдено. Будь ласка, перевірте шлях до файлу.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
    return cats_info

cats_info = get_cats_info("cats_database.txt")
print(cats_info)