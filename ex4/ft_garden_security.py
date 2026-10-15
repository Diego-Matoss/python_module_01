#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> str:
        return (
            f"{self.name}: {round(self._height, 1)}cm, {self._age} days old"
        )


def main() -> None:
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.0, 10)
    print(f"Plant created: {plant.show()}\n")

    plant.set_height(25)
    plant.set_age(30)

    print(f"Height updated: {plant.get_height()}cm")
    print(f"Age updated: {plant.get_age()} days\n")

    plant.set_height(-10)
    plant.set_age(-10)

    print(f"\nCurrent state: {plant.show()}")


if __name__ == "__main__":
    main()
