class Employee(object):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class HourlyEmployee(Employee):

    def __init__(self, name, wage):
        super().__init__(name)
        self.wage = wage

    def weekly_pay(self, hours):
        if hours > 40:
            bonus = (hours - 40) * 1.5
            self.pay = self.hours * self.wage + bonus
        elif hours <= 40:
            self.pay = hours * self.wage
        return self.pay


class SalariedEmployee(Employee):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def weekly_pay(self, hours):
        return self.salary


class Manager(Employee):

    def __init__(self, name, wage, bonus):
        super().__init__(name)
        self.wage = wage
        self.bonus = bonus

    def weekly_pay(self, hours):
        return self.wage + self.bonus


staff = []
staff.append(HourlyEmployee("Morgan, Harry", 30.0))
staff.append(SalariedEmployee("Lin, Sally", 52000.0))
staff.append(Manager("Smith, Mary", 104000.0, 50.0))
for employee in staff:
    # print(employee)
    hours = int(input("Hours worked by " + employee.get_name() + ": "))
    pay = employee.weekly_pay(hours)
    print("Salary: %.2f" % pay)
