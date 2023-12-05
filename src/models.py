from datetime import datetime


class Operation:
    def __init__(self, pk, state, date, operation_amount, description, from_where, to):
        self.pk = pk
        self.state = state
        self.date = self.convert_date(date)
        self.operation_amount = operation_amount
        self.description = description
        self.from_where = self.convert_payment_info(from_where)
        self.to = self.convert_payment_info(to)

    def convert_date(self, date):
        """
        Функция конвертации формата даты
        :param date: строка с датой
        :return: преобразованная дата в iso datetime
        """
        return datetime.fromisoformat(date)

    def convert_payment_info(self, payment_info: str):
        if payment_info:
            payment_info_list = payment_info.split()
            if payment_info.startswith("Счет"):
                num_payment = payment_info_list.pop()
                num_payment = f'**{num_payment[-4:]}'
                payment_info_list.append(num_payment)
            else:
                num_card = payment_info_list.pop()
                num_card = f'{num_card[0:4]} {num_card[4:6]}** **** {num_card[-4:]}'
                payment_info_list.append(num_card)
            return " ".join(payment_info_list)
        return f'Счет/Номер карты не указан'

    def __str__(self):
        return (f"{datetime.strftime(self.date, '%d.%m.%Y')} {self.description}\n"
                f"{self.from_where} -> {self.to}\n"
                f"{self.operation_amount['amount']} {self.operation_amount['currency']['name']}")