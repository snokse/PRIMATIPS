
import math as m
from random import randint
import random as rand
course = "String operators & functions"

print(f"""****************************
     *** {course} ****
      ************************************""")
print(course[2],course[6])

print(course[0:3],course[4:])

print(len(course))
print(type(course))
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("pro"))
print(course.count("o"))
print(course.replace("p","P"))
print(course.replace("p","P"))

s1 = "Learn all about"
s2 = "pyton strings"
print(s2.title())
s2 = s2.title()
s3 = s1+ " " +s2
print(s3)
print(len(s3))
print(s3.find("Pyton"))
print(s3.replace("strings",""))
print(s3)

name = "Ahmed"
age = 30
message = "Hello "+ name + " you are " +str(age)+ " years old"
message1 = f"Hello {name} you are {age+5} years old"

print(message)
print(message1)

message1 += message
print(message1)

# Numeric functions
num12 = m.sqrt(9)
print(f"{num12:.2f}")

print(f"{m.pi:.2f}")

print(randint(0,49))

print(max(1,3,4))
print(min(1,3,4))
print(m.pow(3,3))

print(rand.random())
print(ord("a"))


arr = [1,2,3]
arr.append("Ahmed")
print(arr)

names = []
 nbr = 0

if nbr<5 :
      names.append()

