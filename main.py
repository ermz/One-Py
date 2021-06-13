

def days_to_units(days, unit):
    if unit == "hours":
        return f"{days} days are {days * 24} {unit}"
    elif unit == "minutes":
        return f"{days} days are {days * 24 * 60} {unit}"
    else:
        return "unsupported units"


def validate_and_execute(du_dic):
    try:
        user_input_number = float(du_dic["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, du_dic["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you enter a 0 please enter a valid positive number")
        else:
            print("you entered a negative number, please enter a valid number")
    except ValueError:
        print("Input is not a number. don't ruin my program")


user_input = ""
while user_input != "exit":
    user_input = input("hey user, enter a number of days and conversion \n")
    days_and_units = user_input.split(":")
    print(days_and_units)
    days_and_units_dic = {"days": days_and_units[0], "unit": days_and_units[1]}
    print(days_and_units_dic)
    validate_and_execute(days_and_units_dic)
    # validate_and_execute(days_and_units_dic("days"))

