# -*- coding: utf-8 -*-
"""week14 A106260073張雅雯

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Nxba0CnApzEtwddrF07yxQwyrQGpgKMi
"""

lucky_number=24
print("My lucky number is %s"%(lucky_number))
print("My lucky number is{}".format(lucky_number))

pi=3.14159
print("My lucky number is %.2f"%(lucky_number)) #小數點去到第二位，偏c語言
print("My lucky number is{}".format(lucky_number))

help(eval) #input轉印成物件

pi #物件的名稱

print('pi')

eval('pi')

def find_divisors(x):#尋找一個因數
  for i in range(1,x+1):
    if x %i==0:
      print(i)

find_divisors(8)

def count_divisors(x):
  n_divisors=0
  for i in range(1,x+1):
    if x%i==0:
      print(i)
      n_divisors+=1

count_divisors(8)

def count_divisors(x):
  n_divisors=0
  for i in range(1,x+1):
    if x%i==0:
      n_divisors+=1
  print(n_divisors)

my_int=8 #整數
my_int_n_divisors=count_divisors(my_int) #答案的4未存起來

print(my_int_n_divisors) #都未存到 少了一個元件return

def count_divisors(x):
    n_divisors = 0
    for i in range(1, x+1):
        if x % i == 0:
            #print(i)
            n_divisors += 1
    return n_divisors

my_int = 8
my_int_n_divisors = count_divisors(my_int)

print(my_int_n_divisors)

def is_prime(x):#個數
  div_cnt=count_divisors(x)
  if div_cnt==2:
    print("{}是質數".format(x))
  else:
    print("{}不是質數".format(x))

is_prime(2)#判斷是否為質數

is_prime_res=is_prime(2)
print(is_prime_res)

def is_prime(x):#個數
  div_cnt=count_divisors(x)
  if div_cnt==2:
    return True
  else:
    return False

is_prime_res=is_prime(2)
print(is_prime_res)

def is_prime(x):#個數
  div_cnt=count_divisors(x)
  return div_cny==2

def is_prime(x):#個數
  return count_divisors(x)==2

for i in range (1,11):
  print("{}是否為質數:{}".format(i,is_prime(i)))

#一對多
def find_divisors(x): 
  divisors=[]
  for i in range(1, x+1):
        if x % i == 0:
          divisors.append(i)
  return divisors

find_divisors(2)

#多對多
def find_bmi(height, weight):
    bmi = weight / (height/100)**2
    if bmi > 30:
        bmi_index = 'Obese'
    elif bmi > 25:
        bmi_index = 'Overweight'
    elif bmi > 18.5:
        bmi_index = 'Normal weight'
    else:
        bmi_index = 'Underweight'
    bmi_dict = {
        'bmi_value': bmi,
        'bmi_index': bmi_index
    }
    return bmi_dict

find_bmi(198, 129)

def find_bmi(height,weight):
  bmi=weight/(height/100)**2
  if bmi>30:
    bmi_index='obese'
  elif bmi>25:
    bmi_index='overweight'
  elif bmi>18.5:
    bmi_index="normal weight"
  else:
    bmi_index='underweight'
  return bmi,bmi_index #output as a tuple

find_bmi(198,129)

zion_bmi,zion_bmi_index=find_bmi(198,129)
print(zion_bmi)
print(zion_bmi_index)

def get_circle_meterics(r,return_area=True):
  pi=3.14159
  area=pi*r**2
  perimeter=2*pi*r
  if return_area:
   return area
  else:
    return perimeter

get_circle_meterics(3,True)

get_circle_meterics(3,False)

get_circle_meterics(3)

def create_price(*args):
  return args

create_price(25,35,45,60) #彈性參數

def create_price(*args):
  for args in args:
    print("${}".format(args))

create_price(25,35,45,60,100) #彈性參數

def create_price(*args):
  for args in args:
    print("${:3}".format(args)) #靠第三位對齊

create_price(25,35,45,60,100)

#**kwags#代表 keep words 跟values
def print_menu(**kwargs):
  return kwargs

print_menu(black_tea=25,bubble_tea=35,ice_cream=40)

def print_menu(**kwargs):
  for k,v in kwargs.items():#要品項要價格
      print("${:15}:${:3}".format(k,v))

print_menu(black_tea=25,bubble_tea=35,ice_cream=40)

help(open)

f=open("starwars.txt","w")

f.close()

f=open("starwars.txt","w")
f.write("starwars:A new hope\n")
f.close()

f = open("starwars.txt", "a")
f.write("Starwars: The Empire Strikes Back\n")
f.write("Starwars: Return of the Jedi\n")
f.close()

f=open("starwars.txt","r")
f.read()
f.close()

f=open("starwars.txt","r")
for i in f:
  print(i)

medium_prices={
    'black tea':20,
    'green tea':20,
    'oolong tea':25,
}
for v in medium_prices.values(): #平移
  print(v+10)

def add_milk(x):
  return x+10

for v in medium_prices.values(): #平移
  print(add_milk(v))

list(map(add_milk,medium_prices.values()))

list(map(lambda x: x+10,medium_prices.values())) #lambda用過即丟掉，搭配map,filter

list(map(lambda x : x*9/5+35,[35,34,32]))

#應對大量資料，需效能取捨/跟上面答案一樣
for t in [35,34,32]:
  print(t*9/5+32)



