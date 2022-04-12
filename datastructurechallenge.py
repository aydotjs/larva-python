"""
lets say you are teacher and you have different students records containing id of students and the mark
list in different subject. You want to enter all these data in computer and you want to compute the avg
mark and display it
"""
"""
create a function called get user 
function will collect student id
function will collect student marks
create more students variable
check for duplicates
create function that will get avg marks

"""
def getDataFromUSer():
    D = {}
    while True:
        studentId = input("Enter student ID: ")
        markList = input("Enter the marks of each student seperated by a comma: ")
        moreStudentsQuestion = input('Enter "no" to quit insertion of new students: ')
        if studentId in D:
            print(studentId, "is already inserted")
        else:
            D[studentId] = markList.split(",")
        if moreStudentsQuestion == "no":
            return D

studentData = getDataFromUSer()

def getAvg(D):
    avgMarks = {}
    for x in D:
        L = D[x]
        s = 0
        for marks in L:
            s+=int(marks)
        avgMarks[x] = s/len(L)
    return avgMarks
avgM = getAvg(studentData)
for x in avgM:
    print("Student : ", x, "got average mark as : ", avgM[x])
