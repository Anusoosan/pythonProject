import math

##### Question No.1 ####
print(list(range(1,11)))

##### Question No.2 ####
print(list(range(1,100,2)))

##### Question No.3 ####
print("Multiplication table of 7")
for i in range(1, 11):
   print(7, "X", i, "=", 7 * i)

##### Question No.4 ####
for i in range(1, 11):
   print("Multiplication table of", i)
   for x in range(1,11):
      print(x, "X", i, "=", x*i)

##### Question No.5 ####
print ("Sum of numbers from 1 to 10 is:", sum(range(1,11)))


##### Question No.6 ####
def fact(n):
   return (math.factorial(n))

print("Factorial of", 10, "is", fact(10))

##### Question No.7 ####
print ("Sum of odd numbers from 10 to 30 is:", sum(range(11,30,2)))

##### Question No.8 Create a function that will convert from Celsius to Fahrenheit####
"""celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))

##### Question No.9 Create a function that will convert from Fahrenheit to Celsius ####
fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit-32) * 5/9
print('%.2f fahrenheit is: %0.2f celsius' %(fahrenheit, celsius))
"""
##### Question No.10 Calculate the sum of numbers in an array of numbers ####
numbers = [10,20,30,40,50]
print("Sum of the given list of numbers = ", sum(numbers))

##### Question No.11 Calculate the average of the numbers in an array of numbers####
length = len(numbers)

print("Average of the given list of numbers = ", sum(numbers)/length)

##### Question No.12 ####


##### Question No.13 Find the maximum number in an array of numbers ####

maximum_num = max(numbers)
print("Maximum number from the list = ", maximum_num)

##### Question No.14 ####



##### Question No.15 ####



##### Question No.16 Create a function that will return a Boolean specifying if a number is prime ####
"""def isPrime(num):
   if num>1:
      for i in range(2,num):
         if(num%i) == 0:
            return False
         return True
      return False
print("The given number is Prime: " , isPrime(int(input("Enter a number: "))))
"""

##### Question No.17 Calculate the sum of digits of a positive integer number ####
