from __future__ import annotations
from typing import Union


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.hidden = False
        self.health = health
        Animal.alive.append(self)

    def __str__(self) -> str:

        return (f"Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}")

    def __repr__(self) -> str:

        return f"{{{self}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(other: Union[Carnivore, Herbivore]) -> Union[str, None]:
        if isinstance(other, Carnivore):
            return "Carnivore won't bit Carnivore"
        if isinstance(other, Herbivore) and other.hidden:
            return "Carnivore won't be able to bite hidden Herbivore"
        if other.health > 0:
            other.health -= 50
        if other.health <= 0:
            Animal.alive.pop(Animal.alive.index(other))
