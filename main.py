def main():
    tasks = [
        "Изучить Git",
        "Выполнить лабораторную работу",
        "Отправить проект на GitHub",
    ]

    print("Учебный трекер")
    print("Задачи на сегодня:")

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


if __name__ == "__main__":
    main()