pencils = ""


def jack_bot():
    global pencils
    print(pencils)
    print(f"Jack's turn")
    if len(pencils) % 4 == 0:
        pencils = pencils.replace("|", "", 3)
        print('3')
    elif len(pencils) % 4 == 3:
        pencils = pencils.replace("|", "", 2)
        print('2')
    elif len(pencils) % 4 == 2:
        pencils = pencils.replace("|", "", 1)
        print('1')
    else:
        pencils = pencils.replace("|", "", 1)
        print('1')
    if len(pencils) == 0:
        print("John won!")
    else:
        john()


def john():
    global pencils
    print(pencils)
    print(f"John's turn!")
    amount = input()
    while amount not in ["1", "2", "3"]:
        print("Possible values: '1', '2' or '3'")
        amount = input()

    while int(amount) > len(pencils):
        print("Too many pencils were taken")
        amount = input()
        while amount not in ["1", "2", "3"]:
            print("Possible values: '1', '2' or '3'")
            amount = input()
    pencils = pencils.replace("|", "", int(amount))
    if len(pencils) == 0:
        print("Jack won!")
    else:
        jack_bot()


num_pencils = input("How many pencils would you like to use: ")

while not num_pencils.isdigit():
    print("The number of pencils should be numeric")
    num_pencils = input()
while int(num_pencils) <= 0:
    print("The number of pencils should be positive")
    num_pencils = input()
    while not num_pencils.isdigit():
        print("The number of pencils should be numeric")
        num_pencils = input()

pencils = "|" * int(num_pencils)
first_person = input("Who will be the first (John, Jack):").capitalize()

while first_person != "John" and first_person != "Jack":
    print("Choose between 'John' and 'Jack'")
    first_person = input().capitalize()

if first_person == "Jack":
    jack_bot()
elif first_person == "John":
    john()
