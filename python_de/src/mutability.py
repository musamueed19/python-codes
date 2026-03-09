array = [1, "two", 3, "four"]

def number():
    array.append(5)
    return array

def alfha():
    array.append("six")
    return array

print("numeric function", number())
print("alfha function", alfha())