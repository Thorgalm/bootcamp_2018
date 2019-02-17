# MOJE:
# class Employee:
#     def __init__(self, name, last_name, rate_per_hour):
#         self.name = name
#         self.last_name = last_name
#         self.rate_per_hour = rate_per_hour
#         self.reg_time = 0
#
#     def register_time(self, hours):
#         self.reg_time = hours
#
#     def pay_salary(self):
#         if self.reg_time <= 8:
#             salary = self.rate_per_hour * self.reg_time
#         if self.reg_time > 8:
#             salary = self.rate_per_hour * (self.reg_time - 8) * 2 + 8 * self.rate_per_hour
#         self.reg_time = 0 #zerujemy atrybut, zeby po ponownym wywolaniu pay_salary pokazywał,ze wypłata jest 0
#         return salary

class Employee:
    def __init__(self, name, last_name, rate_per_hour):
        self.name = name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour
        self.reg_time = 0
        self.reg_overtime = 0

    def register_time(self, hours):
        # if hours > 8:
        #     self.reg_overtime = hours - 8
        #     self.reg_time = 8
        # else:
        #     self.reg_time += hours
        if hours > 8:
            self.reg_time += 8 + (hours - 8 ) *2
        else:
            self.reg_time += hours
            
    def pay_salary(self):
        salary = self.rate_per_hour * self.reg_time + self.rate_per_hour * self.reg_overtime *2
        self.reg_time = 0 #zerujemy atrybut, zeby po ponownym wywolaniu pay_salary pokazywał,ze wypłata jest 0
        self.reg_overtime = 0
        return salary

# employee = Employee('Jan', 'Nowak', 100.0)
# employee.register_time(5)
# employee.pay_salary()
#
# employee.register_time(10)
# employee.pay_salary()

employee = Employee('Jan', 'Nowak', 100.0)
employee.register_time(10)
print(employee.pay_salary())

def test_employee_initialization():
    employee = Employee('Jan', 'Nowak', 100.0)

    assert employee.name == "Jan"
    assert employee.last_name == "Nowak"
    assert employee.rate_per_hour == 100

def test_pay_salary():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)

    assert employee.pay_salary() == 500
    assert employee.pay_salary() == 0

def test_pay_salary_over_time():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(10)

    assert employee.pay_salary() == 1200
    assert employee.pay_salary() == 0

def test_pay_salary_many_registration():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    employee.register_time(5)

    assert employee.pay_salary() == 1000
    assert employee.pay_salary() == 0

def test_pay_salary_many_registration():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(10)
    employee.register_time(10)

    assert employee.pay_salary() == 2400
    assert employee.pay_salary() == 0