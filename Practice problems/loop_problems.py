# Exercise 2 : Use single for loop to access each list

my_list=[[1,2,3],[4,5,6],[7,8,9],[]]

for i in my_list:
    print(i)


# Exercise 3 : Using Nested for loop access each individual element from list with in the list

for i in my_list:
    for j in i:
        print(j)


# Exercise 5: print the fallowing output
'''
1
2 2
3 3 3
4 4 4 4 '''

a=int(input("Enter the number: "))

for i in range(1,a+1):
    for j in range(i):
        print(i,end=" ")
    print(" ")

# Exercise 6: Skip space to print from the sentence ‘Python Logic For Kids’

my_sentence='Python Logic For Kids'
my_sen2=[]
for i in range(len(my_sentence)):
    if my_sentence[i]==' ':
        continue
    else:
        my_sen2.append(my_sentence[i])
print(my_sen2)
# print(my_sentence[:i+1])

# Exercise 7 : Print the * pattern using nested for loops
# *
# * *
# * * * 
# * * * *
# * * * * *
# * * * *
# * * *
# * * 
# *

n=int(input("Enter the number: "))

for i in range(1,n):
    for j in range(i):
        print("*" ,end=" ")
    print(" ")
for i in range(n,0,-1):
    for j in range(i):
        print("*" ,end=" ")
    print(" ")



# Exercise 9 :Print odd number patterns

m=int(input("Enter the number: "))
k=1
for i in range(0,m):
    for j in range(0,k):
        print("*" ,end=" ")
        k+=2
    print(" ")


# Exercise 10 : Print Alphabets
val=65
for i in range(0,5):
    for j in range(0,i+1):
        ch=chr(val)
        print(ch, end=" ")
        val=val+1
    print(" ")