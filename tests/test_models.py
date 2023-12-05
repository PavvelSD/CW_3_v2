from src.models import Operation

def test_convert_payment_info():
    operation = Operation(
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
        description="Открытие вклада",
        from_where="Maestro 1596837868705199",
        to="Счет 64686473678894779589"
    )
    assert operation.convert_payment_info(operation.to) == "Счет **9589"
