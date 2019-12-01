"""
Abstract Factory design pattern implementation.
This example illustrates the usage of the abstract factory design pattern.
"""

# Author: 
# Lajos Neto <lajosnetogit@gmail.com>


from __future__ import annotations
from abc import ABC, abstractmethod


####################################################
# Forge and weapons base abstract classes used on all
# concrete implementation which the user have access to.
####################################################

class Forge(ABC):
    """
    Base Forge class.
    This is the main factory abstract class.
    This abstract class specifies which methods should all other factories implement,
    enforcing an interface to be followed.
    """
    
    @abstractmethod
    def smith_dagger(self) -> Dagger:
        pass

    @abstractmethod
    def smith_sword(self) -> Sword:
        pass

    @abstractmethod
    def smith_bow(self) -> Bow:
        pass


class Dagger(ABC):
    """
    Abstract class for a dagger.
    All dagger concrete classes should implement this abstract class.
    """
    @abstractmethod
    def thrust(self):
        pass


class Sword(ABC):
    """
    Abstract class for a sword.
    All sword concrete classes should implement this abstract class.
    """

    @abstractmethod
    def slash(self):
        pass


class Bow(ABC):
    """
    Abstract class for a bow.
    All sword concrete classes should implement this abstract class.
    """

    @abstractmethod
    def draw(self):
        pass

####################################################
# Concrete implementations for all weapons
####################################################

class EbonyDagger(Dagger):
    def __str__(self):
        return 'Ebony Dagger'

    def thrust(self):
        return 10

class EbonySword(Sword):
    def __str__(self):
        return 'Ebony Sword'

    def slash(self):
        return 13

class EbonyBow(Bow):
    def __str__(self):
        return 'Ebony Bow'

    def draw(self):
        return 17

class DaedricDagger(Dagger):
    def __str__(self):
        return 'Daedric Dagger'

    def thrust(self):
        return 11

class DaedricSword(Sword):
    def __str__(self):
        return 'Daedric Sword'

    def slash(self):
        return 14

class DaedricBow(Bow):
    def __str__(self):
        return 'Daedric Bow'

    def draw(self):
        return 19

####################################################
#  Concrete implementation of all forges
####################################################

class EbonyForge(Forge):
    """
    Concrete implementation of a Forge.
    This Ebony Forge class implementes all methods described withins its base 
    abstract class, the Forge abstract base class.
    """

    def smith_dagger(self) -> EbonyDagger:
        return EbonyDagger()
    
    def smith_sword(self) -> EbonySword:
        return EbonySword()
    
    def smith_bow(self) -> EbonyBow:
        return EbonyBow()

class DaedricForge(Forge):
    """
    Concrete implementation of a Forge.
    This Daedric Forge class implementes all methods described withins its base 
    abstract class, the Forge abstract base class.
    """
    def smith_dagger(self) -> DaedricDagger:
        return DaedricDagger()
    
    def smith_sword(self) -> DaedricSword:
        return DaedricSword()
    
    def smith_bow(self) -> DaedricBow:
        return DaedricBow()

####################################################
# Implementation of a class to access Forge methods
####################################################

class ForgingMenu():
    """
    Class providing user access to all available smith methods.
    This class works through the abstract Forge abstract type.
    We can pass any of the Forges to the user class and keep a
    consistent behaviour.
    """
    def __init__(self, forge: Forge):
        self.forge = forge
    
    def create_dagger(self) -> Dagger:
        return self.forge.smith_dagger()
    
    def create_sword(self) -> Sword:
        return self.forge.smith_sword()
    
    def create_bow(self) -> Bow:
        return self.forge.smith_bow()


if(__name__ == '__main__'):
    print("\n")
    menu = ForgingMenu(EbonyForge())
    dagger = menu.create_dagger()
    sword = menu.create_sword()
    bow = menu.create_bow()
    print("Forged weapon: {0} //// Attack points: {1}".format(dagger, dagger.thrust()))
    print("Forged weapon: {0} //// Attack points: {1}".format(sword, sword.slash()))
    print("Forged weapon: {0} //// Attack points: {1}".format(bow, bow.draw()))

    print("\n")

    menu = ForgingMenu(DaedricForge())
    dagger = menu.create_dagger()
    sword = menu.create_sword()
    bow = menu.create_bow()
    print("Forged weapon: {0} //// Attack points: {1}".format(dagger, dagger.thrust()))
    print("Forged weapon: {0} //// Attack points: {1}".format(sword, sword.slash()))
    print("Forged weapon: {0} //// Attack points: {1}".format(bow, bow.draw()))
    print("\n")
