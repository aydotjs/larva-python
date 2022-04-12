# while loop
"""
x = 0
while x <= 10:
    print("Value of X is: ", x)
    x = x + 1
"""
# l = []
# num = 0

# while num <= 10:
#     l.append(num)
#     num = num + 1
# print(l)

# n = int(input("Max Iterations: "))
# i = 1
# while i < n:
#     if i % 2 == 0:
#         print(i)
#     else: 
#         pass
#     i = i + 1

"""
n = 10
i = 1
while  i <= n :
     if i % 9 == 0:
         print("Inside if block")
     else:
        i = i + 1
        print("Inside else block")
print("done")

"""
# i = 1
# while True:
#     if i % 17 == 0:
#         print("Break")
#         break
#     else: 
#         i += 1
#         continue
# n = 10
# i = 1
# while True:
#     if i%9 != 0:
#         print("The continue statement keeps taking us back " + str(i) + " times backward")
#         i += 1 
#         continue   
#     print("Something")
#     print("Something else")
    
# print("done")

#For Loops
# l = []
# for i in range(11):
#     l.append(i)
#     print(l)





# a = range(10)
# print(a)
# # range(0, 10, 1)



"""
IMPORTANT
l = []
for x in range(10):
    print(x)
    x += 2
    l.append(x ** 2)
print(l)

# """
# mylist = []
# for y in range(10):
#     print(y)
#     mylist.append(y**2)

# print(mylist)

from math import factorial


S = {"Ayo", "Bayo", "Catherine" }
# l = []
# s = ()

# for a in S:
    
#     if a == "Catherine":
#       break
#     print(a)
# else:
#     print("Loop terminates with success")


#Strings,List, Dictionary, Tuples
# start = 1
# end = 100
# print( "Prime numbers between ", start, "and", end, "are:" )
# for num in range(start, end + 1):
#     if num > 0:
#         for i in range(1, num):
#             if(num % i) == 0:
#                 break
#         else:
#             print(num)

# print(list(range(1,2)))

#Calculate the sum of all numbers from 1 to an inputted number
#prompt user to input a number

#range from 1 to input

# n = int(input("Enter number: "))
# sum = 0
# for i in range(1, n + 1):
#     sum = sum + i
# print("\n\n")
# print("Sum is: ", sum)
# cause user input number
#creating a variable called factorial and assign it value =1
#iterate starting from 1 to given number
#multiply factorial by given number and reassign it
#print factorial

# n = int(input("Enter a number: "))
# factorial = 1
# if n < 0:
#     print("Print Factorial does not exist for negative numbers")
# elif n == 0:
#     print("Factorial of Zero  is one ")
# else:
#     for i in range(1, n + 1):
#         factorial = factorial * i
#     print("The factorial of ", n, " is ", factorial)


n = int(input("Enter a number: "))
factorial = 1
if n < 0:
    print("Print Factorial does not exist for negative numbers")
elif n == 0:
    print("Factorial of Zero  is one ")
else:
    i = 1
    while i<=n:
        factorial = factorial * i
        i = i + 1
print("The factorial of ", n, " is ", factorial)

