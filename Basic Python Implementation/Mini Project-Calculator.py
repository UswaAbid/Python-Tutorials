
first = input("Enter first number: ")
operator = input("Enter opertor (+,-,*,/,%): ")
second = input("Enter second number: ")

first = int(first)
second = int(second)         #Converting string into integer

if operator == "+":
   print(first + second)
elif operator == "-":
   print(first - second)
elif operator == "*":
   print(first * second)
elif operator == "/":
   print(first / second)
elif operator == "%":
   print(first % second)
else:
   print("INVALID OPERATION!")
