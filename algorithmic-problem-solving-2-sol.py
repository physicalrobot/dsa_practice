# We need to find the sum of all mulitples of 3 and 5 below 1000. 
# We can start by iterating to 1000 and saving all the values that are divisible by 3 and 5 in a value and adding to the value when hit another divisible number.


def sum_of_multiples(n):
    sum = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(sum_of_multiples(1000))


# Test Case

# Example 1

# n = 10
# 3,5,6,9
# sum = 23

print(sum_of_multiples(10))



