def can_withdraw(balance, amount):
    if balance - amount >= 50000 and amount % 10000 == 0:
        return True
    return False

    