import datetime as dt

class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is not None:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = dt.date.today()

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def get_today_stats(self):
        today_am = 0
        today_date = dt.datetime.today().date()
        for record in self.records:
            if record.date == today_date:
                today_am += record.amount
        return today_am

    def get_week_stats(self):
        week_amount = 0
        today_date = dt.datetime.today().date()
        period = dt.timedelta(days=7)
        week_ago_date = today_date - period
        for record in self.records:
            if record.date > week_ago_date and record.date <= today_date:
                week_amount += record.amount
        return week_amount

    def add_record(self, new_record):
        self.records.append(new_record)
        
    def get_remained(self):
        return self.limit - self.get_today_stats()
        


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.get_remained() > 0:
            today = 'Сегодня можно съесть что-нибудь ещё,'
            return f'{today} но с общей калорийностью не более {self.get_remained()} кКал'
        return f'Хватит есть!'


class CashCalculator(Calculator):
    USD_RATE = 70.00
    EURO_RATE = 80.00
    RUB_RATE = 1

    currencies = {
        'rub': (RUB_RATE, 'руб'),
        'usd': (USD_RATE, 'USD'),
        'eur': (EURO_RATE, 'Euro')
    }
    
    def get_today_cash_remained(self, currency):

        cash_remained = self.limit - self.get_today_stats()

        if cash_remained == 0:
            return 'Денег нет, держись'
        
        money = {
            'rub': ('руб', 1),
            'usd': ('USD', self.USD_RATE),
            'eur': ('Euro', self.EURO_RATE)
        }

        currency, rate = money[currency]
        currency_cash = abs(round((cash_remained / rate), 2))

        if cash_remained > 0:   
            return f'На сегодня осталось {currency_cash} {currency}'
        else:
            return f'Денег нет, держись: твой долг - {currency_cash} {currency}' 
