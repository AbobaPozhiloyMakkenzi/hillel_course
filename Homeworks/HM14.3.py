
import requests
my_link = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'

with open('currencies.txt', 'w') as file:
    file.write('\n'.join(list(map(lambda item: f'{item[0]+1}) {item[1]["txt"]} to UAH currency: {item[1]["rate"]}', enumerate(requests.request('GET', my_link).json())))))
