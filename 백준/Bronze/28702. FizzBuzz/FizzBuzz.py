import sys
Input = sys.stdin.readline

first = Input().strip()
two =  Input().strip()
three =  Input().strip()
result = 0
a = ["FizzBuzz", "Fizz", "Buzz"]

for _ in range(3):
    if first not in a :
        result = int(first)+3
        break
    elif two not in a :
        result = int(two)+2
        break
    elif three not in a  :
        result = int(three)+1
        break

if (result%3 == 0) & (result%5 == 0) :
    print("FizzBuzz")
elif (result%3 == 0) :
    print("Fizz")
elif (result%5 == 0):
    print("Buzz")
else :
    print(result)