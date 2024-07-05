numbers = [4, -1, 2, -5, 3, -2, 1, -3, 0, 5]

count = 0

for number in numbers:
    if number == 0:
        print(number,"is neutral.")
    elif number < 0:
        print(number, "is negative.")
    else:
        print(number, "is positive.")
        count += 1

print("Total positive numbers:", count)