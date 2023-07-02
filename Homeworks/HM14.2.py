
import requests
my_link = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
res = requests.request('GET', my_link)
responce_json = res.json()


with open('currencies.txt', 'w') as file:
    for i in range(len(responce_json)):
        data = responce_json[i]
        name, rate = data['txt'], data['rate']
        file.write(str(f'{i+1}) {name} to UAH currency: {rate} \n'))

