#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys

# Для своего варианта лабораторной работы 2.8 необходимо дополнительно реализовать
# сохранение и чтение данных из файла формата JSON. Необходимо также проследить за тем,
# чтобы файлы генерируемый этой программой не попадали в репозиторий лабораторнойработы.


def add(students):
    # Запросить данные о студенте
    name = input("Фамилия и инициалы? ")
    group = int(input("Номер группы? "))
    progress = [
        int(input("Оценка за 1 дисциплину - ")),
        int(input("Оценка за 2 дисциплину - ")),
        int(input("Оценка за 3 дисциплину - ")),
        int(input("Оценка за 4 дисциплину - ")),
        int(input("Оценка за 5 дисциплину - "))
    ]

    student = {
        'name': name,
        'group': group,
        'mark': progress
    }

    students.append(student)
    if len(students) > 1:
        students.sort(key=lambda item: item.get('group')[::-1])
    return students


def list(students):
    if not students:
        print("Список студентов пуст.")
        return

    # Заголовок таблицы
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 15
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
            "№",
            "Ф.И.О.",
            "Группа",
            "Успеваемость"
        )
    )
    print(line)

    # Вывести данные о всех студентах
    for idx, student in enumerate(students, 1):
        ma = student.get('mark', '')
        print(
            '| {:^4} | {:<30} | {:<20} | {},{},{},{},{:<7} |'.format(
                idx,
                student.get('name', ''),
                student.get('group', ''),
                ma[0],
                ma[1],
                ma[2],
                ma[3],
                ma[4]
            )
        )
        print(line)


def select(students):
    # Инициализировать счетчик
    count = 0
    # Проверить сведения студентов из списка
    for student in students:
        mark = student.get('mark', '')
        if sum(mark) / max(len(mark), 1) >= 4.0:
            print(
                '{:>4} {}'.format('-', student.get('name', '')),
                '{:>1} №{}'.format('группа', student.get('group', ''))
            )
            count += 1
    if count == 0:
        print("Студенты с баллом 4.0 и выше не найдены.")


def help():
    print("Список команд:\n")
    print("add - добавить студента;")
    print("list - вывести список студентов;")
    print("select - запросить студентов с баллом выше 4.0;")
    print("save - сохранить список студентов;")
    print("load - загрузить список студентов;")
    print("exit - завершить работу с программой.")


def save_students(file_name, students):
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(students, fout, ensure_ascii=False, indent=4)


def load_students(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


def main():
    # Список студентов
    students = []

    while True:
        # Запросить команду из терминала
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой
        if command == 'exit':
            break
        elif command == 'add':
            students = add(students)
        elif command == 'list':
            list(students)
        elif command.startswith('select'):
            select(students)
        elif command.startswith("save "):
            parts = command.split(maxsplit=1)
            file_name = parts[1]
            save_students(file_name, students)
        elif command.startswith("load "):
            parts = command.split(maxsplit=1)
            file_name = parts[1]
            students = load_students(file_name)
        elif command == 'help':
            help()
        else:
            print("Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
