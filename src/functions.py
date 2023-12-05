import json

from src.models import Operation


def load_operations(path):
    """
    Функция для чтения данных из файла
    :param path: путь к файлу
    :return: преобразованные данные
    """
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_examples(operations):
    """
    Функция формирования списка экземпляров класса Operation
    :param operations: список словарей
    :return: список экземпляров
    """
    operation_examples = []
    for operation in operations:
        if operation:
            operation_example = Operation(
                pk=operation["id"],
                state=operation["state"],
                date=operation["date"],
                operation_amount=operation["operationAmount"],
                description=operation["description"],
                from_where=operation.get("from", ""),
                to=operation["to"]
            )
            operation_examples.append(operation_example)
    return operation_examples


def get_executed(operations):
    """
    Функция формирования списка экземпляров (операций) со статусом "Исполнено"
    :param operations: список экземпляров
    :return: отфильтрованный список экземпляров
    """
    executed_operations = []
    for operation in operations:
        if operation.state == "EXECUTED":
            executed_operations.append(operation)
    return executed_operations


def operations_by_date(operations):
    """
    Функция сортировки экзмепляров по дате
    :param operations:список экземпляров
    :return: отсортированный список экземпляров по дате
    """
    return sorted(operations, key=lambda operation: operation.date, reverse=True)
