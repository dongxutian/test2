#########################################################
#secret number game
#-----------------------------
#The program generates a random number between 1-100
#
#We want the user to guess a number between 1-100
#If the user guessed bigger than the secret number, the program will return '>'
#IF the user guessed less than the secret number, the program will return '<'
#If the user guessed the secret number, then the program will print the secret number
#
#########################################################

# import random
# secret_number=random.randint(1,100) #stores secret number from 1-100
#
# while True:
#     user_input=int(input('Please enter a number between 1 and 100: '))
#     if user_input>secret_number:
#         print('>')
#     if user_input<secret_number:
#         print('<')
#     if user_input==secret_number:
#         print("Congrats, you win!")
#         break

'''
Extremely important
They're abstract
They're in every modern programming language
helps you process and organize the data in your programs
List: Mutuable type
Tuple: Immutuable type
Set: Unique elements
Dictionary: key/value mapping

'''

x=['1.1.1.1','2.2.2.2','3.3.3.3','4.4.4.4','5.5.5.5']
y=x[::2]
z=0
while z<3:
    print(y[z])
    z+=1
    print()


x=[1,3,5,2,10]
for item in x:
    print(item)
y=0
while y<len(x):
    print(x[y])
    y+=1


for index,item in enumerate(x):
    print(F"index and item are: {index} and '{item}")

nested=['a','b',100,[1,2,3],100]

matrix=[
    [1,2,3],
    [1,2,4],
    [2,3,4]
]
print(matrix[0][0])
for row in matrix:
    for col in row:
        print(col)

