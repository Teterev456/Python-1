class Wallet:
    def __init__(self, balance:  float = 0, currency: str = "", wallet_name: str = "Wall1", payment_system: str = ""):
        self._balance = balance
        self.currency = currency
        self.wallet_name = wallet_name
        self.payment_system = payment_system

    def deposit(self):
        self.currency = input("Выберите валюту для пополнения: ")
        self.payment_system = input("Введите платежную систему: ")
        dep_value = float(input("Сумма к пополнению: "))
        self._balance += dep_value
        return f"Вы успешно пополнили счет на: {dep_value} {self.currency} через платежную систему {self.payment_system}"

    def payment(self):
        currency = self.currency
        currency_payment = input(f"Выберите валюту для оплаты({self.currency}): ")
        while currency != currency_payment:
            print("Такой валюты на вашем счету нет, попробуйте снова")
            currency_payment = input(f"Выберите валюту для оплаты({self.currency}): ")
        money_for_payment = float(input(f"Введите количество средств для оплаты: "))
        if money_for_payment > self._balance:
            return "На вашем счёте недостаточно средств."
        else:
            self._balance -= money_for_payment
            return f"Вы успешно списали {money_for_payment} {self.currency}."

    def info(self):
        return f"Счет - {self.wallet_name}\nКоличество средств на балансе: {self._balance} {self.currency}"

    def delete(self):
        answer = input("Удалить счёт?(y/n): ")
        while answer != "y" or answer != "n":
            print("Такой команды не существует, попробуйте снова.")
            answer = input("Удалить счёт?(y/n): ")
            if answer == "y":
                self._balance = 0
                self.wallet_name = "None"
                self.currency = ""
                return "Вы успешно удалили свой аккаунт."
            elif answer == "n":
                return "Удаление счета отменено."


class CryptoWallet(Wallet):
    def __init__(self, coin:  str = "", balance:  float = 0, currency: str = "", wallet_name: str = "Wall1", payment_system: str = ""):
        self.coin = coin in ("BTC", "ETH")
        super().__init__(balance=balance, currency=currency, wallet_name=wallet_name, payment_system=payment_system)

    def info(self):
        self.coin = self.currency
        if self.coin == "BTC":
            value = 72000
            return f"Счет - {self.wallet_name}\nКоличество средств на балансе: {self._balance} {self.coin} = {self._balance * value} USD"
        elif self.coin == "ETH":
            value = 3500
            return f"Счет - {self.wallet_name}\nКоличество средств на балансе: {self._balance} {self.coin} = {self._balance * value} USD"
        else:
            return f"Счет - {self.wallet_name}\nКоличество средств на балансе: {self._balance} {self.coin} = 0 USD(Информации о цене данной монеты нет.)"
