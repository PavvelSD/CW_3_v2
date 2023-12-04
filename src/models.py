from datetime import datetime


class Operation:
    def __init__(self, pk, date, state, operation_amount, description, from_where, to):
        self.pk = pk
        self.date = self.convert_date(date)
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_where = self.convert_payment_info(from_where)
        self.to = self.convert_payment_info(to)

    def convert_date(self, date):
        """
        Функция конвертации формата даты
        :param date: строка с датой в формате iso
        :return: datetime в требуемом формате
        """
        iso_date = datetime.fromisoformat(date)
        str_date = datetime.strftime(iso_date, "%d.%m.%Y")
        return datetime.strptime(str_date, "%d.%m.%Y")

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
        return (f"{self.date} {self.description}\n"
                f"{self.from_where} -> {self.to}\n"
                f"{self.operation_amount['amount']} {self.operation_amount['currency']['name']}")