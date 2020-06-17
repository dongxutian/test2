########################
#This program will read in
#user input by using the
#input()function in python
#We can store the user input in a variable and manipulate
#it.
#
#######################
#the addition functionality of our calc

# x1=float(input("Enter in a number to add   "))
# print("The number entered is ", x1)
#
# y1 = float(input("Enter in another number to add   "))
# print("The number entered is ", y1)
#
# print (x1,'+',y1, '=', x1+y1) ##sum numbers x and y

#The subtraction functionality of our calc
# x2=float(input("Enter in a number to subtract   "))
#
# y2=float(input("Enter in the second number"))
#
# print(x2,'-', y2, '=', x2-y2)

# the multiplication functionality of our calc

# x3 = float(input("Enter in a number to multiply   "))
# y3=float(input("Enter in another number to multiply  "))
# print(x3, '*', y3, '=', x3*y3)

#the division functionality of our calc

# x4=float(input("Enter a number to divide    "))
# y4=float(input("Enter another number to divide  "))
# print(x4,'/',y4,'=',x4/y4)

#implement the power functionality using **

# x5=float(input("Enter in a number to power  "))
# y5=float(input("Enter another number to power: "))
# print (x5, '**', y5,'=', x5**y5)

#implement the mod functionality %

#implement the math module, and implement ANY one functionality

#create a Github account

x,y=5,7
if x<y:
    print('ok!')
else:
    print('not ok!')

grade =40
if grade >=90:
    print('A')
elif grade >=80:
    print('B')
elif grade >=70:
    print('C')
else:
    print(':(')

temp=50
if temp>90:
    print('hot!')
    if temp <60:
        print(temp)
        if temp==50:
            print(temp)


lucky_number=15
if lucky_number>15:
    print('>')
elif lucky_number <15:
    print('<')
else:
    print('=')

'''
nesting
-----
when multiple if statements are included inside each other
'''

print("testing nesting in python")
x,y,z=1,2,3
if x==1:
    print(x)
    if y==2:
        print(x+y)
        if z==3:
            print(z)

print("modification for nesting")
if x==1:
    print(x)
    if x==1 and y!=2:
        print(y)
    else:
        print(x)
else:
    print("hello!")


a,b,c=5,10,15
if a==5:
    print(a)
    if a>=5:
        print(a)
    elif b<=10:
        print(b)
    else:
        print(c)


'''
iteration in python
-------------
doing repetivitve tasks
'''

print("test iteration in python")
for x in range(10):
    print(x)

ord('a')

for x in range(1,11,2):
    print(x, end='  ')

