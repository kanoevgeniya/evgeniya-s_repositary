# 1) Создать переменную типа String
myString = 'This is my first Python Homework'
# 2) Создать переменную типа Integer
myInteger = 4
# 3) Создать переменную типа Float
myFloat = 5.28972
# 4) Создать переменную типа Bytes

# 5) Создать переменную типа List
myList = ['zero', 'one', 'two',3, 4, 'five']
# 6) Создать переменную типа Tuple
myTulip = ('odin', 'dva', 'tri', 4, 5, 'shest')
# 7) Создать переменную типа Set
myListForSet =set (myTulip)
# 8. Создать переменную типа Frozen set
# 9) Создать переменную типа Dict
myDict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
#
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print ( myString, type(myString), '\n',
        myInteger, type(myInteger), '\n',
        myFloat, type(myFloat), '\n',
        myList, type(myList), '\n',
        myTulip, type(myTulip),'\n',
        myListForSet , type(myListForSet), '\n',
        myDict , type (myDict))

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
firstString = 'this is the first string'
secondString = 'this is the second string'
c = firstString + ' ' + secondString
print (c)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print (myString , myInteger)
# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print (myString + str( myInteger))