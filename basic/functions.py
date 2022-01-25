print(len("howlongisthissentencewillbeyeahhhhhhh"))
age = "23"
print(type(age))
new_age = int(age)
print(type(new_age))


def say_hello(who):
    print("Hello ", who)


say_hello("Nico")


def plus(x, y):
    print(x+y)


plus(54+23, 54-23)


def minus(x, y=10):
    print(x-y)


minus(23)
minus(23, 15)


def plus_return(x, y):
    return x+y


print(plus_return(12, 56))


def say_hello_return(name, age):
    return f"Hello {name} you are {age} years old"


hello = say_hello_return(age="nico", name=12)
print(hello)
