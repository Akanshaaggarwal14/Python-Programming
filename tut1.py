#QUES 1
print('''Twinkle Twinkle little star,
     How I wonder what you are!
Up above the world so high,
     Like a diamond in the sky.
twinkle twinkle little star,
     How I wonder what you are.''')

#QUES 2
name = input("Enter your first name: ")
surname = input("Enter your last name: ")
print("your name in reverse order: ", surname, "", name)

#QUES 3
r = int(input("enter radius of the circle = "))
import math 
print("Area of circle for given radius = ", math.pi*(r**2))

#QUES 4
color_list=["Red", "Green", "White", "Black"]
size = len(color_list)
print("first element of list = ", color_list[0])
print("last element of list = ", color_list[size-1])

#QUES 5
n = int(input("Enter any integer = "))
value = n + n**2 + n**3
print("value after computing n + nn + nnn = ", value)

#QUES 6
num = input("Enter numbers")
l = num.split(",")
print(list(l))
print(tuple(l))

#QUES 7
C = int(input("enter temperature in degree celcius = "))
F = ((C*9)/5)+32
print("temperature in degree fahrenite = ", F)

#QUES 8
num1 = int(input("Enter first number = "))
num2 = int(input("Enter second number = "))
num1, num2 = num2, num1
print("first number = ", num1)
print("second number = ", num2)
num1+=1
print("new first number after incremental addition = ", num1)

#QUES 9
num = int(input("Enter a number = "))
if(num%2==0):
     print(num, "is EVEN")
else:
     print(num, "is ODD")

#QUES 10
year = int(input("Enter any year = "))
if(year%400==0):
     print(year, "is a LEAP YEAR")
elif(year%4==0 and year%100!=0):
     print(year, "is a LEAP YEAR")
else:
     print(year, "is NOT a LEAP YEAR")

#QUES 11
x1 = int(input("Enter x1 coordinate = "))
y1 = int(input("Enter y1 coordinate = "))
x2 = int(input("Enter x2 coordinate = "))
y2 = int(input("Enter y2 coordinate = "))

dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("Euclidean distance between given coordinates = ", dist)

#QUES 12
a = int(input("Enter angle 1 = "))
b = int(input("Enter angle 2 = "))
c = int(input("Enter angle 3 = "))

sum = a+b+c
if(sum==180):
     print("Triangle can be formed")
else:
     print("Triangle cannot be formed")

#QUES 13
p = int(input("Enter principle amount = "))
r = int(input("Enter rate of interest = "))
n = int(input("Enter no. of times interest is compounded per year = "))
t = int(input("Enter no. of years = "))

amount = p*((1+(r/(100*n)))**(n*t))
print("total amount = ", amount)

#QUES 14
count = 0
x= int(input("Enter a number = "))
if(x<=1):
     print(x, "is neither composite nor prime")
else:
    for i in range(2, x//2+1):
        if(x%i == 0):
            count+=1
        i+=1
    if(count==0):
        print(x, "is prime")
    else:
        print(x, "is not prime")

#QUES 15
n= int(input("Enter a number = "))
sum = 0
for i in range (1, n+1):
    sum = sum + (i**2)
    i+=1
print("1^2 + 2^2 + 3^2 + .... N^2 = ", sum)