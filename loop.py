# While runs untill the conditon is true

i=1
while(i<=5):
    print(i)
    i+=1


# j=5
# for j in range(5,10,2):
#     print(j)

a=tuple(range(1,20,1))
print(a)



# Nested loop

for i in range(1,3):
    for j in range(4,6):
        print(f"{i} {j}")


# Break statement

for i in range(1,10,1):
    if i==5:
        break

    print(i)


# Continue statement
for i in range(1,10,1):
    if i==5:
        continue
    print(i)