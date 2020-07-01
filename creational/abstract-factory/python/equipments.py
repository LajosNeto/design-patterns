"""
Abstract Factory design pattern implementation.
This example illustrates the usage of the abstract factory design pattern.

Abstract implementation of all kinds of equipments a forge can handle.
"""

# Author: 
# Lajos Neto <lajosnetogit@gmail.com>


from abc import ABC, abstractmethod


class Armor(ABC):
    """
    Abtract implementation of an Armor
    """
    @abstractmethod
    def display_name(self):
        pass
    
    @abstractmethod
    def defend(self, attack):
        pass


class Sword(ABC):
    """
    Abtract implementation of a Sword
    """
    @abstractmethod
    def display_name(self):
        pass

    @abstractmethod
    def slash(self):
        pass

class Spear(ABC):
    """
    Abtract implementation of a Spear
    """
    @abstractmethod
    def display_name(self):
        pass

    @abstractmethod
    def pierce(self):
        pass


class Bow(ABC):
    """
    Abtract implementation of a Bow
    """
    @abstractmethod
    def display_name(self):
        pass

    @abstractmethod
    def shoot(self):
        pass


class Shield(ABC):
    """
    Abtract implementation of a Shield
    """
    @abstractmethod
    def display_name(self):
        pass
    
    @abstractmethod
    def block(self, attack):
        pass