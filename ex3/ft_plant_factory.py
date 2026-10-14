#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int, growth_rate: float):
        self.name = name.capitalize()
        self.height = height
        self.days = age
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.days += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    plants = [
        Plant("Rose", 25.0, 30, 0.8),
        Plant("Oak", 200.0, 365, 1),
        Plant("Cactus", 5.0, 90, 0.1),
        Plant("Sunflower", 80.0, 45, 1.2),
        Plant("Fern", 15.0, 120, 1.1),
    ]

    for plant in plants:
        print("Created: ", end="")
        plant.show()
