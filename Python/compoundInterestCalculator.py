#COMPOUND INTEREST CALCULATOR 

#TO FIND THE COMPOUND INTEREST, WE USE THE FORMULA A = P(1 + r/n)^(nt)
      #WHERE A = THE FUTURE VALUE OF THE INVESTMENT/LOAN, INCLUDING INTEREST  
      #P = THE PRINCIPAL INVESTMENT AMOUNT (THE INITIAL DEPOSIT OR LOAN AMOUNT)
      #r = THE ANNUAL INTEREST RATE (DECIMAL)
      #n = THE NUMBER OF TIMES THAT INTEREST IS COMPOUNDED PER YEAR
      #t = THE NUMBER OF YEARS THE MONEY IS INVESTED OR BORROWED FOR
# THEN COMPOUND INTEREST CAN BE CALCULATED AS CI = A - P

#input values
P = float(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate (in percentage): ")) / 100  #convert percentage to decimal
n = int(input("Enter the number of times interest is compounded per year: "))
t = int(input("Enter the number of years the money is invested or borrowed for: "))

#calculating amount

A = P * (1 + (r/n)) ** (n * t)

#calculating compound interest

CI = A - P

print(f"THE COMPOUND INTEREST FOR PRINCIPAL AMOUNT {P} AT ANNUAL INTEREST RATE {r*100}% COMPOUNDED {n} TIMES PER YEAR FOR {t} YEARS IS: {CI:.2f}")