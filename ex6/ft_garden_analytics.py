#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0
            self._shade_count = 0

        def display(self, name: str) -> None:
            print(f"[statistics for {name.capitalize()}]")
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, {self._show_count} show"
            )

        def display_shade(self) -> None:
            print(f" {self._shade_count} shade")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)
        self.stats = self.Stats()

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Anonymous", 0.0, 0)

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
        self._height = round(self._height + (days), 1)
        self.stats._grow_count = self.stats._grow_count + 1

    def older(self, days: int) -> None:
        self._age = self._age + days
        self.stats._age_count = self.stats._age_count + 1

    def show(self) -> None:
        print(
            f"{self.name}: {round(self._height, 1)}cm, {self._age} days old"
        )
        self.stats._show_count = self.stats._show_count + 1

    @staticmethod
    def check_age(days: int) -> bool:
        return days > 365


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
        self.is_blooming = True


class Tree(Plant):
    def __init__(
            self, name: str, height: float, age: int, trunk_diameter: float
    ):
        super().__init__(name, height, age)
        self._trunk_diameter = 0.0
        self.set_trunk_diameter(trunk_diameter)

    def set_trunk_diameter(self, value: float) ->None:
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
        self.stats._shade_count = self.stats._shade_count + 1


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


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)
        self.seeds_count = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds count: {self.seeds_count}")

    def bloom(self) -> None:
        super().bloom()
        self.seeds_count = 42


def display_stats(plant: Plant) -> None:
    plant.stats.display(plant.name)


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}\n")

    print("=== Flower")
    flower = Flower("rose", 15.0, 10, "red")
    flower.show()
    display_stats(flower)
    print(f"[Asking the {flower.name} to grow and bloom]")
    flower.grow(5)
    flower.bloom()
    flower.show()
    display_stats(flower)

    print("\n=== Tree")
    tree = Tree("oak", 200.0, 365, 5.0)
    tree.show()
    display_stats(tree)
    tree.stats.display_shade()
    tree.produce_shade()
    display_stats(tree)
    tree.stats.display_shade()

    print("\n=== Seed")
    seed = Seed("sunflower", 80.0, 45, "yellow")
    seed.show()
    print(f"[make {seed.name} grow, age and bloom]")
    seed.grow(30)
    seed.older(20)
    seed.bloom()
    seed.show()
    display_stats(seed)

    print("\n=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    anonymous.stats.display("Unknown plant")


if __name__ == "__main__":
    main()
