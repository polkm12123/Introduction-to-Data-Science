# -*- coding: utf-8 -*-
"""week11 A16260073張雅雯

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q9PStX1N0cM78_loqgFaoiJafUsFL9cJ
"""

primes=[2,3,5,7,11]
print(type(primes))

primes=(2,3,5,7,11)
print(type(primes))

print(primes[0]) #第0筆是什麼數字
print(primes[1])
print(primes[-1])
print(primes[-2])

print(primes[::2])

primes_list=[2,3,5,7,11]
primes_list[-1]=13 #最後一個換13
print(primes_list)

print(len(primes_list))

#insert制訂新放入的地方
primes_list.insert(-1,11) #長度更動
print(primes_list)

primes_list.pop()
print(primes_list)

print(primes)
print(type(primes))

primes[-1]=13

primes.append(13) #無append

x= 0.25
print(type(x))
print(x.as_integer_ratio())#1是分子，4是分母
print (type(x.as_integer_ratio()))

def where_are_you_from(city,country):
  return city,country

print(where_are_you_from("Taipei","Taiwan"))
print(type(where_are_you_from("Taipei","Taiwan")))

my_city,my_country=where_are_you_from("Taipei","Taiwan")
print(my_city)
print(my_country)

numerator , denominator=x.as_integer_ratio()
print(numerator)
print(denominator)

the_avengers = {
    "Iron Man": "Tony Stark",
    "Captain America": "Steve Rogers",
    "Hulk": "Bruce Banner",
    "Thor": "Thor",
    "Black Widow": "Natasha Romanoff",
    "Hawkeye": "Clint Barton"
}
print(the_avengers)
print(type(the_avengers))

#獲取 dict 的標籤與資料
#keys()：取得標籤
#values()：取得資料
#items()：同時取得標籤和資料

print(the_avengers.keys())

print(the_avengers.values())

print(the_avengers.items())

print(the_avengers["Iron Man"])
print(the_avengers["Captain America"])
print(the_avengers["Hulk"])
print(the_avengers["Thor"])
print(the_avengers["Black Widow"])
print(the_avengers["Hawkeye"])

living_area=input("請輸入您的居住縣市:")
print(living_area)
print("{}每人每月最低生活費為{:,}".format(living_area,17005))

living_area=input("請輸入您的居住縣市:")
living_cost=None
if living_area=="臺北市":
  living_cost=17005
elif living_area=="新北市":
  living_cost=15500
elif living_area=="桃園市":
  living_cost=15281
elif living_area=="台中市":
  living_cost=14596
elif living_area=="台南市":
  living_cost=12388
elif living_area=="高雄市":
  living_cost=13099
elif living_area=="非六都之縣市":
  living_cost=12388
elif living_area=="金門縣連江縣":
  living_cost=11648
if living_cost is None:
  print("請輸入居住縣市")
else:
  print("請重新輸入居住城市，每人每月最低生活費為{}".format(living_cost))
print("{}每人每月最低生活費為{:,}".format(living_area,17005))

living_cost_dict= {
    "臺北市":17005,
    "新北市":15500,
    "桃園市":15281,
    "台中市":14596,
    "台南市":12388,
    "高雄市":13009,
    "非六都之縣市":12388,
    "金門縣連江縣":11648
}
living_area=input("請輸入你的居住城市:")
try:
  living_cost=living_cost_dict[living_area]
  print("{}每人每月最低生活費為{:,}".format(living_area,living_cost))
except KeyError:
   print("請輸入居住縣市")

#@title 哈哈
living_area = '\u81FA\u5317\u5E02' #@param ['臺北市', '新北市', '桃園市', '臺中市', '臺南市', '高雄市', '非六都之縣市', '金門縣連江縣']
living_cost = living_cost_dict[living_area]
print("{}的每人每月最低生活費為{:,}".format(living_area, living_cost))

primes=(2,3,5,7,11,13,13,11,11,11,2,2,2)
print(primes)

primes_list = [2, 3, 3, 3, 5, 5]
print(primes_list)

set(primes_list)

primes = {2, 3, 5, 7, 11, 13, 13, 13, 11, 11, 11, 11, 2, 2, 2}
print(primes)

primes={2,3,5,7,11,13}
odds={1,3,5,7,9,11,13}
print(type(primes))
print(type(odds))

#交集
primes&odds

# .intersection
primes.intersection(odds)

# 聯集
primes | odds

#.union
primes.union(odds)

#差異
print(primes - odds)
print(odds - primes)

#.difference
print(primes.difference(odds))
print(odds.difference(primes))

(primes - odds) | (odds - primes)

#對稱差異
primes^odds

#.symmetric_difference
print(primes.symmetric_difference(odds))

help(iter)

I=iter(primes)
next (I)

next(I)

next(I)

next(I)

next(I)
next(I)

next(I)

primes[0]

import requests

today_json = requests.get("https://data.nba.net/10s/prod/v1/today.json").json()
print(type(today_json))

today_json.keys()

print(type(today_json['links']))

today_json['links']['leagueRosterPlayers']

primes_list = [2, 3, 5, 7, 11]
I = iter(primes_list)
next(I)

primes_tuple = (2, 3, 5, 7, 11)
I = iter(primes_tuple)
next(I)

I = iter(living_cost_dict.keys())
next(I)

I = iter(living_cost_dict.values())
next(I)

I = iter(living_cost_dict.items())
next(I)

may4th = "Luke, use the Force!"
I = iter(may4th)
next(I)

I = iter(5566)

I = iter(5566.0)

I = iter(False)

help(range)

for i in range(1, 101, 1):
    print(i)

