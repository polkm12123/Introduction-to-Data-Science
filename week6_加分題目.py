# -*- coding: utf-8 -*-
"""week6 加分題目

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BO6nuU12la_PyuRkveWnIsnYpMx747a6
"""

(1)若x = "Python", y = "Python"，則(x is y) 和 (x==y)的結果是True還是False?

(2)若x = "Python", y = x，則(x is y) 和 (x==y)的結果是True還是False?

x = "Python"
y = "Python"

print(x is y)

print(x==y)

x = "Python"
y=x

print(x is y)

print(x==y)

#(3) 二者答案為什麼一樣或不一樣？
因x值得字串與y值的字串是一樣的。is:是否為相同的值