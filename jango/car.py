class Car():
    wheels = 4
    doors = 4
    windows = 4
    seats = 4
# class 안에 있는 def(function)을 method라고 부른다.

    def start(potato):
        print(potato.color)
        print("start")


porche = Car()
porche.color = "Red"
porche.start()
