#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name.capitalize()
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

    def grow(self, days: int) -> None:
        self._height = round(self._height + (2.1 * days), 1)

    def older(self, days: int) -> None:
        self._age = self._age + days

    def show(self) -> None:
        print(
            f"{self.name}: {round(self._height, 1)}cm, {self._age} days old"
        )


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    def bloom(self) -> None:
        print(f"[Asking the {self.name} to bloom]")
        self.is_blooming = True


class Tree(Plant):
    def __init__(
            self, name: str, height: float, age: int, trunk_diameter: float
    ):
        super().__init__(name, height, age)
        self._trunk_diameter = 0.0
        self.set_trunk_diameter(trunk_diameter)

    def set_trunk_diameter(self, value: float) -> None:
        if value < 0:
            print("You can't set a negative trunk diameter")
        else:
            self._trunk_diameter = value

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.get_trunk_diameter()}")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.get_height()}cm long and "
            f"{self.get_trunk_diameter()}cm wide."
        )


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            harvest_season: str,
    ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season.capitalize()
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(
            f"Harvest season: {self.harvest_season}\n"
            f"Nutritional value: {self.nutritional_value}"
        )

    def grow(self, days: int) -> None:
        super().grow(days)

    def older(self, days: int) -> None:
        super().older(days)
        self.nutritional_value = self.nutritional_value + (days)


def main() -> None:
    print("=== Garden Plant Types ===\n=== Flower")
    flower = Flower("rose", 15.0, 10, "red")
    flower.show()
    flower.bloom()
    flower.show()

    print("\n===Tree")
    tree = Tree("oak", 200.0, 365, 5.0)
    tree.show()
    tree.produce_shade()

    print("\n===Vegetable")
    vegetable = Vegetable("tomato", 5.0, 10, "april")
    vegetable.show()
    vegetable.grow(20)
    vegetable.older(20)
    print(
        f"[make {vegetable.name}"
        f" grow and age for {vegetable.nutritional_value} days]"
        )
    vegetable.show()


if __name__ == "__main__":
    main()
