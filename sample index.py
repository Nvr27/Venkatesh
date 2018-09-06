nums = [1, 2, 3, 4]
i = 0
#
# while i < len(nums):
#     print(i, nums[i]*10)
#     i += 1
# i=0
# for j in range(5):
#     i+=j
# print(i)
#
# while i < 5:
#     i+=1
#
# while i < len(nums):
#     nums[i]= nums[i] + 5
#     print(nums[i])
#     i=i+1
# print(nums)
while i < len(nums):
    nums[i] = nums[i] + i
    i += 1
print(nums)
