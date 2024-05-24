"""Zoo."""


class Animal:
    """Animal class."""

    def __init__(self, name: str, specie: str, age: int):
        """
        Class constructor.

        Each animal has a name and a specie.
        :param name: animal name
        :param specie: animal specie
        """
        self.name = name
        self.specie = specie
        self.age = age


class Zoo:
    """Zoo class."""
    def __init__(self, name: str, max_number_of_animals: int):
        """
        Class constructor.

        Each zoo has a name and max number of animals the zoo can have.
        There also should be an overview of all animals present in the zoo.

        :param name: zoo name
        :param max_number_of_animals: how many animals can be in the zoo
        """
        self.name = name
        self.max_number_of_animals = max_number_of_animals
        self.animals = []

z = Zoo("zoo", 50)

    def can_add_animal(self, animal: Animal) -> bool:
        """
        Check if animal can be added to the zoo.

        Animal can be added to the zoo if:
        1. Adding a new animal does not exceed zoo's max number of animals.
        2. Same Animal object is not present in the zoo.
        3. Animal with same name and specie is not yet present in the zoo.
        :param animal: animal who is checked
        :return: bool describing whether the animal can be added to the zoo or not
        """
        if len(self.animals) >= self.max_number_of_animals:
            for i in self.animals:
                if i == animal:
                    return False
                else:
                    return True
        else:
            return False
    def add_animal(self, animal: Animal):
        """
        Add animal to the zoo if possible.

        :param animal: animal who is going to be added to the zoo
        Function does not return anything
        """
        pass

    def can_remove_animal(self, animal: Animal) -> bool:
        """
        Check if animal can be removed from the zoo.

        Animal can be removed from the zoo if animal is present in the zoo.

        :param animal: animal who is checked
        :return: bool describing whether animal can be removed from the zoo or not.
        """
        pass

    def remove_animal(self, animal: Animal):
        """
        Remove animal from the zoo if possible.

        :param animal: animal who is going to be removed from the zoo.
        Function does not return anything
        """
        pass

    def get_all_animals(self):
        """
        Return a list with all the animals in the zoo.

        :return: list of Animal objects
        """
        pass

    def get_animals_by_age(self):
        """
        Return a list of animals sorted by age (from younger to older).

        :return: list of Animal objects sorted by age
        """
        pass

    def get_animals_sorted_alphabetically(self):
        """
        Return a list of animals sorted (by name) alphabetically.

        :return: list of Animal objects sorted by name alphabetically
        """
        pass
