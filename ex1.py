import itertools

# Ex1: Write a program to count positive and negative numbers in a list
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]

def count_positive_negative(lst):
    positive_count = 0
    negative_count = 0
    
    for num in lst:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
    
    return positive_count, negative_count

positive, negative = count_positive_negative(data1)

print('ex1: ')
print("Number of positive numbers:", positive)
print("Number of negative numbers:", negative)

# Ex2: Given a list, extract all elements whose frequency is greater than k.
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3

def extract_elements(lst, k):
    for x in lst:
        if (x > k):
            print(x)

print('ex2: ')
extract_elements(data2, k)

# Ex3: find the strongest neighbour. Given an array of N positive integers.
# The task is to find the maximum for every adjacent pair in the array.
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]   

def largest(arr, n):
 
    max = arr[0]
 
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max
 
n = len(data3)
largest_value = largest(data3, n)

print('ex3: ')
print("Largest in given array ", largest_value)

# Ex4: print all Possible Combinations from the three Digits
data4 = [1, 2, 3]

print('ex4: ')

combinations = list(itertools.permutations(data4))
for combo in combinations:
    print(combo)

# Ex5: Given two matrices (2 nested lists), the task is to write a Python program
# to add elements to each row from initial matrix.
    
data5_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]

def add_matrices(matrix1, matrix2):
    new_matrix = []

    for item1, item2 in zip(matrix1, matrix2):
        new_matrix.append(item1 + item2)
    return new_matrix

result_matrix = add_matrices(data5_list1, data5_list2)

print('ex5: ')
print(result_matrix)


# Ex6:  Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

result = []

for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        result.append(num)

print('ex6: ')
print(','.join(map(str, result)))

# Ex7: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Initialize an empty list to store the even numbers
even_numbers = []

for num in range(1000, 3001):
    num_str = str(num)
    all_even = True
    for digit in num_str:
        if int(digit) % 2 != 0:
            all_even = False
            break
    if all_even:
        even_numbers.append(num)

print('ex7: ')
print(','.join(map(str, even_numbers)))

