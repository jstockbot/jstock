import datetime

now = datetime.datetime.now()

print("{}year {}mon {}day {}hour {}min {}sec".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

last_number = 2

if last_number == 0 \
    or last_number == 2:
    print("even")

array = [1,2,3, False, "song"]
print(array)

number = 0

if number > 0 :
    raise NotImplementedError
else :
    raise NotImplementedError


