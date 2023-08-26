class RateofInterest:
    interest = 0.06
    def __int__(self, name, loan):
        self.name = name
        self.loan = loan

    def calc_interest(self):
        print("Your interest is: ", self.loan * RateofInterest.interest)

per = RateofInterest("Jibran", 50000)
RateofInterest.interest = .08
per.calc_interest(RateofInterest)