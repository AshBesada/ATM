import sys

# account balance
account_balance = float(500.25)


# print balance function
def print_balance():
    # example of functions that return the correct output
    print('Your current balance: \n', account_balance)

# deposit function


def deposit(amount):
    print('Deposit was $%.2f, current balance is $%.2f' %
          (amount, account_balance + amount))  # input (parameters) that are utilized within the function(s

# withdraw function


def withdraw(amount):
    if amount > account_balance:
        print('$%.2f is greater than your account balance of $%.2f' %
              (amount, account_balance))  # example of functions that return the correct output
    else:
        print('Withdrawal amount was $%.2f, current balance is $%.2f' %
              (amount, account_balance - amount))

# quit function


def quit():
    print("Thank you for banking with us.")


# get user input
userchoice = input("What would you like to do?\n")

# determine which function to run
if userchoice == 'B':
    print_balance()

elif userchoice == 'D':
    deposit_amount = float(
        input('How much would you like to deposit today?\n'))
    deposit(deposit_amount)
elif userchoice == 'W':
    withdrawal_amount = float(
        input('How much would you like to withdraw today?\n'))
    withdraw(withdrawal_amount)
elif userchoice == 'Q':
    quit()

# Pause program on screen until user hit the enter key.
input("Press \"Enter\" to close")