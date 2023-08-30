class Car:

    def __init__(self, company, model, color, speed):
        self.company=company
        self.model=model
        self.color=color
        self.speed=speed

    def increase_speed(self, value):
        self.speed+=value

    def decrease_speed(self, value):
        self.speed-=value

    def __str__(self):
        return f"A {self.company} car that is {self.color} is moving at {self.speed}mph."

carnival=Car("Kia", "Carnival", "white", 149)
print(carnival)
carnival.increase_speed(6)
print("The speed increased to "+str(carnival.speed)+"mph")
carnival.decrease_speed(8)
print("The speed decreased to "+str(carnival.speed)+"mph")
print(carnival)