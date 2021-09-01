# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name, age):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name} your age is {int(age)}')  # Press Ctrl+F8 to toggle the breakpoint.


def mystat():
    fname = input('your first name: ')
    lname = input('your last name:  ')
    snumber = input('street number: ')
    sname = input('street name: ')
    city = input('city: ')
    print(f"This is me: {fname} {lname}, {snumber} {city} ")
    return fname, lname, snumber, sname, city


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Lalit W', 50)
    fname, lname, snumber, sname, city = mystat()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
