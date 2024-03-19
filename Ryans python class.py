"""
#variables
students_name ="ryan"
students_name ="ben"
students_age ="20"
students_mark ="100"
print(students_name)

STUDENT_NAME ="mukaga"
students_name ="wasika"
print(STUDENT_NAME)
a= int(1)




#casting in python

price=10
qty=5
total=price*qty
print("the total is: "+str(total)+" kenya shillings")


price=20
qty=3
total=price*qty
myanswer1="the total is: "+str(total)+"kenya shillings"
myanswer2="the total is: " ,total, "kenya shillings"

print(myanswer1)

firstname="jonathan"
secondname="1234567"
thirdname=firstname+"            "+secondname
print(thirdname)



x=5
x+=5  #x=x+5
x-=4  #x=x-4
x*=3  #
x/=2
#logical operators
a

pens=60.0
books="50"
total=pens+int(books)
print("my total is" ,total)


pens=60.0
books="50"
total=pens+int(books)
result="my total is: "+str(total)+" kenya shillings"
print(result)

x=10
if x>3:
 print("x is greater than 3")
elif x==3:
    print("x is less than 3")
else:
    print("x is equal to 3")


country=input("Enter the country:")
if country=="rwanda":
    print("east africa")
elif country=="kenya":
    print("east africa")
elif country=="ugamda":
    print("east africa")
elif country=="congo":
    print("east africa")
else:
    print("invalid country")

    

x=1
while x<=10:
    print("the number is:",x)
    x+=1
    if(x == 3):
        x+=1
        continue
    if(x == 5):
        x+=1
        continue
print("loop end")

"""

"""
def add_odd_numbers(limit):
    total = 0
    for num in range(1, limit + 1, 2):  # Start from 1, increment by 2 (odd numbers)
        total += num
    return total

limit = 10
result = add_odd_numbers(limit)
print("Sum of odd numbers up to", limit, "is:", result)



def sum_of_odd_numbers(limit):
    total = 0
    num = 1
    while num <= limit:
        total += num
        num += 2  # Increment by 2 to move to the next odd number
    return total

limit = int(input("Enter the limit of numbers:"))
result = sum_of_odd_numbers(limit)
print("Sum of odd numbers from 1 to", limit, "is:", result)
"""


"""
x=1
sum=0
while x < 10:
   if x%2!=0:
     print("the number is:",x)
     sum+=x
   x+=1
   print(sum)




#looping
x=1
while x<=10:
    print("the number is:",x)
    x+=1

#continue
x=1
while x<=10:
    print("the number is:",x)
    x+=1
    if(x == 3):
        x+=1
        continue
    if(x == 5):
        x+=1
        continue
print("loop end")

#break
x=1
while x<=10:
    print("the number is:",x)
    x+=1
    if(x == 3):
        x+=1
        continue
    if(x == 5):
        x+=1
        continue
print("loop end")



#while and else
y=2
while y<=6:
    print("the number is:",y)
    y+=1
else:
    print("loop end")



ugandan=0
kenyan=0
counter=1
visitors=int(input("enter your visitors number"))
while counter<=visitors:
    nationality=input("enter your nationality")
    if nationality=="kenyan":
        kenyan+=1
        print("allowed")
        counter+=1
    else:
        ugandan+=1
        print("not allowed")
        counter+=1
print("the number of visitors is",visitors)
print("the number of",kenyan)
print("the number is ",ugandan)


"""
#for loop
cars=("audi","bmw","subaru","mazda","suzuki")
for car in cars:
    print(car)

#while loop implementation
cars=("audi","bmw","subaru","mazda","suzuki")
x=0
while x<len(cars):
    print(cars[x])
    x+=1

for x in range(6):
    print("sai")

for x in range(2,4):
        print("said")

for x in range(2,4,2):
    print("mercy")




sum=0
for x in range(10):
   if x%2==0:

     sum+=x
print(sum)
