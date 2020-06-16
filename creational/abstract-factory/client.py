"""
Abstract Factory design pattern implementation.
This example illustrates the usage of the abstract factory design pattern.

Sample usage of the implemented abstract factory structure.
"""

# Author: 
# Lajos Neto <lajosneto@gmail.com>


from forge_factory import ForgeFactory
from zora_forge import ZoraForge
from rito_forge import RitoForge


def build_equipments(forge: ForgeFactory):
    armor = forge.forge_armor()
    sword = forge.forge_sword()
    shield = forge.forge_shield()

    print(f"Forged Armor : {type(armor).__name__}")
    print(f"Forged Sword : {type(sword).__name__}")
    print(f"Forged Shield : {type(shield).__name__}")


if __name__ == '__main__':
    build_equipments(ZoraForge())
    build_equipments(RitoForge())