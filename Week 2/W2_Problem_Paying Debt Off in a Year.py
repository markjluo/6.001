balance = float(input('Enter the Balance: '))
annualInterestRate = float(input('Enter the Annual Interest Rate: '))
Num_months = int(input('Months to Pay off: '))
mir = annualInterestRate/12


def re(balance, mir, payment, Num_months):
    remaining = balance
    for i in range(Num_months):
        remaining = (remaining-payment)*(1+mir)
    return remaining


lower = balance/Num_months
upper = (balance*(1+mir)**Num_months)/Num_months
payment = (upper + lower)/2

guess = 0
while re(balance, mir, payment, Num_months) > 0:
    payment += 0.1
    guess += 1
while re(balance, mir, payment, Num_months) < 0:
    payment -= 0.1
    guess += 1


print(guess)
print('Lowest payment:', round(payment, 2))


