import datetime as dt

today = dt.date.today()

class Calculator:
    def __init__(self, limit):
        self.limit = int(limit)
        self.records = []
        
    def add_record(self, record):
        self.records.append(record)
        
    def get_today_stats(self):
        today_stats = 0
        today_stats = sum([record.amount for record in self.records if record.date == today])
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        week_start_day = today - dt.timedelta(7)
        week_stats = sum([record.amount for record in self.records if week_start_day <= record.date <= today])
        return week_stats


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = today


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        self.calories_remain = self.limit - self.get_today_stats()

        if self.limit > self.get_today_stats():
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.calories_remain} кКал"
        return f"Хватит есть!"


class CashCalculator(Calculator):
    USD_RATE = 78.87
    EURO_RATE = 82.62

    def get_today_cash_remained(self, currency):
        self.currency = currency
        self.currency_values = {
            "rub": (1, "руб"),
            "usd": (self.USD_RATE, "USD"),
            "eur": (self.EURO_RATE, "Euro")
        }
        self.currency_rate, self.currency_abbr = self.currency_values[self.currency]
        self.today_cash_remain = self.limit - self.get_today_stats()

        if self.currency == "rub":
            self.balance = self.today_cash_remain
        else:
            self.balance = round(self.today_cash_remain / self.currency_rate, 2)

        if self.today_cash_remain > 0:
            return f"На сегодня осталось {self.balance} {self.currency_abbr}"
        elif self.today_cash_remain < 0:
            return f"Денег нет, держись: твой долг - {abs(self.balance)} {self.currency_abbr}"
        return f"Денег нет, держись"