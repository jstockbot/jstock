counter = 0
def fibonacci(n) :
    print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter += 1
    if n == 1 :
        return 1
    if n == 2 :
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)

print("value = {}".format(fibonacci(10)))
print("덧셈 횟수는 {}".format(counter))