# pie=3.17
# radius=float(input("Enter your value:"))
# area_of_circle=pie*radius*radius
# print(f"Area of circle: {area_of_circle}")

num1=float(input("Enter number1:"))
num2=float(input("Enter number2:"))

choice=input("Enter your choice + - * / ")
if choice=='+':
    print(f"Addition: {num1+num2}")
elif choice=='-':
    print(f"Subtraction: {num1-num2}")
elif choice=='*':
    print(f"Multiplication: {num1*num2}")
elif choice=='-':
    print(f"Division: {num1/num2}")
else:
    print("Invalid choice")