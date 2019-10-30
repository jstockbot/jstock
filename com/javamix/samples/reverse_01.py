numbers = [1,2,3,4,5]
nums = reversed(numbers)


print(numbers)
print(numbers[::-1])
print(numbers)

for i in nums:
    print(i)

for i in reversed(numbers):
    print(i)


print(list(enumerate(numbers)))

for i, value in enumerate(numbers):
    print("{}번째는 {}".format(i, value))