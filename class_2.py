class empolyee:
    amount = 1.05
    employee_count=0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@email.com"
        empolyee.employee_count+=1

    def full_name(self):
        return f"{self.first} {self.last}"

    def raise_amount(self):
        return int(self.pay * self.amount)
    @classmethod
    def set_amount(cls,money):
        cls.amount=money


emp = empolyee("venkatesh", "nanduri", 50000)
emp1=empolyee("nanduri","reddy",60000)
print(empolyee.set_amount(1.09))
print(emp1.full_name())
print(emp.raise_amount())

print(emp.email)
print(emp.full_name())
print(emp1.raise_amount())
print(empolyee.employee_count)
