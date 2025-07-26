print("CALCULATOR")
num1=int(input("enter the number"))
num2=int(input("enter the numbrer"))
op = input("Enter operator (+, -, *, /): ")
if op == '+':
    Result=num1 + num2
elif op == '-':
    Result= num1 - num2
elif op == '*':
    Result=num1 * num2
elif op == '**':
    Result=num1 ** num2
elif op == '/':
    if num2 != 0:
        Result= num1 / num2
    else:
        print("Error: Cannot divide by zer0")
else:
    print("Invalid operator")
print("Result:",Result)

