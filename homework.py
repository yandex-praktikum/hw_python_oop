import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.currentDate = dt.datetime.now()

    def add_record(self, record):
            self.records.append(record)

    def get_today_stats(self):
        sum = 0
        for record in self.records:
            if (record.date == self.currentDate.date()):
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
    def __init__(self, amount, comment, date=dt.date.today().strftime('%d.%m.%Y')):
        self.amount = amount
        self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.comment = comment

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if (self.limit > self.get_today_stats()):
            balance = self.limit - self.get_today_stats()
            return(f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {balance} кКал')
        else:
            return('Хватит есть!')

class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)
        self.USD_RATE = 62.07
        self.EURO_RATE = 69.40

    def get_today_cash_remained(self, value):
        balance = self.limit - self.get_today_stats()
        if (self.limit > self.get_today_stats()):
            if (value == "rub"):
                return (f'На сегодня осталось {balance} руб')
            elif (value == "usd"):
                return (f'На сегодня осталось {round(balance / self.USD_RATE, 2)} USD')
            elif (value == "eur"):
                return (f'На сегодня осталось {round(balance / self.EURO_RATE, 2)} Euro')
            else:
                return("Ivalid value")

        elif (self.limit == self.get_today_stats()):
            return ("Денег нет, держись")

        else:
            if (value == "rub"):
                return (f'Денег нет, держись: твой долг - {abs(balance)} руб')
            elif (value == "usd"):
                return (f'Денег нет, держись: твой долг - {round(abs(balance / self.USD_RATE), 2)} USD')
            elif (value == "eur"):
                return (f'Денег нет, держись: твой долг - {round(abs(balance / self.EURO_RATE), 2)} Euro')
            else:
                return ("Ivalid value")
