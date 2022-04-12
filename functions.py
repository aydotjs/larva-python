# def saySomethin():
#     print("Say something")

# def anything():
#     print("Anything")
#     print("Anything again")
#     print("Anything another time")
#     saySomethin()

# anything()

# def learningParameters(mango):
#     fruits = mango 
#     print(fruits)
# learningParameters("I love mangoooooooo")

# def mypow(a,b, myString):
#     c = a**b
#     print(c)
#     print(myString)

# mypow(3, 3, " is the result of the power function")

# print(isinstance(5.0, float))

# def checkArgs(a,b,c):
#     if isinstance(a, float) and isinstance (b, float) and isinstance(c, float):
#       print(c)
#       print(a)
#       print(b)
#       sum = a + b + c
#       print(sum)
# checkArgs(4.1,6.2)


# x = ["TAyo", "Ayo"]
# print(x[0])

#Return statement and variable scope 

# a = 6

# def myadd():
#   x = 4
#   y = 5
#   z = x + y
#   a = "Something"
#   print(z)
#   return a

# d = myadd()
# print(d)



#global scope
#block scope

# def addingNumbers (a, b):
#   sumValue = a + b
#   return sumValue

# valueOfFunc =  addingNumbers(9,7)
# print(valueOfFunc)

# def r():
#   a = 5
#   b = 7
#   c = a + b
#   d = "Something"
#   return a, b,d
#   return b 

# print(r())

#=============================================
#giving functions arbitrary no. of arguments
#=============================================

def addAllNumbers(*T):
    sum = 0
    for i in range(len(T)):
        sum = sum + T[i]
    return sum


# d = {
#     "name" : "Ayo",
#     "surname" : "jjb",
#     "nickname" : "Ayo"
#     }
    


# def printAllVariablesAndValues(**kkk):
#     for x in kkk:
#         print("The key is ", x, " and the value is ", kkk[x])

# printAllVariablesAndValues(name = "Ayo", complexion = "light")
def checkIfNotNumeric(*args):
    for x in args:
        if not(isinstance(x,(int,float))):
            return False
    return True
print(checkIfNotNumeric(5,"hh",9))