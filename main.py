calculation_to_units = 24
name_of_unit = "hours"
current_day = 35
custom_message = "that is very cool"

def days_to_units(days):
    if days > 10:
        return f"{days} days are {days * calculation_to_units} {name_of_unit}"
    else:
        return "Greater than 10"


user_input = input("hey user, enter a number of days na i will cover it to hours \n")
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print(calculated_value)