from config import OPERATIONS_PATH
from src.functions import load_operations, get_examples, get_executed, operations_by_date


def main():
    """
    Функция вывода информации о пяти последних выполненных операций
    """
    # получаение списка из файла по указанному пути
    operations = load_operations(OPERATIONS_PATH)

    # преобразование списка с операциями
    example = get_examples(operations)

    # фильтрация списка операциями
    executed_operations = get_executed(example)

    # сортировка списка с операциями по дате
    sorted_operations = operations_by_date(executed_operations)
    count = 0
    # вывод пяти последних выполненных операций на экран
    for operation in sorted_operations:
        if count < 5:
            count += 1
            print(operation)
            print()


if __name__ == '__main__':
    main()
