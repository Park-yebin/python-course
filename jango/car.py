class Car():
    # class 안에 있는 def(function)을 method라고 부른다.
    def __str__(self):
        return f"Car with {self.wheels}wheels"

    def __init__(self, *args, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    def take_off(self):
        return "not taking off"


class Convertible(Car):  # car을 쓰면 car의 요소들을 얘도 쓸 수 있음
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Car의 init요소들이 모두 없어지고 얘만 존재하게 됨 그래서 super().__init__사용
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "taking off"

    def __str__(self):
        return f"Car with no roof"


porche = Car(color="green", price="$40")
print(porche.color, porche.price)
mini = Convertible()
print(mini.color, mini.price)
