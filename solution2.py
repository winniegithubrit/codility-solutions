# def print_numbers():
#     for i in range(5):  
#         print(i)

# print_numbers()

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num

    average = total / len(numbers)
    return average 

numbers = [10, 20, 30, 40, 50]
print(calculate_average(numbers))
