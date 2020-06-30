"""
Abstract Factory design pattern implementation.
This example illustrates the usage of the abstract factory design pattern.

Base ForgeFactory interface.
This is the interface that all specific forges must implement and follow.
"""

# Author: 
# Lajos Neto <lajosneto@gmail.com>


from __future__ import annotations
from abc import ABC, abstractmethod

from equipments import Armor, Sword, Spear, Bow, Shield


class ForgeFactory(ABC):

    @abstractmethod
    def forge_armor(self) -> Armor:
        """
        Forges an armor
        """
        pass

    @abstractmethod
    def forge_sword(self) -> Sword:
        """
        Forges a sword
        """
        pass

    @abstractmethod
    def forge_spear(self) -> Spear:
        """
        Forges a spear
        """
        pass

    @abstractmethod
    def forge_bow(self) -> Bow:
        """
        Forges a bow
        """
        pass

    @abstractmethod
    def forge_shield(self) -> Shield:
        """
        Forges a shield
        """
        pass