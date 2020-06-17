def f(*args):
    for x in args:
        print(x)

f(5)
f("I am here",9,5)

def summation(*nums):
    count=0
    for x in nums:
        count+=x
    return count

y=summation(10,20)
print(y)

#######We can specify default values in our functions\n by creating keywaord arguments


def nums(**kwargs):
    for x,y in kwargs.items():
        print(x,y)

nums(a=10,b=100)
nums(a=10,b=100,c=17)


def multiply(*args):
    for x in args:
        x*=10
        print(x)

multiply(1,15,100)



def table(multi=5):
    for x in range(1,multi+1):
        for y in range (x,multi+1):
            print (f'{x}*{y}=',x*y)

num=int(input("Please enter your number: "))
table(num)