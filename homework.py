import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
            self.records.append(record)

    def get_today_stats(self):
        sum = 0
        for record in self.records:
            if record.date == self.currentDate.date(): #тесты запускались но писали ошибки, честно говоря не очень понятно что надо написать 
                sum += record.amount
        return sum

    def get_week_stats(self):
        sum = 0
        delta = dt.timedelta(7)
        week = self.currentDate.date() - delta
        for record in self.records:
            if (record.date > week and record.date <= self.currentDate.date()):
                sum += record.amount
        return sum

class Record:
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.date = dt.datetime.strptime(date, date_format).date() #полагал что этого будет достаточно, быстро как испровить пока не знаю ушел гуглить
        self.comment = comment


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if (self.limit > self.get_today_stats()):
            balance = self.limit - self.get_today_stats()
            return(f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {balance} кКал')
        else:
            return('Хватит есть!')

class CashCalculator(Calculator):
    USD_RATE = 62.07
    EURO_RATE = 69.40

    def get_today_cash_remained(self, currency):
        limit_today = self.limit
        balance_today = self.get_today_stats()
        balance = limit_today - balance_today
        balance_usd = round(balance / self.USD_RATE, 2)
        balance_euro = round(balance / self.EURO_RATE, 2)
        balance_all_currency = {
            "rub": (balance, "руб"),
            "usd": (balance_usd, "USD"),
            "eur": (balance_euro, "Euro")
        }
        balance_in_currency, value_currency = balance_all_currency[currency]
        if balance_today == limit_today:
            return "Денег нет, держись"
        if balance_today < limit_today:
            return f"На сегодня осталось {balance_in_currency} {value_currency}"
        return f"Денег нет, держись: твой долг - {-balance_in_currency} {value_currency}"

