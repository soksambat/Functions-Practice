# EX7.Create function to count negative number in array [-1,11,2,0,-1,4]
def count_negative_numbers(number):
    return sum(1 for num in number if num < 0)
number7 = [-1, 11, 2, 0, -1, 4]
print(count_negative_numbers(number7)) 