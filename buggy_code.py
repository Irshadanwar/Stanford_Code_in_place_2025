# buggy_code.py – Sample Python file with bugs for testing GPT Code Buddy

def find_average(numbers):
    total = 0
    for i in range(numbers):
        total += numbers[i]
    average = total / len(numbers)
    return averge  # typo: should be 'average'

nums = [10, 20, 30, 40, 50]

print("The average is:", find_avarage(nums))  # typo in function name
