class Employee:
    def __init__(self, name, last_name, rate_per_hour):
        self.name = name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour
        self.reg_time = 0
        self.reg_overtime = 0

    def register_time(self, hours):
        if hours > 8:
            self.reg_time += 8 + (hours - 8) * 2
        else:
            self.reg_time += hours

    def pay_salary(self):
        salary = self.rate_per_hour * self.reg_time + self.rate_per_hour * self.reg_overtime * 2
        self.reg_time = 0  # zerujemy atrybut, zeby po ponownym wywolaniu pay_salary pokazywał,ze wypłata jest 0
        self.reg_overtime = 0
        return salary


class PremiumEmployee(Employee):

    def __init__(self, name, last_name, rate_per_hour):
        super().__init__(name, last_name, rate_per_hour)
        self.bonus = 0

    def give_bonus(self, amount):
        self.bonus += amount

    def pay_salary(self):
        to_pay = super().pay_salary() + self.bonus
        self.bonus = 0
        return to_pay


def test_premiumEmployee_give_bonus():
    employee = PremiumEmployee('Jan', 'Słodowy', 100.0)
    employee.register_time(5)
    employee.give_bonus(1000.0)

    assert employee.pay_salary() == 1500
    assert employee.pay_salary() == 0
