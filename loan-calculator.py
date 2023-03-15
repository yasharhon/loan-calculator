import LoanClasses as LC

def main():
    myLoan = LC.Loan(10000, 1.44, 0.2)
    myLoan.performLoanLoopSeries()
    
if __name__ == '__main__':
    main()
