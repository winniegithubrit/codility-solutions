def find_missing_number(nums):
  # get the length of the inputed array
    n = len(nums)
    # calculating the sum of the first n natural numbers
    total_sum = (n * (n + 1)) // 2
    # calculate the sum of the elements in the input array
    array_sum = sum(nums)
    # calculate the missing number by subtracting from the total
    missing_number = total_sum - array_sum
    # return the missing number
    return missing_number

# testing
nums = [3, 1, 0, 4, 5]
print("The missing number is:", find_missing_number(nums))  
