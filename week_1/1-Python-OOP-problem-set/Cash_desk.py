import copy


class Cash_desk(object):

    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, money):
        for key in money:
            self.money[key] += money[key]
        print(self.money)
        return self.money

    def total(self):
        money = self.money
        total = 0
        for key in money:
            total += key * money[key]
        return total

    def can_withdraw_money(self, amount_of_money):
        money = self.money.copy()
        total = self.total()
        if amount_of_money == total:
            return True
        elif amount_of_money < total:
            banknotes = sorted(list(money))[::-1]
            # print(banknotes)
            for banknote in banknotes:
                while money[banknote] > 0:
                    if amount_of_money - banknote >= 0:
                        amount_of_money -= banknote
                        money[banknote] -= 1
                    else:
                        break
            return amount_of_money == 0

my_cash_desk = Cash_desk()
my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
print(my_cash_desk.total())
print(my_cash_desk.can_withdraw_money(30))
print(my_cash_desk.can_withdraw_money(70))
# my_cash_desk.take_money({20: 1})
# print(my_cash_desk.can_withdraw_money(91))
