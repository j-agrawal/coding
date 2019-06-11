import datetime
name = input("enter your name:")
print("your name is:"+name)
age = int(input("enter your age:"))
print("your age is:%d"%age)
x = datetime.datetime.now()
curyear=x.year
y=95-age
resultantyear= curyear + y
print("the year in which the user's age will be 95 is:%d" %resultantyear)

