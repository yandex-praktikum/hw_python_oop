import datetime as dt
from typing import Union, Optional
from math import fabs


class Record:
    def __init__(self, amount: float, comment: str, date: Optional[dt.datetime] = None):
        self.amount = amount
        self.date = (
            dt.datetime.strptime(date, "%d.%m.%Y").date()
            if date is not None
            else dt.date.today()
        )
        self.comment = comment


class Calculator:
    def __init__(self, limit: int):
        self.limit = limit
        self.records = []

    def add_record(self, record: Record) -> None:
        self.records.append(record)

    def get_today_stats(self) -> Union[float, int]:
        return sum([r.amount for r in self.records if r.date == dt.date.today()])

    def get_week_stats(self) -> Union[float, int]:
        return sum(
            [
                r.amount
                for r in self.records
                if dt.date.today() >= r.date >= dt.date.today() - dt.timedelta(days=7)
            ]
        )


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_remained = self.limit - self.get_today_stats()
        if calories_remained > 0:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories_remained} кКал"
        else:
            return "Хватит есть!"


class CashCalculator(Calculator):
    USD_RATE = 62.27
    EURO_RATE = 69.08

    def get_today_cash_remained(self, currency: str):
        cash_remained = self.limit - self.get_today_stats()
        if cash_remained == 0:
            return "Денег нет, держись"

        if currency == "eur":
            phrase = f"{round(fabs(cash_remained) / self.EURO_RATE, 2)} Euro"
        elif currency == "usd":
            phrase = f"{round(fabs(cash_remained) / self.USD_RATE, 2)} USD"
        elif currency == "rub":
            phrase = f"{int(fabs(cash_remained))} руб"
        else:
            return "Я не знаю такую валюту"

        if cash_remained > 0:
            return f"На сегодня осталось {phrase}"
        else:
            return f"Денег нет, держись: твой долг - {phrase}"
