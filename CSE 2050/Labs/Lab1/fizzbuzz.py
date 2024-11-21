def fizzbuzz(start, finish):
    "replace 3 with fizz and 5 with buzz"
    for i in range(start,finish + 1):
        if (i % 5 == 0 or "5" in str(i)) and (i % 3 == 0 or "3" in str(i)):
            print("fizzbuzz")
        elif i % 3 == 0 or "3" in str(i):
            print("fizz")
        elif i % 5 == 0 or "5" in str(i):
            print("buzz")
        else:
            print(i)