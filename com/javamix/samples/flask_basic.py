def test(function):
    def wrapper2():
        print("Start")
        function()
        print("End")
    return wrapper2

@test
def hello():
    print("hello")

hello()