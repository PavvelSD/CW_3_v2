from config import OPERATIONS_PATH
from src.functions import load_operations, get_examples, get_executed, operations_by_date


def main():
    operations = load_operations(OPERATIONS_PATH)
    example = get_examples(operations)
    executed_operations = get_executed(example)
    sorted_operations = operations_by_date(executed_operations)
    print(example[1].from_where)
    for operation in sorted_operations:
        print(operation)


if __name__ == '__main__':
    main()
