import requests

class CurrencyConverter:
    def __init__(self):
        self.rates = {}
    def get_rates(self):
        response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
        if response.status_code == 200:
            data = response.json()
            for item in data:
                self.rates[item['cc']] = item['rate']
        else:
            print("Error fetching exchange rates. Please try again.")
    def convert(self, amount, from_currency, to_currency):
        if from_currency != "UAH":
            amount = amount / self.rates[from_currency]
        amount = round(amount * self.rates[to_currency], 2)
        return amount
converter = CurrencyConverter()
converter.get_rates()
while True:
    try:
        amount = float(input("Enter the amount of currency: "))
        from_currency = input("Enter the currency code of the amount you entered: ").upper()
        to_currency = "USD"
        converted_amount = converter.convert(amount, from_currency, to_currency)
        print("The amount of {} {} is equal to {:.2f} USD".format(amount, from_currency, converted_amount))
        break
    except KeyError:
        print("Invalid currency code entered. Please try again.")
    except ValueError:
        print("Invalid amount entered. Please try again.")