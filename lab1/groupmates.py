from collections.abc import Iterable, Iterator
from typing import TypedDict


class TStudent(TypedDict):
    name: str
    group: str
    age: int
    marks: list[int]


groupmates: list[TStudent] = [
    {"name": "Иванов Алексей", "group": "БСТ-2301", "age": 19, "marks": [5, 4, 5, 4, 5]},
    {"name": "Петрова Мария", "group": "БСТ-2301", "age": 18, "marks": [4, 5, 5, 5, 4]},
    {"name": "Сидоров Дмитрий", "group": "БСТ-2301", "age": 20, "marks": [3, 4, 3, 4, 3]},
    {"name": "Козлова Анна", "group": "БСТ-2301", "age": 19, "marks": [5, 5, 4, 5, 5]},
    {"name": "Морозов Кирилл", "group": "БСТ-2301", "age": 18, "marks": [4, 3, 4, 3, 4]},
    {"name": "Новикова Елена", "group": "БСТ-2301", "age": 19, "marks": [5, 4, 4, 5, 4]},
    {"name": "Волков Артём", "group": "БСТ-2301", "age": 20, "marks": [3, 3, 4, 3, 3]},
    {"name": "Соколова Дарья", "group": "БСТ-2301", "age": 18, "marks": [4, 5, 4, 4, 5]},
    {"name": "Лебедев Максим", "group": "БСТ-2301", "age": 19, "marks": [5, 5, 5, 4, 5]},
    {"name": "Кузнецова Ольга", "group": "БСТ-2301", "age": 20, "marks": [4, 4, 3, 4, 4]},
]


def print_students(students: Iterable[TStudent]) -> None:
    print("Имя студента".ljust(15), "Группа".ljust(8), "Возраст".ljust(8), "Оценки".ljust(20))
    for student in students:
        print(
            student["name"].ljust(15),
            student["group"].ljust(8),
            str(student["age"]).ljust(8),
            str(student["marks"]).ljust(20),
        )
    print("\n")


def print_students_unjustified(students: Iterable[TStudent]) -> None:
    print("Имя студента", "Группа", "Возраст", "Оценки")
    for student in students:
        print(student["name"], student["group"], str(student["age"]), str(student["marks"]))
    print("\n")


def filter_gt_avg_mark(students: Iterable[TStudent], avg_mark: int) -> Iterator[TStudent]:
    return (student for student in students if sum(student["marks"]) / len(student["marks"]) >= avg_mark)


if __name__ == "__main__":
    print_students(groupmates)
    print_students_unjustified(groupmates)

    avg_mark = int(input("Введите среднюю оценку: "))
    print_students(filter_gt_avg_mark(groupmates, avg_mark))
