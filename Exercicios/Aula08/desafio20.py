import random
#from random import choice

a1 = str(input("Input the student name: "))
a2 = str(input("Input the student name: "))
a3 = str(input("Input the student name: "))
a4 = str(input("Input the student name: "))

l = [a1, a2, a3, a4]
random.shuffle(l)

print("Following sequence of student press: {}".format(l))

