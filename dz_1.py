num1 = input("first number: ")
operation = input("mathematical operation (+, -, /, *, //, %): ")
num2 = input("second number: ")

if not num1.isdigit() or not num2.isdigit():
	print("number invalid")
else:
	num1 = int(num1)
	num2 = int(num2)

	if operation == '+':
		print(num1 + num2)
	elif operation == '-':
		print(num1 - num2)
	elif operation == '*':
		print(num1 * num2)
	elif operation == "%" or operation == "/" or operation == "//":
		if num2 != 0:
			if operation == "%":
				print(num1 % num2)
			if operation == "/":
				print(num1 % num2)
			if operation == "//":
				print(num1 % num2)
		else:
			print("cant divide by 0")

if operation.isdigit():
	print("a mathematical operation can't be a number")
elif operation not in ["%", "//", "/", "+", "-", "*"]:
	print("the mathematical operation you've entered is invalid")
