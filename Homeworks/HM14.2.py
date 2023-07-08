import json
import matplotlib.pyplot as plt
import requests
dates = []
values = []
currencies = ['EUR',"USD"]

while True:

    while True:
        pick = input('pick the currency!').upper().strip()
        if not isinstance(pick,str):
            break
        elif pick not in currencies:
            print('wrong name of the currency')
        else:

            date = int(input('pick the date!'))
            if not isinstance(date,int):
                break
            iter_num = 2024 - date


            for i in range(iter_num):
                link = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json&valcode={pick}&date={date+i}0101'
                dates.append(int(date+i))
                try:
                    res = requests.request('GET', link)
                except Exception as e:
                    print(e)
                else:
                    responce_json = res.json()
                    with open('currencies.txt', 'a') as file:
                        for i in range(len(responce_json)):
                            data = responce_json[i]
                            name, rate = data['txt'], data['rate']
                            values.append(data['rate'])
                            file.write(str(f'{data["exchangedate"]}) {name} to UAH currency: {rate} \n'))
        if input('Wanna get a report?') == 'yes':
            break

    fig, ax = plt.subplots()

    ax.plot(dates, values)
    ax.set_title = 'Currencies'
    ax.set_xlabel('Year')
    ax.set_ylabel('Rate')

    ax.scatter(dates, values)

    plt.show()

    decision = input('wanna continue?').strip().lower()
    if decision != 'yes':
        break


