r = lambda q: q*2
s = lambda q: q*3
x=2
x=r(x)
print(x)
x=s(x)
print(x)

######################################

a = 4.5
b=2
print(a//b) 
print(a/b)

2+9*((3*12)-8)/10

################################
# variable is defined outside te function

x = 3.33333
'%-6.2f | %05.2f | %+0.6.1f' % (x,x,x)

count =1
def dothis():
    global count    
    for i in (1,2,3):
        print(count)
        count += 1
        
dothis()
print(count)

w='hello'
v=['a','e','i','o','u']
[x for x in w if x in v]

##############################

# passing the parametere through self parmeter
class Acc:
    def __init__(self,id):
        self.id = id
        id = 555
    
acc = Acc(111)
print(acc.id)




for i in range(2):
    print(i)

for i in range(4,6):
    print(i)

########################################

values = [1,2,3,4]
number = set(values)

def cheksum(num):
    if num in number:
        return True
    else:
        return False

for i in filter(cheksum,values):
    print(i)

###########################################


counter = {}
def addCounter(country):
    if country in counter:
        counter[country] += 1
    else:
        counter[country] = 1
        
addCounter('china')
addCounter('japan')
print(len(counter))


##################################

class Geeks:
    def __init__(self,id):
        self.id = id       
manager = Geeks(100)

# member variable name 
manager.__dict__['life'] = 49
#total no of items to dictionary of is 2, variable
#life and id
print(manager.life + len(manager.__dict__))

###################################

dictionary = {}
dictionary[1] =1
dictionary['1'] = 2
dictionary[1] += 1

sum_ = 0
print(dictionary)
for k in dictionary:
    sum_ += dictionary[k]
    print(sum_)
    
print(sum_)

#################################

dictionary = {1:'1',2:'2',3:'3'}

del dictionary[1]
dictionary[1] ='10'
del dictionary[2]
print(dictionary)
print(len(dictionary))

##################################


#same as append
def addlist(listcontiner):
    listcontiner += [10]
    print(listcontiner)
    
mylist = [10,20,30,40]

addlist(mylist)

#####################

class A(object):
    val=1
    
class B(A):
    pass

class C(A):
    pass

print(A.val,B.val,C.val)
B.val=2
print(A.val,B.val,C.val)
A.val =3
print(A.val,B.val,C.val)

#########################

check1 = ['learn','quiz','practice','contribute']

check2 = check1  #deep copy
check3 = check1[:] # shallow copy

check2[0] = 'code'
check3[1] = 'mcq'

count= 0
for c in (check1,check2,check3):
    print(c)
    print(count)
    if c[0] == 'code':
        count += 1
    if c[1] == 'mcq':
        count += 10       
print(count)
    
#############################

def gfg(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

gfg(2)
gfg(3,[3,2,1])
gfg(3) # uses the orignial list stored in orignial



#memory block
###########################

list1 = range(100,105)
print(list1)

#############################

list1 = [1,2,3,4,5,6]
list2 = list1.copy()
del list2[1]
print(list1)
print(list2)

##########################
def check(x):
    print(x)
    
    
    
lis1 = [1,2,3,4,5,6,7]
a = map(check,lis1)

print(list(a))
next(a)
##############################

dictionary = {'GFG': 'geeksforgeeks',
              'google': 'google_check',
              'facebook': 'facebook_check'}

del dictionary['google']
for key,value in dictionary.items():
    print(key)

dictionary.clear()

for key,value in dictionary.items():
    print(key)


del dictionary

for key,value in dictionary.items():
    print(key)


################################
    
dict_1 = {'Google':1,
          'Facebook': 2,
          'Microsoft' : 3}

dict_2 = {'GFG': 1,
          'Microsoft': 2,
          'Youtube': 3}

dict_1.update(dict_2)

for key,value in dict_1.items():
    print(key,value)
    
#############################
    
data = [[2,3,9]]

tem = [[x for x in [data]] for x in range(3)]    

###################################
l1 = list()

l1.append([1,[2,3],4])
l1.extend([7,8,9])
print(l1)
print(l1[0][1][1] + l1[2])


#########################

L1 = [1,1.33,'GFG', 0,'NO']
val1, val2 = 0,''

for x in L1:
    if(type(x) == int or type(x) == float):
        val1 += x
        print(val1)
    elif (type(x) == str):
        val2 += x
        print(val2)
    else:
        break
print(val1,val2)        
        
###########################

import sys
L1 = tuple()
print(sys.getsizeof(L1)) 

#################################
#tuple are group of two or more value


t1 = (1)
print(type(t1))
t2 = (2,3)
t1 += 5
print(t1)
print(t1+t2)

###################################

list1= [True,50,10]
list1.insert(2,5) #insert 5 at index 2
print(list1)

##################################3

T = (1,2,3,4,5,6,7,8)
print(T.index(2)) # give the index value of the element
#####################################

L = [1,2,3,4,5,6]
print(L.pop(0)) # delete and return th index value
print(L.remove(L[0])) # no return value
print(L)

#########################################

from math import sqrt

L1 = [x**2 for x in range(10)].pop() # pop last element
print(L1)
L1 += 19
print(L1)
print(sqrt(L1))
L1 = [x**2 for x in reversed(range(10))].pop()
print(L1)
L1 += 16
print(int(sqrt(L1)))

#######################################33

D = dict()
# enumerate ass index value  or add counter to iterable
for x in enumerate(range(2)):
    print(x[1])
    D[x[0]] = x[1]
    D[x[1]+7] = x[0]
    
#enumerate return tuples

###########################

d= dict()
for i in range(3):
    for j in range(2):
        d[i] = j
print(d)

#the value of d key is overwrited in j loop
###############################################

D= {1: [1,2,3], 2: (4,6,8)}
D[1].append(4)
print(D)
L1 = list(D[2]) # it will convert tuplt into list
print(L1)


###########################################


from random import randrange

L =list()

for x in range(5):
    L.append(randrange(0,100,2)-10))
    
print(L)
    
#######################################


from math import *
a = 2.13
b = 3.7777
c = -3.12
print(int(a), floor(b), ceil(c), fabs(c))     

#########################################

import re
print(re.sub('ge','***', 'Geekforgeeks',flags= re.IGNORECASE))
print(re.sub('ge','**','Geeksforgeeks'))

############################################

x= ['ab','cd']
for i in x:
    print(i.upper())
    x.append(i)
    
############################################
    
for i in 123:
    print(i)
    
###################################333333333333
    
numbergames= {}
numbergames[(1,2,3)] =8
numbergames[(4,2,1)] = 10
numbergames[(1,2)] = 12
print(numbergames)

sum =0
for k in numbergames:
    print(k)
    sum += numbergames[k]
    print(sum)
    
print(len(numbergames))
    
################################################

tu = (1,2)
li = [1,2]
tustr = ('aaaaaa')
listr = ['sdfres']
print('tuple', tu*2) #tuple (1, 2, 1, 2)
print('list', li*2)    #list [1, 2, 1, 2]
print(tustr*2) # aaaaaaaaaaaa
print(listr*2) #['sdfres', 'sdfres']

#######################################33

# not a valid satement
d1 = {'A':1,'B':2}
d2 = {'A':1 , 'B':3}
print(d1 > d2)

######################################

t1 = (5,2,3,4,5)
t2= (2,3,4,5,6)
print(t1>t2)

######################################33
 

#Integer is not a valid input
 #'int' object is not iterable
l = list('12345')
print(l)
#########################3

T = tuple('geeks')
print(T)

a,b,c,d,e = T # unpacking tuples values in variable

T = (a,b,c,d,e)
print(T)

##################################3

l1= 'abc'
l2 = 'nnn'
print(l1+l2)

#################3

print(False + True)
print(int(True))

##################################

t1 = tuple('abcd')
for i in t1:
    print(int(i))
    
###################################

str1 = '{1} hello, how r u {0} khana'.format('aditya','rajmana')    

print(str1)

############################

a = 2
b = '3.77'
c=-8
str1 = '{0:.4f} {0:3d} {2} {1}'.format(a,b,c)
print(str1)

################################
#find() returns the index of substring if found in

lines= 'Aditya hello how r u'
print(find(lines,'Aditya'))

##################################3
lines= 'what a cool weather today is'
L = lines.split('a')
print(L)
for i in L:
    print(i)

#######################################

sets = {1,2,3,5,6}
print(type(sets))

#################################

my_string = 'asdfasdfas'
print(len(my_string))


######### Decorators ####################
 
def messagewithwelcome(fun): #it takes function as parameter
    
    #Nested funcion
    def addwelcome(site_name):
        return "Welcome to" + fun(site_name)
    
    return addwelcome

@messagewithwelcome
def site(site_name):
    return site_name

print(site('aditya'))

################################

def attach_data(function):
    function.data = 3
    return function

@attach_data
def add(x,y):
    return x+y
    
    
print(add(2,3))    
print(add.data)


#######################33

import numpy as np

x_train =np.random.random((100,8,16))
print(x_train)
y_train = np.random.random((100,16))
print(y_train)

############################

leng=3
data=[[i+j for j in range(leng)] for i in range(100)]
print(data)

train = [[i+j-1 for j in range(leng)] for i in range(1,101)]
print(train)
    


ded outerfunction(text):
    text = text
    
    def innnerfunction():
        print(text)
        
    return innerFunction

if __name__ = '__main__':
    mufunction = outerFunction('Hey!')
    myfuncrion
    
x= [[0],[1]]
print((''.join(list(map(str,x))),))




l= [2,3,[4,5]]
l2 = l1.copy()
l2[0]=88

print(l,l2)


def test(i,j):
    if(i==0):
        return j
    else:
        return test(i-1,i+j)
    
print(test(4,7))


    
    
    
    
    
    
string ='my name is x'
for i in string:
    print(i,end=',')
    
def change(a):
    print(a,"1111")
    
def change(a):
    print(a,'222222')
    
change(1)



a = 0 % 3 == 0
a   
    
    
    
    
    




































































































