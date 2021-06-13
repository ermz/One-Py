calculation_to_units = 24
name_of_unit = "hours"
current_day = 35
custom_message = "that is very cool"

def days_to_units(days):
    return f"{days} days are {days * calculation_to_units} {name_of_unit}"


def validate_and_execute(number):
    try:
        user_input_number = float(number)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you enter a 0 please enter a valid positive number")
        else:
            print("you entered a negative number, please enter a valid number")
    except ValueError:
        print("Input is not a number. don't ruin my program")


user_input = ""
while user_input != "exit":
    user_input = input("hey user, enter a number of days or list of days and I will cover it to hours \n")
    print("hello")
    if list(user_input):
        for element in user_input.split():
            validate_and_execute(element)
    else:
        validate_and_execute(user_input)


