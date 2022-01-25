def plus(x, y):
    if type(y) is int or type(y) is float:
        return x+y
    else:
        return None


print(plus(12, 3.5))


def age_check(age):
    print(f"You are {age} years old")
    if age < 18:
        print("You can't drink yet")
    elif age == 18 or age == 19:
        print("You are new to this")
    elif age < 25 and age > 20:
        print("You are still young")
    else:
        print("Enjoy yourself")


age_check(23)
