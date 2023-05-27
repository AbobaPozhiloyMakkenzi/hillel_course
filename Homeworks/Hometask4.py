#task1Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів, які містять дві голосні літери підряд.
vowels = ['a', 'e', 'i', 'o', 'u']
sentence = input('please, print your sentence').strip().split()
list = 0
for word in sentence:
    for i in range(len(word)-1):
        if word[i] in vowels and word[i] == word[i+1]:
            list += 1
print(list)

# #task2 Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною
lower_limit = 35.9
upper_limit = 37.339
shop_list = { "cito": 47.999,
              "BB_studio": 42.999,
              "momo": 49.999,
              "main-service": 37.245,
              "buy.now": 38.324,
              "x-store": 37.166,
              "the_partner": 38.988,
              "store": 37.720,
              "rozetka": 38.003}
for res in shop_list.items():
    if res[1] >= lower_limit and res[1] <= upper_limit:
       print(res)

