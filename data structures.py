"""
mystudents=["said","mercy","kimberly"]
print(mystudents)
mystudents.append("franco") #add item to list
print(mystudents)
mystudents.remove("mercy")   #remove item from list
print(mystudents)
mystudents[2]="franco madinka" #modify list
print(mystudents)
"""

#empty list
students=[]
while len(students)<3:
  name_input= input("enter your students name:")
  students.append(name_input)

print(students)