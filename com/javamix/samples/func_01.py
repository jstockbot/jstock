def print_n_time(value, n=2):
    for i in range(n):
        print(value)
        
def print_n_time2(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

def print_n_time3(*values, n=3):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_time("안녕하세요.", 10)

print_n_time3("오송열","자바믹스","안녕하세요")