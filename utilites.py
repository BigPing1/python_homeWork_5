def enter_numbers():
    userStart = int(input("Please press '1' start\t"))
    userList = []

    if userStart == 1:
        count = int(input("How many numbers is your list?\t"))
        container = 0
        while container != count:
            print("Enter numbers")
            userList.append(int(input()))
            container+=1
        print(f"Your list {userList}")
        return userList
    else:
        print("Wrong enter")


def middle_numbers(number):
    container = 0
    for numbers in number:
        container += numbers
    print("Midle number is\t", container / len(number))



def max_number(number):
    print("Your max number is ", max(number))

