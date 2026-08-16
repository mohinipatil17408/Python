First = int(input("Enter first no:"))
operators = (input ("enter operators "))
Second = int(input("enter second no:"))

if operators == "+":
    print(First+Second)
elif operators == "-":
    print(First-Second)
elif operators == "*":
    print(First*Second)
elif operators == "/":
    print(First/Second)
elif operators == "%":
    print(First%Second)
else:
    print('invalid syntax')
