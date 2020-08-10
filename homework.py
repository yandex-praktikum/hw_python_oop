import datetime as dt


class Calculator:  # родительский класс

    def __init__(self, limit):  # конструктор свойств (атрибутов)
        self.limit = limit
        self.records = []
        self.today = dt.datetime.today().date()

    def add_record(self, some_record):
        self.records.append(some_record)

    def get_today_stats(self):
        sum = 0
        for record in self.records:
            if record.date == self.today:
                sum = sum + record.amount
        return sum

    def get_week_stats(self):
        week_stats = 0
        for record in self.records:
            if self.today - dt.timedelta(days=6) <= record.date:
                if record.date <= self.today:
                    week_stats += record.amount
        return week_stats


class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.datetime.today().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class CashCalculator(Calculator):
    USD_RATE = 73.63
    EURO_RATE = 87.17

    def get_today_cash_remained(self, currency):
        currencys = {
            'rub': 'руб',
            'usd': 'USD',
            'eur': 'Euro'
        }
        answer_currency = currencys[currency]
        if currency == 'eur':
            cash_remained = round((self.limit - self.get_today_stats()) / self.EURO_RATE, 2)
        elif currency == 'usd':
            cash_remained = round((self.limit - self.get_today_stats()) / self.USD_RATE, 2)
        else:
            cash_remained = self.limit - self.get_today_stats()
        if cash_remained > 0:
            return (f'На сегодня осталось {cash_remained} {answer_currency}')
        elif cash_remained == 0:
            return ('Денег нет, держись')
        else:
            cash_remained /= -1
            return (f'Денег нет, держись: твой долг - {abs(cash_remained)} {answer_currency}')


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        calories_remained = self.limit - self.get_today_stats()
        if calories_remained < 0:
            return 'Хватит есть!'
        else:
            return f'Сегодня можно съесть что-нибудь ещё,' \
                   f' но с общей калорийностью не более ' \
                   f'{round((calories_remained), 2)} кКал'
