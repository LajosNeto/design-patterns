"""
Abstract Factory design pattern implementation.
This example illustrates the usage of the abstract factory design pattern.

Implements the Zora Forge, a concrete implementation of a forge.
"""

# Author: 
# Lajos Neto <lajosneto@gmail.com>


from __future__ import annotations
from abc import ABC, abstractmethod

from .forge_factory import ForgeFactory
from equipments import Armor, Sword, Spear, Bow, Shield


class ZoraForge(ForgeFactory):
    
    def forge_armor(self):
        return ZoraArmor()
    
    def forge_sword(self):
        return SilverLongSword()
    
    def forge_spear(self):
        return SilverscaleSpear()
    
    def forge_bow(self):
        return SilverBow()
    
    def forge_shield(self):
        return SilverShield()

class ZoraArmor(Armor):
    """
    Zora armor variant
    """
    def display_name(self):
        return "Zora Armor, 25 defense"

    def defend(self, attack):
        defense_rate = attack - 25
        return defense_rate if defense_rate > 0 else 0

class SilverShield(Shield):
    """
    Zora shield variant
    """
    def display_name(self):
        return "Silver Shield, 20 defense"

    def block(self, attack):
        block_rate = attack - 20
        return block_rate if block_rate > 0 else 0

class SilverLongSword(Sword):
    """
    Zora sword variant
    """
    def display_name(self):
        return "Silver Long Sword, 22 attack"

    def slash(self):
        return 22

class SilverscaleSpear(Spear):
    """
    Zora spear variant
    """
    def display_name(self):
        return "Silver Scale Spear, 12 attack"

    def pierce(self):
        return 12

class SilverBow(Bow):
    """
    Zora bow variant
    """
    def display_name(self):
        return "Silver Bow, 15 attack"

    def shoot(self):
        return 15