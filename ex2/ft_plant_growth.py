#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int, growth_rate: float):
        self.name = name.capitalize()
        self.height = height
        self.days = age
        self.growth_rate = growth_rate

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")

    def grow(self):
        self.height += self.growth_rate

    def age(self):
        self.days += 1


def main():
    print("=== Garden Plant Growth ===")
    plant1: Plant = Plant("Rose", 25, 30, 0.8)
    plant1.show()
    for n in range(1, 8):
        print(f"=== Day {n} ===")
        plant1.grow()
        plant1.age()
        plant1.show()
    print(f"Growth this week: {round(plant1.growth_rate * 7, 1)}cm")


if __name__ == "__main__":
    main()
