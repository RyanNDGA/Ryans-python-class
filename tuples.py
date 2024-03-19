#tuples
fruits = ('apple', 'banana', 'mangoes')
print(fruits)
print(fruits[1])


myfruitslist=list(fruits)
print(myfruitslist)
myfruitslist[2]="pinapples"
print(myfruitslist)
fruits=tuple(myfruitslist)
print(fruits)