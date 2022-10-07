import datetime as dt
class Calculator:
    def __init__(self,limit):
        self.limit=limit
        self.today=dt.date.today()
        self.week=self.today-dt.timedelta(7)
        self.records = []
    def add_record(self,record):
        self.records.append(record)
    def get_today_stats(self):
        today=dt.date.today()
        today_stats=sum(Record.amount for record in records
                        if record.date==today)
    def get_week_stats(self):
        week_stats=[]
        for record in self.records:
            if self.week<=record.date<=self.today:
                week_stats.append(record.amount)
        return sum(week_stats)
    def get_today_remained(self):
        remainder=self.limit-self.get_today_stats()
        return remainder
class Record(Calculator):
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date=dt.date.today()
        else:
            self.date = dt.datetime.strptime(date,'%d.%m.%Y').date()
class CashCalculator(Calculator):
    USD_ExchangeRate=60
    EURO_ExchangeRate=57
    RUB_ExchangeRate=1
    def get_today_cash_remained(self,currency='rub'):
        currencies={'usd':('USD',CashCalculator.USD_ExchangeRate),
                    'eur':('Euro',CashCalculator.EURO_ExchangeRate),
                    'rub':('Rub',CashCalculator.RUB_ExchangeRate)}
        cash_remained=self.get_today_remained()
        if cash_remained==0:
            return 'Деньги закончились'
        if cash_remained>0:
            message=f'На сегодня осталось {cash_remained} {name}'
        else:
            cash_remained=abs(cash_remained)
            message=(f'Деньги закончились, твой долг равен {cash_remained} {name}')
        return  message
if __name__=='main':
    cash_calculator=CashCalculator(1000)
    cash_calculator.add_record(Record(amount=145,comment="Кофе"))
    print(cash_calculator.get_today_cash_remained("rub"))