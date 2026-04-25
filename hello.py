print("hello, world")
name=input('What is your name? ').strip().title()
# This is a comment and it won't be executed
age=input('How old are you? ')
# print('Hello,' , name ,',' , age , '!',sep='???')
# print('Hello,' + name + ',' + age + '!', sep='???')

#str remove the whitespace from string and Capatalize user's name
# name=name.strip().title()

#Split users name into first name and last name
first, last = name.split(" ")
print(f'Hello,{name}, {age}!')
