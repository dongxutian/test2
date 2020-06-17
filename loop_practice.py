"""

Practice Loop problems

------------------
A set of problems that we can work through
to help master iteration in python

"""


'''
I want to sum the numbers from 1-100
using a for loop
'''

sum=0
y=1
for x in range(1,101,y):
    y+=1
    sum+=x
    print('x','=',x, 'y', '=',y)

print(sum)

#nested for loop

# for x in range(3):
#     for y in range(3):
#         print(x,y,end='  ')
#     print()

for x in range(3):
    for y in range(3):
        print('*', end=' ')
    print('')




# for x in range(1, 255):
#     for y in range(1,255):
#         print(f"set family inet address 10.{x}.{y}.1")


i=0
while i<10:
    print(i)
    i+=1

##while loop example
i=0
while True:
    print('i=',i)
    i+=1
    if i ==1500:
        print('exiting....')
        break


i=0
while i<200:
    i+=1
    if i==3:
        continue
    else:
        print(i)


"""
Try /except statement
"""

y = 0
try:
    x = int(input('Enter in a numerrator '))
    y=int(input('Enter in a deno '))
    z = x/y
except ValueError:
    print('Error')
except ZeroDivisionError as zero:
    print(' aviod that')
    print(zero.args)

