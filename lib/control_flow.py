#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    pass

def hows_the_weather(temp):
    if (temp < 40):
        print(f"It's brisk out there!")
    elif (temp >= 85):
        print(f"It's too dang hot out there!")
    elif (temp>=40):
        print(f"It's a little chilly out there")
    else:
        print("It's perfect out there!")

def fizzbuzz(number):
     if number % 3 == 0 and number % 5 ==0 :
         print('FizzBuzz')
     elif number % 3 == 0:
         print('Fizz')
     elif number % 5 == 0:
         print('Buzz')
     else :
         print(number)
def calculator(oper, num1, num2):
    if oper == "+":
        return num1 + num2
    elif oper == "-":
        return num1 - num2
    elif oper == "*":
        return num1 * num2
    elif oper == "/":
        if num2 != 0:
            return num1/num2
        else:
            print(f"Cannot divide by zero!")
            return None
    else :
        print(f"Invalid operation!")
        return None
