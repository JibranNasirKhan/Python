class RateofInterest:
    interest = .06
    def __init__(self, name, loanamt):
        self.name = name
        self.loanamt = loanamt

    def cal_interest(self):
        print("Your interest is: ", self.loanamt * self.interest)

class Student(RateofInterest):
    interest = .04

c = Student("Jibran", 500000)
c.cal_interest()

