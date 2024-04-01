# for loop
# 1. Find numbers which are divisible by 7 and multiple of 5 between a range 
start = 0  # Start of the range
end = 100  # End of the range
for num in range(start, end + 1):
    if num % 7 == 0 and num % 5 == 0:
        print(num)
print("here is the numbers")  

# 2. Print the following pattern
# 1

# 1   2

# 1   2    3

# 1   2    3      4

n = 4
for i in range(n):
    p=1
    for j in range(i + 1):
        print(p,end=' ')
        p+=1
    print()
print("here is your pattern")    

# 3. Accept number from user an calculate the sum of all numbers between 1 and given number
num = int(input("Enter a number: "))
s= 0
for i in range(1, num + 1):
    s+= i
print("The sum of all numbers between 1 and", num, "is:", s)


##### 4. Print multiplication table of a given number upto a given range

def multiplication_table(number, range_limit):
    for i in range(1, range_limit + 1):
        print(f"{number} x {i} = {number * i}")
number = int(input("Enter the number for multiplication table: "))
range_limit = int(input("Enter the range limit: "))

multiplication_table(number, range_limit)

# 5. Print the total number of digits in a number
number = int(input("Enter a number: "))
num_digits = 0

for digit in str(number):
    if digit.isdigit():
        num_digits += 1
print("Total number of digits:", num_digits)

# 6. Write a program to count number of even and odd number from a series of numbers given by user
even_count = 0
odd_count = 0
numbers = input("Enter a series of numbers separated by spaces: ").split()
for num in numbers:
    if int(num) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)

# 7.Write a program that prints each item and its corresponding type
items = [1, "hello", 3.14, True, [1, 2, 3], {"key": "value"}]
for item in items:
    print(item, ":", type(item))

# Write a program code to construct the following loop
# 5 4 3 2 1

# 4 3 2 1

# 3 2 1

# 2 1

# 1
n=5
k=5    
for i in range(n):
    p=k  
    for j in range(i,n):  
        print(p, end=' ')
        p-=1
    print()  

# 9. Write a pogram code construct the following loop

# 1

# 2  2

# 3   3    3

# 4    4    4   4

# 5    5    5   5   5
n=5
p=1    
for i in range(n):  
    for j in range(i+1):  
      print(p,end=' ')  
    p+=1
    print()  

# 10.Write a program to find the sum of first n natural numbers using a while loop.
def sum_of_natural_numbers(n):
    sum = 0
    count = 1
    while count <= n:
        sum += count
        count += 1
    return sum
# 11. Write a program to print the multiplication table of n using for loop in reversed order.
multi = int(input("Enter the number of multiplication table: "))

ending = int(input("Enter the range limit : "))

for i in range(ending,0,-1):
    print(i,"*",multi,"=",i*multi)

