start=int(input("Enter start: "))
end=int(input("Enter end: "))
steps=int(input("Enter steps: "))
br=int(input("Enter where you want to break:"))
cn=int(input("Enter where you want to skip:"))

for i in range(start,end,steps):
    if i==br:
        break
    elif i==cn:
        continue
    else:
        print(i)