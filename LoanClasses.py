import numpy as np

MONTHSINYEAR = 12

class Loan:    
    def __init__(self, loanAmount, interestRate, amortizationRate):
        self.loanAmount = loanAmount
        self.interestRate = interestRate
        self.amortizationRate = amortizationRate
        self.remainingLoan = loanAmount
        self.remainingInterest = 0
        self.__updateTotal()

    def __updateTotal(self):
        self.remainingToPay = self.remainingLoan + self.remainingInterest

    def __payLoan(self, amount):
        interestPaid = np.min([self.remainingInterest, amount])
        self.remainingInterest -= interestPaid

        loanPaid = 0

        if amount > interestPaid:
            loanPaid = np.min([self.remainingLoan, amount - interestPaid])
            self.remainingLoan -= loanPaid

        self.__updateTotal()

        return interestPaid + loanPaid

    def performLoanLoopSeries(self):
        costPerMonth = self.loanAmount * self.amortizationRate
        
        interestPerMonth = self.interestRate/MONTHSINYEAR

        totalCost = 0

        while self.remainingLoan > 0:
            self.remainingInterest += self.remainingToPay * interestPerMonth

            self.__updateTotal()

            print(self.remainingLoan, self.remainingInterest, self.remainingToPay)

            totalCost += self.__payLoan(costPerMonth + self.remainingInterest)

        print(totalCost)


            
