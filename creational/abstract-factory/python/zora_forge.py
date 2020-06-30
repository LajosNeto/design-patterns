"""
Abstract Factory design pattern implementation.
This example illustrates the usage of the abstract factory design pattern.

Implements the Zora Forge, a concrete implementation of a forge.
"""

# Author: 
# Lajos Neto <lajosneto@gmail.com>


from __future__ import annotations
from abc import ABC, abstractmethod

from forge_factory import ForgeFactory
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
    def defend(self, attack):
        defense_rate = attack - 25
        return defense_rate if defense_rate > 0 else 0

class SilverLongSword(Sword):
    """
    Zora sword variant
    """
    def slash(self):
        return 22

class SilverscaleSpear(Spear):
    """
    Zora spear variant
    """
    def pierce(self):
        return 12

class SilverBow(Bow):
    """
    Zora bow variant
    """
    def shoot(self):
        return 15

class SilverShield(Shield):
    """
    Zora shield variant
    """
    def block(self, attack):
        block_rate = attack - 20
        return block_rate if block_rate > 0 else 0