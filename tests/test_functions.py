from datetime import datetime

from config import TEST_PATH
from src.functions import load_operations, get_examples, get_executed, operations_by_date
from src.models import Operation


def test_load_operations():
    assert load_operations(TEST_PATH) == "testing"


def test_get_examples(operation_fixture_from_json):
    operations = get_examples(operation_fixture_from_json)
    assert isinstance(operations, list)
    assert isinstance(operations[0], Operation)
    assert operations[0].pk == 441945886
    assert operations[1].to == "Счет **5560"
    assert operations[2].date == datetime.fromisoformat("2018-06-30T02:08:58.425572")


def test_get_executed_operations(operation_fixture_from_examples):
    operations = get_executed(operation_fixture_from_examples)
    assert len(operations) == 2
    assert operations[1].state == "EXECUTED"


def test_operations_by_date(operation_fixture_from_examples):
    operations = operations_by_date(operation_fixture_from_examples)
    assert len(operations) == 3
    assert operations[0].date > operations[1].date
