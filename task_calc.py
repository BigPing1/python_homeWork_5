import calculator

print("Alailable options:\tadd(+)\tsubtract(-)\t multiply(*)\t divide(/)\n")

first_number = int(input("please, enter first numbert\t"))
second_number = int(input("please, enter second number\t"))
operations = input("please, enter operations\t")
operations = operations.lower()

if operations == "add" or operations == "+":
    calculator.add(first_number, second_number)

elif operations == "subtract" or operations == "-":
    calculator.subtract(first_number, second_number)

elif operations == "multiply" or operations == "*":
    calculator.multiply(first_number, second_number)

elif operations == "divide" or operations == "/":
    calculator.divide(first_number, second_number)

else:
    print("Not correect operation")