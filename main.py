import utilites

user_list = utilites.enter_numbers()

if len(user_list) > 0:
    user_operation = int(input("Enter 1(middle number calc)\tEnter 2(Max number calc)\n"))

    if user_operation == 1:
        utilites.middle_numbers(user_list)
    elif user_operation == 2:
        utilites.max_number(user_list)
    else:
        print("Wrong operation number")
