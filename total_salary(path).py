def total_salary(path):
    try:
        with open(path, encoding='utf-8') as file:
            total_sum = 0
            num_developers = 0
            for line in file:
                name, salary = line.strip().split(",")
                total_sum += int(salary)
                num_developers += 1
            if num_developers == 0:
                return (0,0)
            average_salary = total_sum / num_developers
            average_salary_rounded = round(average_salary, 1)
            return  (total_sum, average_salary_rounded)
    except FileNotFoundError:
        print("Файл не знайдено. Будь ласка, перевірте шлях до файлу.")
        return (0, 0)

total, average = total_salary('salary_file.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
