#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plant1: Plant = Plant("rose", 25, 30)
    plant2: Plant = Plant("sunflower", 80, 45)
    plant3: Plant = Plant("cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    plant1.show()
    plant2.show()
    plant3.show()
