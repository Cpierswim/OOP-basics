from AlarmClock import AlarmClock

class Person:
    def __init__(self, name: str, money_to_start_with: int) -> None:
        self.name = name
        self.account_value = money_to_start_with

    def withdraw(self, amout_to_withdraw: int) -> int:
        if(self.account_value - amout_to_withdraw < 0):
            print("Insufficient Funds, amount not withdrawn")
            return -1
        else:
            self.account_value -= amout_to_withdraw
            return self.account_value

    def deposit(self, amount_to_deposit: int, who_is_depositing: str) -> int:
        self.account_value += amount_to_deposit
        print(f"{who_is_depositing} deposited ${amount_to_deposit} into the {self.name} account, which now has ${self.account_value}")


person_one = Person("Chris", 0)
person_two = Person("John", 100)
person_two.withdraw(100)
person_one.deposit(100, person_two.name)
