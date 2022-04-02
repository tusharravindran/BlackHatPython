days__month = {'jan':31,'feb':28,'mar':30,'april':31} #key value
print(days__month)

for month,day in days__month.items():
    print(f'{month} month has {day} days')

print(days__month['jan'])

# mutable 
days__month['jan'] = 100
print(days__month) # jan changes

del days__month['april']
days__month.pop('mar')
print(days__month)

 
print(days__month.get('mar',"no mar in this dict"))  #get the value or print what i give
days__month.get('jan')
print(days__month.get('jan')) #get value


# key and value
for month in days__month.keys():
    print(month,end="\t\n")

for day in days__month.values():
    print(day,end="\t ")


days__month['october']=30
print("\n",days__month)


a={'re':1,'se':5}

b ={'se':5,'re':1}

print(a==b)
