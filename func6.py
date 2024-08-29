# EX6.Create function to count positive number in array [-1,11,2,0,-1,4]
def count_positive_numbers(number):
    return sum(1 for num in number if num > 0)
number6 = [-1, 11, 2, 0, -1, 4]
print(count_positive_numbers(number6))  