# EX2.Create function to sum odd number in array [1,2,3,4,5,6]
def sum_odd_numbers(numbers):
    return sum(num for num in numbers if num % 2 != 0)
numbers2 = [1, 2, 3, 4, 5, 6]
print(sum_odd_numbers(numbers2)) 