import datetime as dt

class Calculator:
    def __init__(self,limit):
        self.limit = limit
        self.records = []

    def add_record(self,record):
        self.records.append(record)
    
    def get_today_stats(self):
        res = 0
        for i in self.records:
            if (i.date == dt.datetime.now().date()):
                res += i.amount
        return(res)
    
    def get_week_stats(self):
        res = 0
        for i in self.records:
            if (i.date > dt.datetime.now().date() - dt.timedelta(days=7) 
            and i.date <= dt.datetime.now().date()):
                res += i.amount
        return(res)

class Record:
    def __init__(self,amount,comment,date=''):
        self.amount = amount
        self.comment = comment
        if date == '':
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date,'%d.%m.%Y').date()

class CashCalculator(Calculator):
    USD_RATE = 90.0
    EURO_RATE = 80.0
    def __init__(self,limit):
        super().__init__(limit)        
    
    def get_today_cash_remained(self,currency):
        #посчитать сколько денег потрачено сегодня
        res = self.limit - super().get_today_stats()
        if currency == 'usd':
            k = self.USD_RATE
            txt = 'USD'
        elif currency == 'eur':
            k = self.EURO_RATE
            txt = 'Euro'
        else:
            k = 1
            txt = 'руб'
        res = round(res/k,2)
        if res > 0:
            return(f'На сегодня осталось {res} {txt}')
        elif res == 0:
            return('Денег нет, держись')
        else:
            return(f'Денег нет, держись: твой долг - {-res} {txt}')

class CaloriesCalculator(Calculator):
    def __init__(self,limit):
        super().__init__(limit)

    def get_calories_remained(self):
        #посчитать сколько калорий осталось на сегодня
        res = self.limit - super().get_today_stats()
        if res > 0:
            return(f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {res} кКал')
        else:
            return('Хватит есть!')
