package creational.abstractFactory

import creational.abstractFactory.equipments.*
import creational.abstractFactory.forges.EquipmentForge

class ForgeMenu(forge: EquipmentForge) {
    private val armor: Armor = forge.forgeArmor()
    private var shield: Shield = forge.forgeShield()
    private var sword: Sword = forge.forgeSword()
    private var spear: Spear = forge.forgeSpear()
    private var bow: Bow = forge.forgeBow()

    fun displayEquipments() {
        print("EQUIPMENT MENU ==================\n")
        print(armor.displayName() + "\n")
        print(shield.displayName() + "\n")
        print(sword.displayName() + "\n")
        print(spear.displayName() + "\n")
        print(bow.displayName() + "\n")
        print("=================================")
    }
}