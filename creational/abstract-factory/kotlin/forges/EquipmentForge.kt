package creational.abstractFactory.forges

import creational.abstractFactory.equipments.Armor
import creational.abstractFactory.equipments.Bow
import creational.abstractFactory.equipments.Spear
import creational.abstractFactory.equipments.Sword
import creational.abstractFactory.equipments.Shield

interface EquipmentForge {
    fun forgeArmor(): Armor
    fun forgeSword(): Sword
    fun forgeSpear(): Spear
    fun forgeBow(): Bow
    fun forgeShield(): Shield
}