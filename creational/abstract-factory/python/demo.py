"""
Abstract Factory design pattern implementation.
This example illustrates the usage of the abstract factory design pattern.

Sample usage of the implemented abstract factory structure.
"""

# Author: 
# Lajos Neto <lajosneto@gmail.com>

from menu import ForgeMenu
from forges.zora_forge import ZoraForge
from forges.rito_forge import RitoForge


if __name__ == '__main__':
    forge_menu = ForgeMenu(ZoraForge())
    forge_menu.displayEquipments()