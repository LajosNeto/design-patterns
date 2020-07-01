"""
Sample forging menu : displays equipments available
for a given tribe.
"""

# Author: 
# Lajos Neto <lajosneto@gmail.com>

class ForgeMenu():
    def __init__(self, forge):
        self.forge = forge
        self.armor = forge.forge_armor()
        self.shield = forge.forge_shield()
        self.sword = forge.forge_sword()
        self.spear = forge.forge_spear()
        self.bow = forge.forge_bow()
    
    def displayEquipments(self) :
        print("\nEQUIPMENT MENU ==================\n")
        print(self.armor.display_name() + "\n")
        print(self.shield.display_name() + "\n")
        print(self.sword.display_name() + "\n")
        print(self.spear.display_name() + "\n")
        print(self.bow.display_name() + "\n")
        print("=================================\n")
