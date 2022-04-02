#slicing
n = [4,7,71,5,8,89]



print("len of 'n'",len(n))
print(n[0:4])
print(n[1:-1])
print(n[0:len(n)],"    ",  n[:])
print(n[::-1])#revers
print(n[-1:-5:-1])

#modifying list 
a =[1,3,4,5,6]
print(a)
a[0:1] =['one',3,'five']
print(a)
a[::2] = [100,100,100,100]
print(a)

#listortuple = [1,4,0,5,6,7]
listortuple = (1,4,6,7)
def mod_elements(listortuple):
    for i in range(len(listortuple)):
        listortuple[i] *= 2
        print(listortuple)














print ("""""######list amethis #######""")
a10 = [1,4,6,0]
#sorting 
print(a10.sort())

 #searchin list 

num =[1,2,3,4,7,10,2,9,3,2,9,3,2,10]

print(num.index(10,6)) #search 10 from index 6
print(num.index(10,0,9)) #search 10 from index 0 to 9 (only first returnm)
print(7 in num)# ' in '  --> returns boolean result'
print(1000 in num)



#search algorithm
#key = int(input())
key = 3 
if key in num:
    print(f'found {key} at index {num.index(key)}')
else:
    print(f'{key} not found')


#other list attributes 

list1 =['tushar','sydd','ysjg']
list1.insert(0,'tushar1')
print(list1)
list1.append('lasttush') # append or 
#extend allow to pass only one argument so (['1','2',])
list1.extend(['last1','last2'])
print(list1)
