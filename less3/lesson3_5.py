def add_students():
    name = input("Введите имя ")
    while True:
        try:
            grade = int(input("Введите оценку "))
            return name, grade
        except ValueError:
            print("Вы ввели не число")
            continue
        # else:
        #     return name, grade


def sort_students(students):
    good_grade = "Поступили:"
    bad_grade = "Не поступили:"
    for name, grade in students.items():
        if grade >= 4:
            good_grade += f"\n{name} - {grade}"
        elif grade <= 3:
            bad_grade += f"\n{name} - {grade}"
    print(good_grade)
    print(bad_grade)


def main():
    students = {}
    while True:
        command = input("1 - Добавте\n2 - Просмотреть\nВведит команду ")
        if command == "1":
            name, grade = add_students()
            students[name] = grade
        elif command == "2":
            sort_students(students)


if __name__ == "__main__":
    main()


"""
Поступили:
имя - оценка
...
Не постурили:
имя - оценка
...


['name - value', 'name - value']
"""
