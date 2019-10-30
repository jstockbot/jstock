# def power(item):
#     return item * item
# def under_3(item):
#     return item <= 3
power = lambda x : x * x
under_3 = lambda x : x < 3

list_input_a = [1,2,3,4,5]

output_a = map(power, list_input_a)

print(output_a)
print("결과 리스트 = {}".format(list(output_a)))

output_b = filter(under_3, list_input_a)
print(output_b)
print("type = {}, 결과값 = {}".format(type(output_b), list(output_b)))