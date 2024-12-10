from __future__ import annotations
from typing import Union


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.hidden = False
        self.health = health
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{"
                f"Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(other: Union[Carnivore, Herbivore]) -> str | None:
        if isinstance(other, Carnivore):
            return
        if isinstance(other, Herbivore) and other.hidden:
            return
        other.health -= 50
        if other.health <= 0:
            Animal.alive.pop(Animal.alive.index(other))
