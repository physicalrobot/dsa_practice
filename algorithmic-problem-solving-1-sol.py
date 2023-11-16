# Look through the given array for an element that doesn't repeat.

def singleNumber(nums):
    # Initialize a variable to store the single element
    single_element = 0

    # XOR all the elements in the array
    for num in nums:
        single_element ^= num

    return single_element


# Test Cases

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

print(singleNumber([2,2,1]))

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

print(singleNumber([4,1,2,1,2]))

# Example 3:
# Input: nums = [1]
# Output: 1

print(singleNumber([1]))
