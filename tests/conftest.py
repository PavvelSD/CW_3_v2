import pytest

from src.models import Operation


@pytest.fixture
def operation_fixture_from_json():
    test_operation = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
        ,
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "CANCELED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
]
    return test_operation


@pytest.fixture
def operation_fixture_from_examples():
    operation_1 = Operation(
                pk=441945886,
                state="EXECUTED",
                date="2019-08-26T10:50:58.294041",
                operation_amount={
                    "amount": "31957.58",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                description="Перевод организации",
                from_where="Maestro 1596837868705199",
                to="Счет 64686473678894779589"
            )
    operation_2 = Operation(
                pk=41428829,
                state="EXECUTED",
                date="2019-07-03T18:35:29.512364",
                operation_amount={
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                description="Перевод организации",
                from_where="MasterCard 7158300734726758",
                to="Счет 35383033474447895560"
            )
    operation_3 = Operation(
                pk=41428829,
                state="CANCELED",
                date="2019-07-03T18:35:29.512364",
                operation_amount={
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                description="Перевод организации",
                from_where="MasterCard 7158300734726758",
                to="Счет 35383033474447895560"
            )
    return [operation_1, operation_2, operation_3]
