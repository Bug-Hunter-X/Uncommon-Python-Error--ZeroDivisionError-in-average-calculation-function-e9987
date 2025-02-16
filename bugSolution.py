def calculate_average(numbers):
    if not numbers:
        return 0
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("List must contain only numbers.")
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_mixed_list = [10, 20, 'a', 40, 50]
try:
    average_mixed = calculate_average(my_mixed_list)
    print(f"The average is: {average_mixed}")
except ValueError as e:
    print(f"Error: {e}")
