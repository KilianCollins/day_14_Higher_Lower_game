# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.


def twoSum(nums: list[int], target: int):
    for x in range(len(nums)):
        for y in range(x +1, len(nums)):
            if nums[y] == target - nums[x]:
                return [nums[x],nums[y]] #
    return []

print(twoSum([9,4,56,7,5,3,2,4,5,6,6,4,3,3,0,1,0,2], 56))












#
# numbers = [1,2,3,4,5,6,]
# # print(len(numbers))
# # target = int(input("enter a integer target: "))
#
# # target = 0
#
# Rnumbers = numbers[::-1]
# mid = int((len(numbers) - 1) / 2)

# for i in numbers[::-1]:
#     print(i)
#
# for i in range(mid+1):
#     # print(Rnumbers[i])
#     x = Rnumbers[i]
#
# for n in range(0, mid + 1):
#     print(numbers[n])
#     y = numbers[n]
#
# for x in numbers:
#     for i in numbers[x-1]:
#         print(9
#         )



# for n in range(mid, len(Rnumbers)+1):
#     print(n)

#     i want this to startr from the end og the list and stop at the middle




#
#
# def sums_that_equal_target(target):
#     mid = int((len(numbers)-1)/2)
#     for x in range(0, --mid):
#         for y in reversed(numbers):
#
#                 if x+y == target:
#                       print(x+y)
#                 else:
#                     print(0)
#
#
# print(sums_that_equal_target(target=target))