class Data:
    def __init__(self, day_month_year):
        # self.day = day
        # self.month = month
        # self.year = year
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Дата введена верно!'
                else:
                    return f'Неверно введен год!'
            else:
                return f'Неверно введен месяц!'
        else:
            return f'Неверно введен день!'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('1 - 1 - 2021')
print(today)
print(Data.valid(11, 11, 2022))
print(today.valid(11, 13, 2011))
print(Data.extract('31 - 12 - 2011'))
print(today.extract('21 - 11 - 2020'))
print(Data.valid(11, 9, 2000))
