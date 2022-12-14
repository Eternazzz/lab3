
import datetime as dt


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.today = dt.date.today()
        self.week_ago = self.today - dt.timedelta(7)

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        day_stats = []
        for record in self.records:
            if record.date == self.today:
                day_stats.append(record.amount)
        return sum(day_stats)

    def get_week_stats(self):
        week_stats = []
        for record in self.records:
            if self.week_ago <= record.date <= self.today:
                week_stats.append(record.amount)
        return sum(week_stats)

    def remained(self):
        return(self.limit - self.get_today_stats())


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        calories_remained = self.remained()
        if calories_remained > 0:
            message = (f'Сегодня можно съесть что-нибудь ещё, но с общей'
                       f'калорийностью не более {calories_remained} кКал')
        else:
            message = 'Хватит есть!'
        return message


class CashCalculator(Calculator):
    USD_RATE = 56.3
    EURO_RATE = 53.1
    RUB_RATE = 1

    def get_today_cash_remained(self, currency='rub'):
        currencies = {'usd': ('USD', CashCalculator.USD_RATE),
                      'eur': ('Euro', CashCalculator.EURO_RATE),
                      'rub': ('руб', CashCalculator.RUB_RATE)}
        cash_remained = self.remained()
        if cash_remained == 0:
            return 'Денег нет, держись'
        if currency not in currencies:
            return f'Валюта {currency} не поддерживается'
        sign, rate = currencies[currency]
        cash_remained = round(cash_remained / rate, 2)
        if cash_remained > 0:
            message = f'На сегодня осталось {cash_remained} {sign}'
        else:
            cash_remained = abs(cash_remained)
            message = (f'Денег нет, держись: твой долг - {cash_remained} '
                       f'{sign}')
        return message


class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


if __name__ == '__main__':
    cash_calculator1 = CashCalculator(1000)
    cash_calculator1.add_record(Record(amount=145, comment='кофе'))
    cash_calculator1.add_record(Record(amount=300, comment='Серёге за обед'))
    cash_calculator1.add_record(Record(amount=3000,
                                  comment='бар в Танин др',
                                  date='08.11.2019'))
    print(cash_calculator1.get_today_cash_remained('rub'))
import datetime as dt


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.today = dt.date.today()
        self.week_ago = self.today - dt.timedelta(7)

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        day_stats = []
        for record in self.records:
            if record.date == self.today:
                day_stats.append(record.amount)
        return sum(day_stats)

    def get_week_stats(self):
        week_stats = []
        for record in self.records:
            if self.week_ago <= record.date <= self.today:
                week_stats.append(record.amount)
        return sum(week_stats)

    def remained(self):
        return(self.limit - self.get_today_stats())


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        calories_remained = self.remained()
        if calories_remained > 0:
            message = (f'Сегодня можно съесть что-нибудь ещё, но с общей'
                       f'калорийностью не более {calories_remained} кКал')
        else:
            message = 'Хватит есть!'
        return message


class CashCalculator(Calculator):
    USD_RATE = 56.3
    EURO_RATE = 53.1
    RUB_RATE = 1

    def get_today_cash_remained(self, currency='rub'):
        currencies = {'usd': ('USD', CashCalculator.USD_RATE),
                      'eur': ('Euro', CashCalculator.EURO_RATE),
                      'rub': ('руб', CashCalculator.RUB_RATE)}
        cash_remained = self.remained()
        if cash_remained == 0:
            return 'Денег нет, держись'
        if currency not in currencies:
            return f'Валюта {currency} не поддерживается'
        sign, rate = currencies[currency]
        cash_remained = round(cash_remained / rate, 2)
        if cash_remained > 0:
            message = f'На сегодня осталось {cash_remained} {sign}'
        else:
            cash_remained = abs(cash_remained)
            message = (f'Денег нет, держись: твой долг - {cash_remained} '
                       f'{sign}')
        return message


class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


if __name__ == '__main__':
    cash_calculator1 = CashCalculator(1000)
    cash_calculator1.add_record(Record(amount=145, comment='кофе'))
    cash_calculator1.add_record(Record(amount=300, comment='Серёге за обед'))
    cash_calculator1.add_record(Record(amount=3000,
                                  comment='бар в Танин др',
                                  date='08.11.2019'))
    print(cash_calculator1.get_today_cash_remained('rub'))
import datetime as dt


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.today = dt.date.today()
        self.week_ago = self.today - dt.timedelta(7)

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        day_stats = []
        for record in self.records:
            if record.date == self.today:
                day_stats.append(record.amount)
        return sum(day_stats)

    def get_week_stats(self):
        week_stats = []
        for record in self.records:
            if self.week_ago <= record.date <= self.today:
                week_stats.append(record.amount)
        return sum(week_stats)

    def remained(self):
        return(self.limit - self.get_today_stats())


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        calories_remained = self.remained()
        if calories_remained > 0:
            message = (f'Сегодня можно съесть что-нибудь ещё, но с общей'
                       f'калорийностью не более {calories_remained} кКал')
        else:
            message = 'Хватит есть!'
        return message


class CashCalculator(Calculator):
    USD_RATE = 56.3
    EURO_RATE = 53.1
    RUB_RATE = 1

    def get_today_cash_remained(self, currency='rub'):
        currencies = {'usd': ('USD', CashCalculator.USD_RATE),
                      'eur': ('Euro', CashCalculator.EURO_RATE),
                      'rub': ('руб', CashCalculator.RUB_RATE)}
        cash_remained = self.remained()
        if cash_remained == 0:
            return 'Денег нет, держись'
        if currency not in currencies:
            return f'Валюта {currency} не поддерживается'
        sign, rate = currencies[currency]
        cash_remained = round(cash_remained / rate, 2)
        if cash_remained > 0:
            message = f'На сегодня осталось {cash_remained} {sign}'
        else:
            cash_remained = abs(cash_remained)
            message = (f'Денег нет, держись: твой долг - {cash_remained} '
                       f'{sign}')
        return message


class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


if __name__ == '__main__':
    cash_calculator1 = CashCalculator(1000)
    cash_calculator1.add_record(Record(amount=145, comment='кофе'))
    cash_calculator1.add_record(Record(amount=300, comment='Серёге за обед'))
    cash_calculator1.add_record(Record(amount=3000,
                                  comment='бар в Танин др',
                                  date='08.11.2019'))
    print(cash_calculator1.get_today_cash_remained('rub'))  # На сегодня осталось 555.0 руб

    calories_calculator1 = CaloriesCalculator(1500)
    calories_calculator1.add_record(Record(amount=300, comment='завтрак'))
    calories_calculator1.add_record(Record(amount=750, comment='обед'))
    print(calories_calculator1.get_calories_remained())  # Сегодня можно съесть что-нибудь ещё
    # но с общей калорийностью не более 450 кКал
