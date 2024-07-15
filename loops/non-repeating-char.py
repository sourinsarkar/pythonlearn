input_str = "sarkar"

# find first non repeating character

for char in input_str:
    if input_str.count(char) == 1:
        print(char)
        break
