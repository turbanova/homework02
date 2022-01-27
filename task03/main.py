def get_key(k):
    for key, value in seasons.items():
         if k in value:
             return key
 
    return "Такого месяца нет"


seasons = dict({"winter": [1, 2, 12], "spring": [3, 4, 5], "summer": [6, 7, 8], "autumn" : [9, 10, 11]})
k = input("Введите индекс месяца")
print(str(get_key(int(k))))