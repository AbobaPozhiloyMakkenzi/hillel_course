
import requests
my_link = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
res = requests.request('GET', my_link)
responce_json = res.json()
list_of_names = []
list_of_rates = []
exchangedate = '03.07.2023'
class Iterator:
    def __iter__(self):
        self.counter = -1
        return self
    def __next__(self):
        self.counter += 1
        if self.counter >= 61:
            raise StopIteration
        return responce_json[self.counter]

Iter_obj = Iterator()

for i in Iter_obj:
    list_of_names.append(i['txt'])
    list_of_rates.append(i['rate'])


class ForeignCurrency:

    def __init__(self, currency,value):

        self.currency = [i for i in currency]
        self.value = [i for i in value]


class Zippers:
    @property
    def zipper(self):
        res = dict(zip(list_of_names,list_of_rates))
        return res.keys()
    @property
    def zipper2(self):
        res = dict(zip(list_of_names, list_of_rates))
        return res.values()


zip1 = Zippers()
zip2 = zip1.zipper
zip3 = zip1.zipper2
frgn = ForeignCurrency(zip2,zip3)

with open('currencies.txt', 'w') as file:
    counter = 0
    while True:
        for i in frgn.currency, frgn.value, 1, 2, 3:
            file.write(str(f'{counter+1}){frgn.currency[counter]} to UAH currency: {frgn.value[counter]} \n'))
            if counter >= 60:
                raise StopIteration
            counter += 1




