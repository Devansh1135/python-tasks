from datetime import date, time , datetime , timedelta
class DateUtils:

    def __init__(self, date, format):
        self.date = date
        self.format = format

    def __repr__(self):
        return f'date : {self.date}, format : {self.format}'
        
    def days_until(self,target_date):
        return target_date - self.date

    @classmethod
    def from_string(cls, date_string, format):
        return cls(date_string, format)

    @staticmethod
    def is_valid_date(year, month, day):
        if 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999:
            return "Valid"
        
        return "Invalid Date!!!"

    @staticmethod
    def is_leap_year(year):
        if year%4 == 0:
            return True
        return False
    
print(DateUtils.is_leap_year(2016))

date1 = DateUtils.from_string(11-3-2024, 'DD/MM/YY')
# print(date1.days_until(15-3-2025))




