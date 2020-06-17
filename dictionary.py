# letters={'a':'apple','c':'coconut','p':'pineapple'}
# for key,value in letters.items():
#     print(key,'--->', value)
# letters.items()
# letters.keys()
# letters.values()

# jupyter notebook
# spyder
#
# empty={}
# for key, value in letters.items():
#     empty.update({key:value})
# print (empty)
# """


# Create a dictionary called shopping_cart
# The dictionary will contain mapping of items from an online store
# the items will have a name as teh key, and then corresponding quantity and price as value
# The dictionary should have at least 5 items
# -Display all teh keys in the dictionary
# -Display all teh values in the dictionary
# -Iterate over the dictionary and display the key/value pairs
# -Create a new dictionary called 'sale' and only add items from the shopping_caart dictionary that are <=$10
# """

shopping_cart={
    'apple':[5,6],
    'milk':[2,7],
    'beef':[3,23.5],
    'ipad':[1,809],
    'makeup':[3,250]
}

keys=shopping_cart.keys()
quatity=shopping_cart.values()
print(keys)
print(quatity)
print('items','--->','quatity','---->','price')
for_sale={}
for key,value in shopping_cart.items():
    print(key,'--->', value[0],'------>',value[1])
    if value[1]<10:
        for_sale.update({key:value})
print("For sale itmes and prices: ")

for key,value in for_sale.items():
    print('item {}, bought {},price {}' .format(key,value[0],value[1]))

numbers=[]
numbers=[x for x in range(1,21)]

#generate the range of numbers from 1-20
#I want to generate only the even numbers and store these numbers in a list called evens
#Let's first solve this using a for loop, and then let's solve this using a list comprehension

evens=[]
i=1
while i<21:
    if i%2==0:
        evens.append(i)
    i+=1

evens_two=[x for x in range(1,21) if x %2==0]