x=[x for x in range(5) for y in range(5)]
print(x)

from random import randint
randint(1,20)
rand_ints=[]
for x in range(20):
    random_num=randint(1,100)
    rand_ints.append(random_num)

rand_ints=[randint(1,100) for x in range(20) ]

dict1={'a':5,'b':10,'c':15}
triple={k:v**3 for (k,v) in dict1.items()}
print(triple)